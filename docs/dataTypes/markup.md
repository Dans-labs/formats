

# Markup

**Plain text with layout and formatting**

???+ abstract "In short"
    Special syntax separates content from markup.

item | info
--- | ---
formats | [CSS](../fileFormats/css.md), [HTML](../fileFormats/html.md), [JavaScript](../fileFormats/javascript.md), [JSX](../fileFormats/jsx.md), [Markdown](../fileFormats/markdown.md), [SGML](../fileFormats/sgml.md), [TeX](../fileFormats/tex.md), [XHTML](../fileFormats/xhtml.md), [XML](../fileFormats/xml.md), [XSLT](../fileFormats/xslt.md)
extensions | [`css`](../extensions/css.md), [`es`](../extensions/es.md), [`htm`](../extensions/htm.md), [`html`](../extensions/html.md), [`js`](../extensions/js.md), [`jsx`](../extensions/jsx.md), [`md`](../extensions/md.md), [`sty`](../extensions/sty.md), [`tex`](../extensions/tex.md), [`xml`](../extensions/xml.md), [`xsl`](../extensions/xsl.md), [`xslt`](../extensions/xslt.md)
related types | [Data (container)](../dataTypes/dataContainer.md), [Text (formatted)](../dataTypes/textFormatted.md), [Text (plain)](../dataTypes/textPlain.md)

## Description

Markup is a mechanism to annotate content with layout, formatting, and
additional semantics.

### SGML, HTML, XML, and XHTML 

XML, HTML and SGML are common and suitable markup language formats, provided the
file formats are valid and complete (see paragraph below). Apart from these
formats there are XML-based or SGML-based formats that can only be read by
special software.
Such files cannot be accepted without further verification;
please check with DANS.

??? abstract "Connections between SG/X/HT/XHT-ML"
    [SGML](../fileFormats/sgml.md) is a classic, which has been extensively used to manufacture large
    bodies of documentation.

    Slightly newer is [HTML](../fileFormats/html.md), which is the defining characteristic of the world
    wide web.

    [XML](../fileFormats/xml.md) arose as an attempt to make [SGML](../fileFormats/sgml.md) simpler and to subsume [HTML](../fileFormats/html.md) in the
    process.

    Technically, [XML](../fileFormats/xml.md) is an application profile of the
    ISO standard [SGML](../fileFormats/sgml.md): all [XML](../fileFormats/xml.md) files are [SGML](../fileFormats/sgml.md) files. Since XML has a much
    stricter syntax, it is easier to validate.
    Since then, [XML](../fileFormats/xml.md) has evolved further, there are various definition schemes and
    ways of validating [XML](../fileFormats/xml.md), and it contains elements that are not
    defined in SGML in the same way, such as the encoding attribute.
    All text in an [XML](../fileFormats/xml.md) document is by definition in [Unicode]({{unicode}}).

    [HTML](../fileFormats/html.md) is another variant of SGML; it is primarily intended for the
    presentation of rich text (and layout) and hyperlinks to other documents.

    In addition to “regular” [HTML](../fileFormats/html.md) there is also [XHTML](../fileFormats/xhtml.md), which is [HTML](../fileFormats/html.md) under the
    stricter rules of [XML](../fileFormats/xml.md).

    [SGML](../fileFormats/sgml.md) and [XML](../fileFormats/xml.md) are hardly being further developed.

??? info "Quirks in the history of HTML"
    The story of [HTML](../fileFormats/html.md) is more intriguing.
    Whereas the W3C has tried,
    [for a long time]({{html52}}#introduction-history),
    to integrate [HTML](../fileFormats/html.md) with [XML](../fileFormats/xml.md),
    the browser vendors, united in the
    [WhatWG]({{whatwg}}) consider [HTML](../fileFormats/html.md) itself as the technique to develop further and have
    defined HTML as a Living Standard]({{htmlliving}}).
    The ways have not really parted, because W3C and WhatWG have
    signed a [memorandum of understanding]({{w3cwhatwg}}).

### Markdown, YAML and JSON

These three formats have become very popular in a wide range of contexts.
They are not as strictly defined as [XML](../fileFormats/xml.md) and [HTML](../fileFormats/html.md).
[Markdown](../fileFormats/markdown.md) especially has many alternative syntaxes, extensions, and 
variations. [Markdown](../fileFormats/markdown.md) essentially translates to [HTML](../fileFormats/html.md),
and most Markdown processor allow interspersed [HTML](../fileFormats/html.md).
That being said, markdown processors also tend to strip such [HTML](../fileFormats/html.md) if it is
considered dangerous.

??? info "Raison d'être"
    The richness of [XML](../fileFormats/xml.md) and [HTML](../fileFormats/html.md) comes at a price:
    they are unsuitable for being typed by a human.

    In scenarios where people have to write extensive documentation and
    configuration, new light-weight conventions have evolved for for typing
    formatted text using minimal markup overhead.
    The visual layout inside a plain text file, by means of white space and
    newlines,
    plus a few ASCII patterns with a special meaning serve as markup.

    Out of this comes [Markdown](../fileFormats/markdown.md) as a format for writing rich text,
    and [YAML](../fileFormats/yaml.md) has a format for writing nested structures.

    [JSON](../fileFormats/json.md) is a strict format from the [Javascript]({{jsmdn}}) world.
    It is a way to serialize structrured data, very much like [YAML](../fileFormats/yaml.md), but with
    a syntax that is very close to JavaScript.
    [JSON](../fileFormats/json.md) has largely taken over a particular role of [XML](../fileFormats/xml.md): exchanging data
    between computers over a network.

### Tex and LaTeX

Both are used extensively in science and scholarship for writing and publishing papers,
mostly in the exact sciences where mathematical formulas are prominent
but also in the huimanities where non alphabetic symbols are being used,
e.g. music and exotic languages.

Many documentation tools use [TeX](../fileFormats/tex.md) as an intermediate format from which they
generate [PDF](../fileFormats/pdf.md).

??? info "History"
    One of the first uses of markup for professional type-setting is the classic
    [`TeX`]({{tex}}).
    Here text is interspersed with macros and commands, most of which start with a
    backslash.
    Whereas `TeX` provides an extremely powerful base for doing typographical
    computations,
    [`LaTeX`]({{latex}}) has been developed as a system to limit the power of raw
    `TeX` to more friendly and higher level commands.

## Recommendations

With markup there are two issues that matter greatly for long-term preservation:

*   has the markup been applied in a **valid** way?
*   is the marked up file **complete**, i.e. self-contained?

### Validity

Validity of a marked up file means that it can be parsed, which is almost always
the first step one has to take in order to make use of such a file.

For [TeX](../fileFormats/tex.md) the criterion is: can the `TeX` processor handle the file.
Unfortunately, there is no rigorous way to test that other than ... running
`TeX`.

For [JSON](../fileFormats/json.md), [Markdown](../fileFormats/markdown.md), [YAML](../fileFormats/yaml.md), [HTML](../fileFormats/html.md), and [XHTML](../fileFormats/xhtml.md)
the notion of validity is simple: either the file
parses, or it does not.

For [SGML](../fileFormats/sgml.md) and [XML](../fileFormats/xml.md) the notion of validity has been divided into **well-formedness** and
**validity**.

??? note "Well-formed and valid"
    Well-formed documents have a correct mixture of markup and text, i.e. the markup
    elements are properly shaped, start tags and end tags match, all characters are
    defined. It is a largely cosmetic, but essential requirement.

    Valid markup language documents are well-formed and moreover comply with
    an extra set of rules about how the marked up elements hang together.

    Through schemas, entirely new “file formats” can be defined, such as

    format | description
    --- | ---
    [SVG](../fileFormats/svg.md) | vector graphics
    [Text Encoding Initiative (TEI)]({{tei}}) | format and annotate text
    [MathML]({{mathml}}) | mathematical formulas
    [SMIL]({{smil}}) | synchronized multimedia

    The [World Wide Web Consortium (W3C)]({{w3c}}) manages the specifications for
    [HTML](../fileFormats/html.md) and [XML](../fileFormats/xml.md),
    and provides a
    [Markup Validator]({{mvalidator}})
    that can validate both [XHTML](../fileFormats/xhtml.md) and [HTML](../fileFormats/html.md) and additional XML-based formats.

    These rules that govern the content of a markup document can be described with
    the help of various substandards, such as a
    [DTD]({{xmldtd}}),
    a 
    [W3C schema]({{xmlschema}}),
    or a
    [Relax NG schema]({{relaxng}}).

    At the top of [XML](../fileFormats/xml.md) and [XHTML](../fileFormats/xhtml.md) documents is a declaration
    that may refer to such a schema.

    Whether a file can be validated or not, depends on the presence of such a
    schema.
    And that is, in itself, a matter of completeness.

### Completeness

Markup may be based on the use of multiple files in additional file formats.

For [JSON](../fileFormats/json.md) and [YAML](../fileFormats/yaml.md) this does not play a role.

For [TeX](../fileFormats/tex.md) this is about style file and package files.
By studying the log file of a `TeX` run one can see which files are needed
for that run.

For [SGML](../fileFormats/sgml.md), [XML](../fileFormats/xml.md), and [XHTML](../fileFormats/xhtml.md) it is a matter
of style sheets (e.g. [CSS](../fileFormats/css.md), [XSLT](../fileFormats/xslt.md)),
scripts (e.g. [JavaScript](../fileFormats/javascript.md)),
fonts (e.g. [WOFF](../fileFormats/woff.md)),
and graphics (e.g. [PNG](../fileFormats/png.md))
and the schemas by which the validity is checked.

???+ caution "Schemas"
    Last, but not least, the presence of a schema is a matter of completeness.
    There are three possibilities about where the schema can be found:

    1.  inside the marked up file;
    2.  on the local file system relative to the marked up file;
    2.  on the local file system, absolutely addressed;
    4.  online.

    Ad 1. This is the easiest case. The schema will always be available.

    Ad 2. Care must be taken that the schema is archived as well, and in the same relative
    position to the marked up file.

    Ad 3. Care must be taken that the schema is archived as well, and possibly the
    marked up file must be changed so that the location of the schema is given in an
    absolute way.

    Ad 4. Ideally, a local copy of the schema should be attached,
    unless it is available at a reliable public service. 

If a non-standard schema is used, the data depositor should consult DANS beforehand.


