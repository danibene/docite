.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/docite.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/docite
    .. image:: https://img.shields.io/conda/vn/conda-forge/docite.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/docite
    .. image:: https://pepy.tech/badge/docite/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/docite
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/docite

.. image:: https://readthedocs.org/projects/docite/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://docite.readthedocs.io/en/stable/

.. image:: https://img.shields.io/pypi/v/docite.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/docite/

.. image:: https://img.shields.io/coveralls/github/danibene/docite/main.svg
    :alt: Coveralls
    :target: https://coveralls.io/r/danibene/docite

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

======
docite
======


    Some tools to format references in documentation

This is a small package I created to help me format references in my documentation.
It uses pandoc to convert the references from bibtex to a format that can be used
in markdown files.

Installation
================
You can install the package via pip::

    pip install docite

Usage
================
You can use the package from the command line as follows::

    docite --inputfile <INPUTFILE> --outputfile <OUTPUTFILE> --bibfile <BIFILE>

or::

    python -m docite.cli --inputfile <INPUTFILE> --outputfile <OUTPUTFILE> --bibfile <BIFILE>

You can also use the package from python as follows::

        from docite import convert
        convert.convert_with_refs(inputfile, outputfile, bibfile)

My personal workflow is:

- I use Zotero to manage my references and then export them to a Better Bibtex file.
- I use the Citation Picker for Zotero extension within VSCode to add the references to my markdown files.
- I use docite to generate an output markdown file with the references formatted.

Here is a gif showing how I use the package:

.. image:: https://github.com/danibene/docite/blob/assets/usage_2024-02-10.gif
    :alt: Usage
    :align: center

Customize
================
By default, the package will use the IEEE citation style. You can change the citation style by using the `--stylefile` option, e.g., to change the citation style to APA you can use the following command::

    docite --inputfile <INPUTFILE> --outputfile <OUTPUTFILE> --bibfile <BIFILE> --stylefile path/to/downloaded/apa.csl

You can find citation style language files in the `citation-style-language repository`_.

.. _citation-style-language repository: https://github.com/citation-style-language/styles


.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

    pip install pre-commit
    cd docite
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate

Don't forget to tell your contributors to also install and use pre-commit.

.. _pre-commit: https://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
