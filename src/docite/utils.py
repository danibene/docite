from importlib import resources
from pathlib import Path

import pypandoc

import docite


def download_pandoc() -> None:
    """Download pandoc if not already installed

    Returns:
      None
    """
    # Check if pandoc is installed
    try:
        pypandoc.get_pandoc_version()
    except OSError:
        # Download and install pandoc
        pypandoc.download_pandoc()


def get_path_to_assets() -> Path:
    """Get the path to the assets directory

    Returns:
      Path: path to the assets directory
    """
    return Path(resources.files(docite) / "assets")
