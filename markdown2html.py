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
    in_paragraph = False  

    with open(sys.argv[1], encoding='utf-8') as md_file:
        for line in md_file:
            line = line.rstrip()

            
            if line.startswith("#"):
                if in_paragraph:
                    text.append("</p>")
                    in_paragraph = False
                if in_list:
                    text.append(f"</{list_type}>")
                    in_list = False
                    list_type = None
                heading_level = len(line.split(' ')[0])
                heading_text = " ".join(line.split(' ')[1:])
                text.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")


            elif line.lstrip().startswith("- "):
                if in_paragraph:
                    text.append("</p>")
                    in_paragraph = False
                if not in_list or list_type != "ul":
                    if in_list:
                        text.append(f"</{list_type}>")
                    in_list = True
                    list_type = "ul"
                    text.append("<ul>")
                list_item = line.lstrip()[2:]
                text.append(f"<li>{list_item}</li>")


            elif line.strip():
                if in_list:
                    text.append(f"</{list_type}>")
                    in_list = False
                    list_type = None
                if not in_paragraph:
                    text.append("<p>")
                    in_paragraph = True
                else:
                    text.append("<br/>")
                text.append(line.strip())


            else:
                if in_paragraph:
                    text.append("</p>")
                    in_paragraph = False
                if in_list:
                    text.append(f"</{list_type}>")
                    in_list = False
                    list_type = None


        if in_paragraph:
            text.append("</p>")
        if in_list:
            text.append(f"</{list_type}>")

    with open(sys.argv[2], 'w', encoding='utf-8') as html_file:
        html_file.write('\n'.join(text) + '\n')
