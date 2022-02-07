# Overview

## What is it?

This repository consists of source documents in
[markdown](https://www.markdownguide.org/basic-syntax)
that can be published to GitHub pages.
It contains a build script in Python, to transform the source documents
into published documents.

The source documents are all about file formats, and the data types involved, and the
file extensions involved.

This is a big nest of interlinked information, and one of the tasks of the build script
is to provide links between related pages wherever relevant.

## How does it work?

The source documents in markdown are transformed to HTML pages for a static website
in several stages. These stages are controlled by a
build script [build.py](build.py), documented in
[help](https://dans-labs.github.io/formats/help/).
If the documentation is not yet online, you can consult the markdown
source of the [help](https://github.com/Dans-labs/formats/blob/master/source/help.md).

## Requirements

In order to run the build script, you need the following Python modules:

```
pip3 install pyyaml mkdocs
```

In order to use GitHub, you either need the command line tool `git` or
the application [GitHub Desktop](https://desktop.github.com).

## Intended workflow

The users are divided into owners, contributors and readers.

Readers consult the end-product by browsing:
[documentation pages](https://dans-labs.github.io/formats/).

Contributors propose changes to the source documents by creating pull-requests.

Owners accept or reject pull requests.
When pull-requests are accepted, they re-build the documentation.

**N.B.** Eventually the building of the documentation should be automatically
triggered upon accepting a pull-request.

### More about pull-requests

Contributors should first *fork* the repo to their own space on GitHub.
This is an online action, done on the GitHub website.

Then they should clone their fork to their own computer.
This is an action that can be done by means of the GitHub Desktop app.

Now they can edit the `source` documents locally, with the text-edit applications
of their choice. That can be `Notepad` for absolute beginners, or `Vim` for absolute
experts, or
[Atom](https://atom.io)
for everybody else.

When they are done, they can push their modification to their online fork on GitHub.
This action can easily be performed with GitHub Desktop again.

When they want their changes to be published, they create a pull-request.

### From `source` to `docs`

The `make` step reads the files in directory `source` and produces resulting files
in directory `docs`.

It transforms markdown files into other markdown files, using
interlinking information and several other settings are stored
[data.yaml](https://github.com/Dans-labs/formats/blob/master/source/data.yaml).

It also generates a config file for `mkdocs` which takes care of the next step.

The fine details of the website layout is in a configuration file read by 
[mkdocs](https://www.mkdocs.org)




