from pathlib import Path
import argparse
import re

regexp_1 = re.compile('\$\$[^$]*\$\$')
regexp_2 = re.compile('\$[^$]*\$')


def rewrite(text):
    found = regexp_1.search(text)
    while found:
        sub = text[found.start()+2:found.end()-2]
        sub = sub.strip().replace('+', '%2B ')
        text = (text[:found.start()] +
                f'<img src="https://render.githubusercontent.com/render/math?math={sub}">\n' +
                text[found.end():])
        found = regexp_1.search(text)
    
    found = regexp_2.search(text)
    while found:
        sub = text[found.start()+1:found.end()-1]
        sub = sub.strip().replace('+', '%2B ')
        text = (text[:found.start()] +
                f'<img src="https://render.githubusercontent.com/render/math?math={sub}">' +
                text[found.end():])
        found = regexp_2.search(text)    
    return text
    

def parse_files(path):
    if path.is_dir():
        files = path.glob('*.md')
    else:
        files = [path]
    return files

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=('Replace LaTeX expressions (bounded by \'$\')'
                                                  'in all markdown files of a given folder.'))
    parser.add_argument('-p', '--path', dest='p', default='.', type=str,
                        help='Path to the folder containing the markdown files, or a markdown itself')
    args = parser.parse_args(['-p', '.'])
    p = Path(args.p)
    files = parse_files(p)
    for file in files:
        with open(file, 'r') as f:
            text = f.read()
        text = rewrite(text)
        with open(file, 'w') as f:
            f.write(text)