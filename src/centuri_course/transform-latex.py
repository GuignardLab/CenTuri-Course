#!python
import argparse
import re
from pathlib import Path

double_dollars = re.compile(r"\$\$[^$]*\$\$")
simple_dollar = re.compile(r"\$[^$]*\$")


def rewrite(text):
    found = double_dollars.search(text)
    while found:
        sub = text[found.start() + 2 : found.end() - 2]
        sub = sub.strip().replace("+", "+")
        text = (
            text[: found.start()]
            + f'<img src="https://render.githubusercontent.com/render/math?math={sub}">\n\n'
            + text[found.end() :]
        )
        found = double_dollars.search(text)

    found = simple_dollar.search(text)
    while found:
        sub = text[found.start() + 1 : found.end() - 1]
        sub = sub.strip().replace("+", "+")
        text = (
            text[: found.start()]
            + f'<img src="https://render.githubusercontent.com/render/math?math={sub}">'
            + text[found.end() :]
        )
        found = simple_dollar.search(text)
    return text


def parse_files(path, file_type="md"):
    if path.is_dir():
        files = path.glob(f"*.{file_type}")
    else:
        files = [path]
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Replace LaTeX expressions (bounded by '$' and '$$')"
            "in all markdown files of a given folder."
        )
    )
    parser.add_argument(
        "-p",
        "--path",
        dest="p",
        type=str,
        required=True,
        help="Path to the folder containing the markdown files, or a markdown itself",
    )
    parser.add_argument(
        "-s",
        "--suffix",
        dest="s",
        type=str,
        default="",
        help="Suffix to add at the end of the name of the modified file.\n If not provided, the files will be modified in place",
    )
    parser.add_argument(
        "-t",
        "--type",
        dest="t",
        type=str,
        default="md",
        choices=["md", "ipynb", "nb"],
        help="Whether to process markdown files directly (option 'md') or notebooks (options 'ipynb' or 'nb')",
    )
    args = parser.parse_args()
    p = Path(args.p)
    if args.t == "nb":
        args.t = "ipynb"
    files = parse_files(p, args.t)
    for file in files:
        if args.t == "ipynb":
            from jupytext import jupytext

            text = jupytext.read(file)
            text = jupytext.notebook_to_md(text)
        else:
            with open(file) as f:
                text = f.read()
        text = rewrite(text)
        if args.s != "" and args.s[0] != ".":
            args.s = "." + args.s
        with open(file.with_suffix(f"{args.s}.md"), "w") as f:
            f.write(text)
