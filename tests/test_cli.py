from pathlib import Path

from docite.cli import main
from docite.utils import get_path_to_assets

__author__ = "danibene"
__copyright__ = "danibene"
__license__ = "MIT"


def test_main(tmp_path_factory):
    """CLI Tests"""
    inputfile = str(get_path_to_assets() / "example_inputfile.md")
    # Load content of inputfile
    with open(inputfile, "r") as f:
        inputfile_content = f.read()
    bibfile = str(get_path_to_assets() / "example_bibfile.bib")
    outputfile_parent_dir = tmp_path_factory.mktemp("outputfile")
    outputfile = str(outputfile_parent_dir / "outputfile.md")
    main(["--inputfile", inputfile, "--outputfile", outputfile, "--bibfile", bibfile])
    assert Path(outputfile).is_file()
    # Check that the input file has not been modified
    with open(inputfile, "r") as f:
        assert f.read() == inputfile_content
    # Check that the output file is not identical to the input file
    with open(outputfile, "r") as f:
        assert f.read() != inputfile_content
    # Check that the output file contains the expected content
    with open(outputfile, "r") as f:
        assert "https://doi.org" in f.read()


def test_main_custom_csl(tmp_path_factory: TempPathFactory) -> None:
    """CLI Tests"""
    inputfile = str(get_path_to_assets() / "example_inputfile.md")
    # Load content of inputfile
    with open(inputfile, "r") as f:
        inputfile_content = f.read()
    bibfile = str(get_path_to_assets() / "example_bibfile.bib")
    cslfile = str(get_path_to_assets() / "apa.csl")
    outputfile_parent_dir = tmp_path_factory.mktemp("outputfile")
    outputfile = str(outputfile_parent_dir / "outputfile.md")
    main(
        [
            "--inputfile",
            inputfile,
            "--outputfile",
            outputfile,
            "--bibfile",
            bibfile,
            "--stylefile",
            cslfile,
        ]
    )
    assert Path(outputfile).is_file()
    # Check that the input file has not been modified
    with open(inputfile, "r") as f:
        assert f.read() == inputfile_content
    # Check that the output file is not identical to the input file
    with open(outputfile, "r") as f:
        assert f.read() != inputfile_content
    # Check that the output file contains the expected content
    with open(outputfile, "r") as f:
        assert "*Journal of Open" in f.read()
