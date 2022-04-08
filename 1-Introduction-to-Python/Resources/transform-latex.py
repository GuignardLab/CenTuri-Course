#!python

from pathlib import Path
import argparse
import re

double_dollars = re.compile('\$\$[^$]*\$\$')
simple_dollar = re.compile('\$[^$]*\$')


def rewrite(text):
    found = double_dollars.search(text)
    while found:
        sub = text[found.start()+2:found.end()-2]
        sub = sub.strip().replace('+', '%2B ')
        text = (text[:found.start()] +
                f'<img src="https://render.githubusercontent.com/render/math?math={sub}">\n\n' +
                text[found.end():])
        found = double_dollars.search(text)
    
    found = simple_dollar.search(text)
    while found:
        sub = text[found.start()+1:found.end()-1]
        sub = sub.strip().replace('+', '%2B ')
        text = (text[:found.start()] +
                f'<img src="https://render.githubusercontent.com/render/math?math={sub}">' +
                text[found.end():])
        found = simple_dollar.search(text)    
    return text
    

def parse_files(path):
    if path.is_dir():
        files = path.glob('*.md')
    else:
        files = [path]
    return files

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=('Replace LaTeX expressions (bounded by \'$\' and \'$$\')'
                                                  'in all markdown files of a given folder.'))
    parser.add_argument('-p', '--path', dest='p', type=str, required=True,
                        help='Path to the folder containing the markdown files, or a markdown itself')
    parser.add_argument('-s', '--suffix', dest='s', type=str, default='',
                        help='Suffix to add at the end of the name of the modified file.\n If not provided, the files will be modified in place')
    args = parser.parse_args()
    p = Path(args.p)
    files = parse_files(p)
    for file in files:
        with open(file, 'r') as f:
            text = f.read()
        text = rewrite(text)
        with open(file, 'w') as f:
            f.write(text)