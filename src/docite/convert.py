import re
from pathlib import Path
from typing import Optional, Union

import pypandoc

from .utils import download_pandoc, get_path_to_assets


def substitute_label_refs(
    inputfile: Union[str, Path], outputfile: Optional[Union[str, Path]] = None
):
    """Substitute label references in a markdown file

    Args:
        inputfile (Union[str, Path]): input markdown file
        outputfile (Union[str, Path]): output markdown file.
            If None, the input file is overwritten.

    Returns:
        None
    """
    if outputfile is None:
        outputfile = inputfile

    with open(inputfile, "r", encoding="utf-8") as f:
        text = f.read()
        text = re.sub(r"\[\/\/\]: # \(ref-([^\)]+)\)", r"[\1](#\1)", text)
    with open(outputfile, "w") as f:
        f.write(text)


def remove_citation_metadata(
    inputfile: Union[str, Path], outputfile: Optional[Union[str, Path]] = None
):
    """Remove citation metadata from a markdown file

    Args:
        inputfile (Union[str, Path]): input markdown file
        outputfile (Union[str, Path]): output markdown file.
            If None, the input file is overwritten.

    Returns:
        None
    """
    if outputfile is None:
        outputfile = inputfile

    lines = []
    with open(inputfile, "r") as f:
        lines = f.readlines()

    with open(outputfile, "w") as f:
        for line_index, line in enumerate(lines):
            write = True
            if line.strip().startswith(("bibliography:", "csl:", "link-citations:")):
                write = False
            if line_index in [0, 4] and line.strip() == "---":
                write = False
            if write:
                f.write(line)


def convert_with_refs(
    inputfile: Union[str, Path],
    outputfile: Union[str, Path],
    bibfile: Union[str, Path],
    style: str = "ieee",
):
    """Convert a markdown file to a PDF with references

    Args:
        inputfile (Union[str, Path]): input markdown file
        outputfile (Union[str, Path]): output PDF file
        bibfile (Union[str, Path]): bibliography file
        style (str): bibliography style

    Returns:
        None
    """

    if style == "ieee":
        style = get_path_to_assets() / "ieee.csl"

    download_pandoc()
    pypandoc.convert_file(
        str(inputfile),
        "gfm",
        outputfile=str(outputfile),
        extra_args=[
            "-s",
            "--bibliography",
            str(bibfile),
            "--citeproc",
            "--csl",
            str(style),
            "--metadata",
            "link-citations=true",
        ],
    )
    substitute_label_refs(outputfile)
    remove_citation_metadata(outputfile)
