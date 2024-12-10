#!/usr/bin/python3
import os
import sys

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

    # If everything is fine, exit with 0 (no output)
    sys.exit(0)

if __name__ == "__main__":
    main()
