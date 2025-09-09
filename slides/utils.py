#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "click",
# ]
# ///
from pathlib import Path
import shutil
import subprocess
import click


@click.group()
def slides():
    pass


@slides.command()
@click.argument("dest")
@click.option(
    "-t", "--template-dir", help="Template directory", type=click.Path(dir_okay=True)
)
@click.option("--overwrite", is_flag=True, default=False)
def create(dest: str, template_dir: str, overwrite: bool) -> None:
    """
    Create a new slide directory.
    """
    dest = Path(dest)
    template_dir = Path(template_dir)

    if dest.exists() and not overwrite:
        raise click.BadArgumentUsage(f"Unable to overwrite {dest}")

    fname = dest.stem + ".md"

    Path.mkdir(dest)
    shutil.copyfile(template_dir / "slides.md", dest / fname)


@slides.command()
@click.option("-s", "--source", help="Source file", type=click.Path(file_okay=True, exists=True))
@click.option(
    "-t", "--template-dir", help="Template directory", type=click.Path(dir_okay=True, exists=True)
)
@click.option("--overwrite", is_flag=True, default=False)
@click.option("-o", "--output", type=click.Path(dir_okay=False, writable=True))
def generate(source: str, template_dir: str, overwrite: bool, output: str) -> None:
    """
    Generate html slides from a markdown source
    """

    source = Path(source)
    template_dir = Path(template_dir)

    if not output:
        p = source.parent
        output = p / f"{source.stem}.html"

    template = template_dir / "template.md"
    lua_filter = template_dir / "revealjs-codeblock.lua"

    if not source.exists():
        raise click.ClickException(f"Can't find the source file: {source}")

    if output.exists() and not overwrite:
        raise click.ClickException(f"Unable to overwrite {output}")

    cmd = f"pandoc -t revealjs -s --slide-level=0 -L {lua_filter} --template {template} -o {output} {source}"

    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    slides()
