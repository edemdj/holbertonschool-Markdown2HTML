#!/usr/bin/python3
"""Markdown to HTML converter."""

import sys
import os

def markdown_to_html(input_file, output_file):
    """
    Convert Markdown headings to HTML.
    """
    html_content = ""

    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            for line in md_file:
                line = line.strip()  
                if line.startswith('#'):  
                    
                    heading_level = len(line.split(' ')[0])
                    if 1 <= heading_level <= 6:  
                        
                        heading_text = line[heading_level:].strip()
                        html_content += f"<h{heading_level}>{heading_text}</h{heading_level}>\n"

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    
    markdown_to_html(input_file, output_file)
    sys.exit(0)
