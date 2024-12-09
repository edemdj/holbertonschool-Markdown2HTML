#!/usr/bin/python3
import os
import sys

def parse_markdown(markdown_file, output_file):
    """
    Parses the given Markdown file for headings and writes the HTML output.
    """
    try:
        with open(markdown_file, 'r') as md, open(output_file, 'w') as html:
            for line in md:
                line = line.strip()
                if line.startswith('#'):
                    # Count the number of leading '#' characters to determine heading level
                    level = len(line.split(' ')[0])
                    if 1 <= level <= 6:  # Valid heading levels are 1 to 6
                        content = line[level:].strip()
                        html.write(f"<h{level}>{content}</h{level}>\n")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get the input markdown file and output HTML file
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Process the Markdown file
    parse_markdown(markdown_file, output_file)

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
