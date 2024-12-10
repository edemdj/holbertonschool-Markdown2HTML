#!/usr/bin/python3
""" markdown to html """

if __name__ == "__main__":

    import sys
    import os.path

    if len(sys.argv) < 3:
        sys.exit("Usage: ./markdown2html.py README.md README.html")
    elif (not os.path.isfile(sys.argv[1]) or not os.path.exists(sys.argv[1])):
        sys.exit("Missing {}".format(sys.argv[1]))
    else:
        text = ""
        with open(sys.argv[1], encoding='utf-8') as md_file:
            for line in md_file:
                if line.split(' ')[0][0] == '#':
                    length = len(line.split(' ')[0])
                    heading = " ".join(line.split(' ')[1:-1]) +\
                        line.split(' ')[-1][:-1]
                    text += "<h{}>{}</h{}>\n".format(length, heading, length)
        with open(sys.argv[2], 'w', encoding='utf-8') as html_file:
            html_file.write(text)