import urllib.request
import urllib.parse
import re
import concurrent.futures

def check_tag(tag):
    formula_enc = tag.replace(r'\textcolor', r'\color')
    encoded = urllib.parse.quote(formula_enc, safe='~()*!.\'\\')
    url = f"https://latex.codecogs.com/svg.image?{encoded}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            if '<svg' in text and 'dvisvgm' in text:
                return tag, True
            else:
                return tag, False
    except Exception as e:
        return tag, False

def main():
    with open('latex_plugin.plugin', 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'self\.help_categories\s*=\s*(\{.*?\n\s*\})', content, re.DOTALL)
    if not match:
        print("Could not find self.help_categories")
        return

    dict_str = match.group(1)
    local_env = {}
    try:
        exec(f"help_categories = {dict_str}", {}, local_env)
        categories = local_env['help_categories']
    except Exception as e:
        print(f"Failed to parse dict: {e}")
        return

    all_tags = [tag for tags in categories.values() for tag in tags]
    print(f"Testing {len(all_tags)} tags...")

    invalid_tags = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_tag, tag): tag for tag in all_tags}
        for future in concurrent.futures.as_completed(futures):
            tag, is_valid = future.result()
            if not is_valid:
                invalid_tags.append(tag)
                print(f"INVALID: {tag}")

    print(f"\nFound {len(invalid_tags)} invalid tags.")
    if not invalid_tags:
        return

    new_content = content
    for tag in invalid_tags:
        # We need to escape the backslashes and regex chars in the tag
        # e.g., "\bra{\phi}" -> "\\\\bra\\{\\phi\\}"
        escaped_tag = re.escape(tag)
        
        # Match r"tag", or r'tag', with optional trailing comma and spaces
        pattern1 = r'r(["\'])' + escaped_tag + r'\1\s*,\s*'
        pattern2 = r'r(["\'])' + escaped_tag + r'\1'
        
        new_content = re.sub(pattern1, '', new_content)
        new_content = re.sub(pattern2, '', new_content)

    # Clean up empty lines that might have been left
    new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)

    with open('latex_plugin.plugin', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Removed invalid tags and updated latex_plugin.plugin")

if __name__ == '__main__':
    main()
