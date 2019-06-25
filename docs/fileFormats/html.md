# HTML

## Extensions

`.html`, `.htm`

## Data types

[text (formatted)](../dataTypes/formattedText.md)

## Preferred status

Yes, but ...

## Description

[HTML]({{wikipedia}}/HTML)
is *the* core web technology, turning the pre-www internet of 1991 into a World Wide Web.

It is basically a document markup language, in which you can store
text plus formatting plus layout.

In earlier times, the layout and format options were basic,
nowadays both are as sophisticated as the printed page can be.

In order to achieve the richest formatting, HTML works together with another
standard for *styles*.
[CSS]({{wikipedia}}/Cascading_Style_Sheets).

What sets HTML apart from printed work is dynamics: users can *interact* with a
web page, and defining this interaction is delegated to yet another technology,
[JavaScript](), which is a programming language.

The ultimate reference to all these technologies is the
[Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/):

*   [HTML]({{mozilla}}/docs/Web/HTML)
*   [CSS]({{mozilla}}/docs/Web/CSS)
*   [Javascript]({{mozilla}}/docs/Web/JavaScript)

HTML files may contain CSS styles inside, or they may refer to other files for
their styling.

Likewise, they may contain Javascript inside, or they may refer to other files
for their scripting.

## Complications

The World-wide-web is one of the most dynamic corners of IT. Standards are
always on the move, and new patterns of organizing web content replace the best
practices of yesterday.

HTML files may contain complete programs, documentation, and installation
procedures on the one hand, or they may consist of long stretches of text with
horribly redundant layout codes.

Most HTML in the world has not been typed by humans, but has been generated by
software.

HTML files can be almost one liners that call a big Javascript program that does
all the rest, or it may contain everything inside.

## HTML in the archive

One scenario by which HTML files may enter the archive, is when a website gets
archived. In that case, it is not the individual HTML files themselves that
should be judged for their long-term preservability, but rather the website as
an integral system.

In this scenario, it is preferable to archive the source code of the web site as
well, not only the end result.

Nowadays, there are many popular ways to write HTML documentation as generated
static pages. The source code resides in a software repository, and the
generated pages are served by a service such as <readthedocs.org> or GitHub
pages.

Another scenario is when HTML files with substantial content have been captured
from a legacy system, or from other sources.
If possible, scan the file for references to external files, and if possible,
rescue those files as well, and store them in an organization that matches
the way they are referenced. Then preserve the resulting directory in a
[tar](tar.md) file.

## See also

[text (plain)](../dataTypes/plainText.md)