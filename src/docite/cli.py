"""
References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys

from docite import __version__, convert

__author__ = "danibene"
__copyright__ = "danibene"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--version",
        action="version",
        version=f"docite {__version__}",
    )
    parser.add_argument(
        "--inputfile",
        type=str,
        required=True,
        help="Input markdown file",
    )
    parser.add_argument(
        "--outputfile",
        type=str,
        required=True,
        help="Output markdown file",
    )
    parser.add_argument(
        "--bibfile",
        type=str,
        required=True,
        help="BibTeX file",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """
    Wrapper allowing :func:`convert_with_refs` to be called with string arguments in
    a CLI fashion.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--inputfile", "input.md"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Converting...")
    print("Input file: ", args.inputfile)
    print("Output file: ", args.outputfile)
    print("Bib file: ", args.bibfile)
    convert.convert_with_refs(args.inputfile, args.outputfile, args.bibfile)
    _logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m docite.cli --help
    #
    run()
