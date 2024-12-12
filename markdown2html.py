#!/usr/bin/python3
"""Markdown to HTML converter"""

if __name__ == "__main__":

    import sys
    import os
    import re

    if len(sys.argv) < 3:
        sys.exit("Usage: ./markdown2html.py README.md README.html")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit(f"Missing {sys.argv[1]}")

    text = []
    in_list = False  # Track if we are inside a list
    list_type = None  # Track the type of list ('ul')
    in_paragraph = False  # Track if we are inside a paragraph

    def parse_inline_markdown(line):
        """
        Replaces inline Markdown syntax with HTML tags:
        **text** -> <b>text</b>
        __text__ -> <em>text</em>
        """
        line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)  # Bold
        line = re.sub(r'__(.+?)__', r'<em>\1</em>', line)  # Italic
        return line

    with open(sys.argv[1], encoding='utf-8') as md_file:
        for line in md_file:
            line = line.rstrip()

            # Process headings
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
                heading_text = parse_inline_markdown(heading_text)
                text.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")

            # Process unordered lists with `-`
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
                list_item = parse_inline_markdown(list_item)
                text.append(f"<li>{list_item}</li>")

            # Process paragraphs
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
                text.append(parse_inline_markdown(line.strip()))

            # Handle empty lines (end of a paragraph or list)
            else:
                if in_paragraph:
                    text.append("</p>")
                    in_paragraph = False
                if in_list:
                    text.append(f"</{list_type}>")
                    in_list = False
                    list_type = None

        # Close any open tags at the end of the file
        if in_paragraph:
            text.append("</p>")
        if in_list:
            text.append(f"</{list_type}>")

    with open(sys.argv[2], 'w', encoding='utf-8') as html_file:
        html_file.write('\n'.join(text) + '\n')
