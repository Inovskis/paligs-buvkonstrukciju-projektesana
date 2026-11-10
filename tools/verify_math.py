import os
import re
import sys

# HTML tabulās (<table>...</table>) Markdown atkāpšanās netiek apstrādāta, tāpēc tur MathJax
# norobežotājiem jābūt ar vienu slīpsvītru: \( ... \). Šajos blokos vienas slīpsvītras
# norobežotāji ir pareizi; tos aizstāj ar tukšumu (saglabājot rindu skaitu) pirms pārbaudes.
HTML_TABLE = re.compile(r'<table[\s\S]*?</table>')
SINGLE_BACKSLASH = re.compile(r'(?<!\\)\\[\[\]()]')

def mask_html_tables(text):
    return HTML_TABLE.sub(lambda m: SINGLE_BACKSLASH.sub('  ', m.group(0)), text)

def verify_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = mask_html_tables(f.read())

    # Remove code blocks
    text_clean = re.sub(r'```[\s\S]*?```', '', text)
    # Remove inline code
    text_clean = re.sub(r'`[^`\n]*?`', '', text_clean)
    
    # Search for any $ that is not escaped
    matches = list(re.finditer(r'(?<!\\)\$', text_clean))
    
    # Search for any single backslash \[ or \] or \( or \)
    single_backslash_matches = list(re.finditer(r'(?<!\\)\\\[|(?<!\\)\\\]|(?<!\\)\\\(|(?<!\\)\\\)', text_clean))
    
    errors = []
    if matches or single_backslash_matches:
        lines = text.splitlines()
        for line_no, line in enumerate(lines, 1):
            line_clean = re.sub(r'`[^`\n]*?`', '', line)
            
            # Check for unescaped $ or single backslash delimiters
            if re.search(r'(?<!\\)\$', line_clean) or re.search(r'(?<!\\)\\\[|(?<!\\)\\\]|(?<!\\)\\\(|(?<!\\)\\\)', line_clean):
                errors.append((line_no, line))
            
    return errors

def main():
    # Target the src directory relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(os.path.dirname(script_dir), 'src')
    
    has_errors = False
    
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                errors = verify_file(filepath)
                if errors:
                    # Double check if any error is just false positive from multiline code blocks
                    actual_errors = []
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = mask_html_tables(f.read())
                    content_clean = re.sub(r'```[\s\S]*?```', '', content)
                    if re.search(r'(?<!\\)\$', content_clean) or re.search(r'(?<!\\)\\\[|(?<!\\)\\\]|(?<!\\)\\\(|(?<!\\)\\\)', content_clean):
                        for line_no, line_content in errors:
                            lines_before = content.splitlines()[:line_no-1]
                            full_text_before = "\n".join(lines_before)
                            backticks_count = full_text_before.count('```')
                            if backticks_count % 2 == 0: # Even number means we are outside code block
                                actual_errors.append((line_no, line_content))
                                
                    if actual_errors:
                        has_errors = True
                        rel_path = os.path.relpath(filepath, src_dir)
                        print(f"ERROR: Found raw math delimiters in '{rel_path}':")
                        for line_no, content in actual_errors:
                            print(f"  Line {line_no}: {content.strip()}")
                        
    if has_errors:
        print("\nVerification FAILED. Please convert the above raw $ delimiters to \\(...\\) or \\[...\\].")
        sys.exit(1)
    else:
        print("Verification SUCCESSFUL. All math delimiters are properly formatted.")
        sys.exit(0)

if __name__ == '__main__':
    main()
