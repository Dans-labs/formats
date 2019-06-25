# Formatted text

## Description

Text is a broad category of data.
For some, text is something that you type with Microsoft Word,
for others it is what they read in a PDF, and for yet others it is the
program code they hack in a text editor.

For the purposes of archiving we divide the text data type in 
**formatted text** and [plain text](plainText.md).

Formatted text consists of text strings with layout information.
A formatted text does not only display the bare text material, but it formats
the texts by arranging it in pages and columns, by applying fonts in different
colors, sizes, weights and shapes, and combining it with various graphical
objects such as images.

Formatted text can get very complex.

## Representations

Common representations for formatted text are:

*   [PDF(/A)](../fileTypes/pdfa.md):
    developed by Adobe, now standardized, deals with the most complex material
    that is printable, takes care of font and other graphics inclusions, makes
    text searchable. Looks perfect from the outside, may look horrible from the
    inside
*   [HTML](../fileTypes/html.md):
    universal language of the Web, deals with very rich layout, comparable to
    PDF, works together with [CSS](../fileTypes/css.md) to achieve subtle
    results. Looks perfect from the outside, may look horribe from the inside
*   [Markdown](../fileTypes/markdown.md):
    upcoming text language of the web, geared to plain text, but with basic
    formatting capabilities from HTML. Looks nice from the outside, looks good
    from the inside. This documentation is written in Markdown
*   [TeX](../fileTypes/tex.md):
    source code for ancient text processor TeX (1987), the first one that could
    deliver scientific and mathematical documents with professional typesetting
    quality. TeX is still a de facto standard for writing scientific papers, not
    only in the exact sciences, but also in various branches of the humanities

## See also

[Data container](data.md), [Plain text](plainText.md).


