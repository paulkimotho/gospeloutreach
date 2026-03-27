import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

link_map = {
    '>Home<': 'href="index.html">Home<',
    '>About Us<': 'href="about.html">About Us<',
    '>Ministries<': 'href="events.html">Ministries<',
    '>Sermons<': 'href="sermons.html">Sermons<',
    '>Contact<': 'href="contact.html">Contact<',
    '>Give<': 'href="give.html">Give<',
    '>Events<': 'href="events.html">Events<'
}

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # We will replace `href="#" >Text<` or `href="#">Text<`
    for key, repl in link_map.items():
        text = key[1:-1] # Extract 'Home' from '>Home<'
        # Regex to find href="#" followed by the exact text
        content = re.sub(rf'href\s*=\s*["\']#["\']\s*>{text}<', repl, content)
        
    # Also update "New Here" or "Get Involved" to maybe go to contact
    content = re.sub(r'href\s*=\s*["\']#["\']([^>]*)>\s*New Here\s*<', r'href="contact.html"\1>\n                New Here\n            <', content)
    
    with open(file, 'w') as f:
        f.write(content)

print("Links updated.")
