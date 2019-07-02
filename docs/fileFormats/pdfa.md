

# PDF/A

**Portable Document Format (for Archiving)**

???+ abstract "In short"
    Stricter form of [PDF](../fileFormats/pdf.md) which is guaranteed to be self-contained.

item | info
--- | ---
types | [Image](../dataTypes/image.md), [Text (formatted)](../dataTypes/textFormatted.md)
preferred | ✅ yes
extensions | [`.pdf`](../extensions/pdf.md)
related formats | [DOC](../fileFormats/doc.md), [DOCX](../fileFormats/docx.md), [GIF](../fileFormats/gif.md), [JPEG](../fileFormats/jpeg.md), [ODT](../fileFormats/odt.md), [PDF](../fileFormats/pdf.md), [PNG](../fileFormats/png.md), [PostScript](../fileFormats/postscript.md), [SVG](../fileFormats/svg.md), [TIFF](../fileFormats/tiff.md)
wikipedia | [`PDF/A`]({{wikipedia}}/PDF/A)

## Description

[PDF](../fileFormats/pdf.md)
has been developed by software maker Adobe to represent printed documents
faithfully and consistently independent of the computer and platform 
where it is displayed.

It has a subtype called
PDF/A
which is specifically designed for long-term sustainability.
PDF/A is the international standard for [Text (formatted)](../dataTypes/textFormatted.md)
documents. A PDF/A file is a stand-alone document: all fonts and images are
included in the file, so it is not dependent on other files on the computer to
correctly display its content.
No part of the contents of a PDF/A file is encrypted.

There are several types of PDF/A. PDF/A-1a is recommended for text documents
that were created entirely on a computer (“born digital”). For digitized
documents PDF/A-1b is a suitable format.

### Software

???+ abstract "Viewers"
    [PDF](../fileFormats/pdf.md) viewers are pretty much part of the operating system nowadays, but if not,
    the Adobe Reader can be downloaded for free.

??? abstract "Generators"
    Facilities to create [PDF](../fileFormats/pdf.md) are near universal, because either the operating system
    or many applications let you "print" files as [PDF](../fileFormats/pdf.md).
    For example, Microsoft Word. Excel, and Powerpoint let you export documents
    as [PDF](../fileFormats/pdf.md), and so do the open source office suites such as
    [LibreOffice]({{libreoffice}})
    and the 
    Mac programs Pages, Numbers and KeyNote.

    It is also possible to generate [PDF](../fileFormats/pdf.md) as output from programs, there are
    good libraries to create custom PDFs.

    Users of [TeX](../fileFormats/tex.md) have especially sophisticated tools to create virtually any
    [PDF](../fileFormats/pdf.md) they want.

    For Windows there is afree application that can “print” documents to a [PDF](../fileFormats/pdf.md):
    [Bullzip PDF Printer]({{bullzip}}).

??? abstract "Editors"
    Modifying [PDF](../fileFormats/pdf.md) files is less well supported by free programs, although
    marking up PDFs with annotations is getting mainstream.

    Of course,
    [Adobe]({{adobe}})
    sells quite capable software for creating and modifying [PDF](../fileFormats/pdf.md) files.

??? abstract "Converters"
    [PDF](../fileFormats/pdf.md) can be used to represent images. Conversions between more common [Image](../dataTypes/image.md)
    formats and [PDF](../fileFormats/pdf.md) can be performed with programs such as
    [ImageMagick]({{imagemagick}})
    and on Windows:
    [IrfanView]({{irfanview}}).



## See also
*   [`{{pdfa}}`]({{pdfa}})



