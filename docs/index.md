![img](images/formats.png){: width="100" align="right"}
![img](images/DANS.png){: width="200" align="right"}

---

**this documentation is under development**

[current docs]({{preferredFormats}})

---


# About

[DANS]({{dans}}) is developing normative guidelines about data and file types
for the purpose of long-term archiving in its self-service repository
  [EASY]({{easy}}).

# Disclaimer

All texts you find here are work in progress.  The currently authoritative texts
can be found on the [prefered formats]({{preferredFormats}}) web page of DANS.

# Purpose

The purpose of this repository is to open up the discussion of which formats are
preferred and which are not.

There are two important kinds of criteria for a format to be preferred:

*   is it technically suitable for long-term preservation?  I.e. will it still
    be usable and/or understandable if most software that we have now is out of
    business? 
*   is it practically usable by depositors and other users of the archive?  We
    do not want to introduce unnecessary hurdles for researchers that submit
      their data to us.

Archiving for research is always unfinished business.  Formats evolve, and new
formats emerge.  Here at DANS we do not pretend to know all formats and we are
open to learn about new ones.

# Getting started

If you have comments on our current preferred format specifications, or if you
want to introduce new formats, you can start by filing an issue.

Please, browse through the
[list of issues]({{issues}})
first in order to see if
your topic is already being dealt with.

# Overview

Use the navigation to browse data types or file formats.

Or, if you browsing the raw files,
[dataTypes]({{formats}}/tree/master/docs/dataTypes/)
contains a collection of data types
and
[fileFormats]({{formats}}/tree/master/docs/fileFormats/)
contains a collection of file formats.
and
[extensions]({{formats}}/tree/master/docs/extensions/)
contains a collection of file extensions.


A *data type* is a way of organizing raw data for specific modelling applications
such as image, sound, text, structured data, etc. 

A file format is a way to serialize the data of a specific data type to a file
such as *pdf*, *xlsx*, *siard*, etc.

Applications that deal with that data are programmed in such a way that they can
read one or more file formats for that type.

When data is written to file in a specific file format, the file name often gets
an extension that indicates that file format
such as `.pdf`, `.xslx`, etc.

There are usually several file formats associated with one data type.

## Building this site

This site is built from source texts and structure information
into a set of Markdown files that is processed by MkDocs into
HTML files that can be served by GitHub Pages.

See the [help](help.md).

# Contact

[Dirk Roorda]({{author}})


---

Preferred Formats Documention **(under development)**

---

[Current documentation]({{preferredFormats}})

[Data Archiving and Networked Services (DANS)]({{dans}})

![img](images/formats.png){: width="100" align="right"}
![img](images/DANS.png){: width="200" align="right"}
