#!/usr/bin/python3
"""Markdown to HTML converter"""

if __name__ == "__main__":

    import sys
    import os

    if len(sys.argv) < 3:
        sys.exit("Usage: ./markdown2html.py README.md README.html")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit(f"Missing {sys.argv[1]}")

    text = []
    in_list = False  
    list_type = None  

    with open(sys.argv[1], encoding='utf-8') as md_file:
        for line in md_file:
            line = line.rstrip()

            
            if line.startswith("#"):
                heading_level = len(line.split(' ')[0])
                if heading_level < 7:
                    heading_text = " ".join(line.split(' ')[1:])
                    text.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")

            
            elif line.lstrip().startswith(tuple(f"{i}." for i in range(1, 10))):
                if not in_list or list_type != "ol":
                    if in_list:
                        text.append(f"</{list_type}>")
                    in_list = True
                    list_type = "ol"
                    text.append("<ol>")
                list_item = line.lstrip().split('. ', 1)[1]
                text.append(f"<li>{list_item}</li>")

            
            elif line.lstrip().startswith("- "):
                if not in_list or list_type != "ul":
                    if in_list:
                        text.append(f"</{list_type}>")
                    in_list = True
                    list_type = "ul"
                    text.append("<ul>")
                list_item = line.lstrip()[2:]
                text.append(f"<li>{list_item}</li>")

            
            else:
                if in_list:
                    text.append(f"</{list_type}>")
                    in_list = False
                    list_type = None
                text.append(line)

        
        if in_list:
            text.append(f"</{list_type}>")

    with open(sys.argv[2], 'w', encoding='utf-8') as html_file:
        html_file.write('\n'.join(text) + '\n')
