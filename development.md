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
in several stages. These stages are controlled by a *build script*.

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
This is an action that can be done by means of the
[GitHub Desktop](https://desktop.github.com) application.

Now they can edit the `source` documents locally, with the text-edit applications
of their choice. That can be `Notepad` for absolute beginners, or `Vim` for absolute
experts, or
[Atom](https://atom.io)
for everybody else.

When they are done, they can push their modification to their online fork on GitHub.
This action can easily be performed with GitHub Desktop again.

When they want their changes to be published, they create a pull-request.
This can also be started from the GitHub Desktop app, which will lead you to the GitHub
website where you can fill in a new pull request.

Owners will be notified of the new pull request and can accept or reject it.

## Details of the workflow

Here we describe the steps in the publishing workflow in greater detail.

### Build script

The build script is a Python program [build.py](build.py),
documented in the published documentation itself:
[help](https://dans-labs.github.io/formats/help/).
If the documentation is not yet online, you can consult the markdown
source directly here: [help](https://github.com/Dans-labs/formats/blob/master/source/help.md).

### Requirements

In order to run the build script, you need the following Python modules:

```
pip3 install pyyaml mkdocs
```

### From `source` to `docs`

``` sh
python3 build.py make
```

The `make` step reads the files in directory `source` and produces resulting files
in directory `docs`.

It transforms markdown files into other markdown files, using
interlinking information and several other settings are stored
[data.yaml](https://github.com/Dans-labs/formats/blob/master/source/data.yaml).

It also generates a config file for `mkdocs` which takes care of the next step.
This generated
[mkdocs.yml](https://github.com/Dans-labs/formats/blob/master/mkdocs.yml)
is in the top level directory.
It is generated on the basis of
[mkdocsIn.yml](https://github.com/Dans-labs/formats/blob/master/source/mkdocsIn.yml)
and a list of urls in 
[urls.list](https://github.com/Dans-labs/formats/blob/master/source/urls.list).

The recommended practice is to never enter a url directly into the source files,
but define an abbreviation for it in `urls.list` and used the abbreviation
in the markdown wrapped in `{{ }}`.

The generation process makes a navigation structure based on the existing
documentation source files.

### From `docs` to `site`

``` sh
python3 build.py build
```

The step that generates HTML from markdown is the task of a *static page generator*.
[mkdocs](https://www.mkdocs.org) is such a program, written in Python.

It reads markdown files in the `docs` folder and produces HTML files
in the `site` folder. During the process it applies styles, headers, footers, and
it creates navigation links.

The fine details of the website layout is in the 
[mkdocs.yml](https://github.com/Dans-labs/formats/blob/master/mkdocs.yml)
which we have generated in the previous step.

### From `site` to the local browser

```
python3 build.py docs
```

This will display the website in `site` in your browser.

### From `site` to the published on GitHub

```
python3 build.py g "commit message"
```

Use this command to publish the website in `site` to GitHub pages.
Behind the screens, mkdocs will collect the contents of `site`, store it in a separate
branch call `gh-pages`, and push the `gh-pages` branch to GitHub.
From there, GitHub takes over, and will publish the contents it finds in `gh-pages`
to `https://Dans-labs.github.io/formats` where all eyes of the world can see it.

Here you can see how the repo has been
[set up for GitHub Pages](https://github.com/Dans-labs/formats/settings/pages).

This step will also commit the changes to GitHub.

## Work to do

In order to turn this pilot into a productive platform to collaborate on preferred formats documentation,
the following things might be needed in due course:

1.  **Allocate a person that is knowledgeable with Python and GitHub to take care of the workflow.**
    This person will play a role for all following steps.

1.  make sure that *build.py* gets triggered on GitHub whenever a pull request gets accepted

1.  **write instructions for collaborators:**
    *   point to an easy
        [markdown guide](https://www.markdownguide.org/basic-syntax)
    *   point to GitHub Desktop and Atom
    *   explain the modification process by means of commits and pull requests
    *   explain how to file Issues
    *   explain what the true source files are and what the generated files are,
        so that people do not modify generated files and see their modifications getting lost
        the next time the build process is run

1.  **Extend the data model / adapt the conventions:**
    So far, all texts have been written from the DANS perspective.
    You might want to make distinctions between recommendations over the participating institutions.
    You have to think about how to organize that.
    Maybe you need another folder `institutes` below which they specify their particular recommendations
    per file type.

1.  **Rebrand the published content:**
    Currently, the published GitHub Pages are in a neutral *readthedocs* style.
    You might want to develop a more DANS-specific template.
    I have done something already, see
    [mkdocs-dans])https://github.com/Dans-labs/mkdocs-dans) but this no longer works.
    However, a better thing to do might be the following:

1.  **Build other publication channels:**
    Instead of (only) publishing content via GitHub pages, you might want to
    build other channels for other avenues.
    This is something that other institutes could do for themselves, or we could provide middleware
    to do that: a program that reads the source files, that can be fed with institute-specific settings
    and logos, and that will produce a set of custom static pages ready to be included by an
    institutional web site.

1.  **Modify the collaboration workflow:**
    If the GitHub workflow of committing changes and creating/accepting pull-requests
    turns out to be too cumbersome for the target audience, you could consider to use Google docs
    for direct collaboration on texts, and only when agreement is reached there,
    to pull content from there and ingest it in this same GitHub repo.
    Owners will then push the changes and trigger the build script.
    Collaborators do not have to be aware of GitHub.
    You still have a lot of change history in your GitHub repository, and you still benefit
    from various benefits of GitHub, such as easy transfer of releases to Zenodo and archiving
    by the [Software Heritage Archive](https://www.softwareheritage.org).






