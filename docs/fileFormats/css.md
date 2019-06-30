[go to current production version]({{preferredFormats}})

---



# CSS

**Cascading Stylesheet**

???+ abstract "In short"
    Declarative styles for the Web.

item | info
--- | ---
types | [Markup](../dataTypes/markup.md), [Text (plain)](../dataTypes/textPlain.md)
preferred | ⚠️ under conditions
extensions | [`.css`](../extensions/css.md)
related formats | [CSV](../fileFormats/csv.md), [HTML](../fileFormats/html.md), [HTML](../fileFormats/html.md), [JavaScript](../fileFormats/javascript.md), [JSON](../fileFormats/json.md), [JSX](../fileFormats/jsx.md), [Markdown](../fileFormats/markdown.md), [Markdown](../fileFormats/markdown.md), [SGML](../fileFormats/sgml.md), [SQL](../fileFormats/sql.md), [TeX](../fileFormats/tex.md), [TeX](../fileFormats/tex.md), [Text](../fileFormats/text.md), [XHTML](../fileFormats/xhtml.md), [XML](../fileFormats/xml.md), [XML](../fileFormats/xml.md), [XSLT](../fileFormats/xslt.md), [YAML](../fileFormats/yaml.md)
wikipedia | [`Cascading_Style_Sheets`]({{wikipedia}}/Cascading_Style_Sheets)

## Description

[Cascading Style Sheets]({{wikipedia}}/Cascading_Style_Sheets)
is a language for styling
[HTML](../fileFormats/html.md) documents.
It is widely used on the web.

[HTML](../fileFormats/html.md) files may contain CSS styles inside, or they may refer to other files for
their styling.

## Complications

The World-wide-web is one of the most dynamic corners of IT. Standards are
always on the move, and new patterns of organizing web content replace the best
practices of yesterday.

CSS has gone through several major versions.

The format is [Text](../fileFormats/text.md), so CSS files are easy to open,
but the meaning of the styles is dependent on the version of the
CSS styling engine that has been used.

Moreover, in real-world web applications, CSS files are often
deliberately `uglified`, in order to decrease their file size.

## Recommendations

For archiving it must be made clear to which files the CSS files refer and which
version of CSS is being used. As browser-specific extensions may exist, the
target environment of the files must be known, unless only basic elements have
been used. If the CSS files contain links to other CSS files or external files,
these links must be working.

If the CSS files have been uglified, their non-uglified sources should be archived as well.



## See also
*   [`{{css}}`]({{css}})
*   [`{{cssmdn}}`]({{cssmdn}})




---

[go to current production version]({{preferredFormats}})
