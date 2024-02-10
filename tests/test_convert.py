import shutil
import tempfile
from pathlib import Path
from typing import Generator

import pytest

# Import the functions you want to test
from docite.convert import convert_with_refs, substitute_label_refs
from docite.utils import get_path_to_assets


# Define a fixture to create a temporary directory for testing
@pytest.fixture
def temp_dir() -> Generator:
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)


# Define a fixture to create a temporary BibTeX file
@pytest.fixture
def temp_bib_file(temp_dir: Path) -> Path:
    bib_file = temp_dir / "test.bib"
    with open(bib_file, "w") as f:
        f.write(
            """@article{example,
  author = "John Doe",
  title = "Example Title",
  year = 2023
}"""
        )
    return bib_file


# Define test cases for 'substitute_label_refs' function
def test_substitute_label_refs(temp_dir: Path) -> None:
    input_file = temp_dir / "input.md"
    output_file = temp_dir / "output.md"

    # Create a sample input markdown file with label references
    with open(input_file, "w") as f:
        f.write("[//]: # (ref-example)\nThis is a reference to [example].")

    substitute_label_refs(input_file, output_file)

    # Read the output file and check if the references are substituted correctly
    with open(output_file, "r") as f:
        text = f.read()
        assert text == "[example](#example)\nThis is a reference to [example]."


# Define test cases for 'convert_with_refs' function
def test_convert_with_refs(temp_dir: Path, temp_bib_file: Path) -> None:
    input_file = temp_dir / "input.md"
    output_file = temp_dir / "output.md"
    bib_file = temp_bib_file
    # Create a sample input markdown file
    with open(input_file, "w") as f:
        f.write("This is a sample markdown file @example.")

    convert_with_refs(input_file, output_file, bib_file)

    assert output_file.is_file()
    # Read the output file and check if the references are substituted correctly
    with open(output_file, "r") as f:
        text = f.read()
        assert "J. Doe, “Example title,”" in text


def test_convert_with_refs_apa_csl(temp_dir: Path, temp_bib_file: Path) -> None:
    input_file = temp_dir / "input.md"
    output_file = temp_dir / "output.md"
    bib_file = temp_bib_file
    csl_file = get_path_to_assets() / "apa.csl"
    # Create a sample input markdown file
    with open(input_file, "w") as f:
        f.write("This is a sample markdown file [@example].")

    convert_with_refs(input_file, output_file, bib_file, csl_file)

    assert output_file.is_file()
    # Read the output file and check if the references are substituted correctly
    with open(output_file, "r") as f:
        text = f.read()
        assert "Doe, J. (2023). *Example title*." in text


# Run the tests
if __name__ == "__main__":
    pytest.main()
