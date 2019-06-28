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

??? explanation "Connections between SG/X/HT/XHT-ML"
    [=sgml] is a classic, which has been extensively used to manufacture large
    bodies of documentation.

    Slightly newer is [=html], which is the defining characteristic of the world
    wide web.

    [=xml] arose as an attempt to make [=sgml] simpler and to subsume [=html] in the
    process.

    Technically, [=xml] is an application profile of the
    ISO standard [=sgml]: all [=xml] files are [=sgml] files. Since XML has a much
    stricter syntax, it is easier to validate.
    Since then, [=xml] has evolved further, there are various definition schemes and
    ways of validating [=xml], and it contains elements that are not
    defined in SGML in the same way, such as the encoding attribute.
    All text in an [=xml] document is by definition in [Unicode]({{unicode}}).

    [=html] is another variant of SGML; it is primarily intended for the
    presentation of rich text (and layout) and hyperlinks to other documents.

    In addition to “regular” [=html] there is also [=xhtml], which is [=html] under the
    stricter rules of [=xml].

    [=sgml] and [=xml] are hardly being further developed.

??? explanation "Quirks in the history of HTML"
    The story of [=html] is more intriguing.
    Whereas the W3C has tried,
    [for a long time]({{html52}}#introduction-history),
    to integrate [=html] with [=xml],
    the browser vendors, united in the
    [WhatWG]({{whatwg}}) consider [=html] itself as the technique to develop further and have
    defined HTML as a Living Standard]({{htmlliving}}).
    The ways have not really parted, because W3C and WhatWG have
    signed a [memorandum of understanding]({{w3cwhatwg}}).

### Markdown, YAML and JSON

These three formats have become very popular in a wide range of contexts.
They are not as strictly defined as [=xml] and [=html].
[=markdown] especially has many alternative syntaxes, extensions, and 
variations. [=markdown] essentially translates to [=html],
and most Markdown processor allow interspersed [=html].
That being said, markdown processors also tend to strip such [=html] if it is
considered dangerous.

??? explanation "Raison d'être"
    The richness of [=xml] and [=html] comes at a price:
    they are unsuitable for being typed by a human.

    In scenarios where people have to write extensive documentation and
    configuration, new light-weight conventions have evolved for for typing
    formatted text using minimal markup overhead.
    The visual layout inside a plain text file, by means of white space and
    newlines,
    plus a few ASCII patterns with a special meaning serve as markup.

    Out of this comes [=markdown] as a format for writing rich text,
    and [=yaml] has a format for writing nested structures.

    [=json] is a strict format from the [Javascript]({{jsmdn}}) world.
    It is a way to serialize structrured data, very much like [=yaml], but with
    a syntax that is very close to JavaScript.
    [=json] has largely taken over a particular role of [=xml]: exchanging data
    between computers over a network.

### Tex and LaTeX

Both are used extensively in science and scholarship for writing and publishing papers,
mostly in the exact sciences where mathematical formulas are prominent
but also in the huimanities where non alphabetic symbols are being used,
e.g. music and exotic languages.

Many documentation tools use [=tex] as an intermediate format from which they
generate [=pdf].

??? explanation "History"
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

For [=tex] the criterion is: can the `TeX` processor handle the file.
Unfortunately, there is no rigorous way to test that other than ... running
`TeX`.

For [=json], [=markdown], [=yaml], [=html], and [=xhtml]
the notion of validity is simple: either the file
parses, or it does not.

For [=sgml] and [=xml] the notion of validity has been divided into **well-formedness** and
**validity**.

??? explanation "Well-formed and valid"
    Well-formed documents have a correct mixture of markup and text, i.e. the markup
    elements are properly shaped, start tags and end tags match, all characters are
    defined. It is a largely cosmetic, but essential requirement.

    Valid markup language documents are well-formed and moreover comply with
    an extra set of rules about how the marked up elements hang together.

    Through schemas, entirely new “file formats” can be defined, such as

    format | description
    --- | ---
    [=svg] | vector graphics
    [Text Encoding Initiative (TEI)]({{tei}}) | format and annotate text
    [MathML]({{mathml}}) | mathematical formulas
    [SMIL]({{smil}}) | synchronized multimedia

    The [World Wide Web Consortium (W3C)]({{w3c}}) manages the specifications for
    [=html] and [=xml],
    and provides a
    [Markup Validator]({{mvalidator}})
    that can validate both [=xhtml] and [=html] and additional XML-based formats.

    These rules that govern the content of a markup document can be described with
    the help of various substandards, such as a
    [DTD]({{xmldtd}}),
    a 
    [W3C schema]({{xmlschema}}),
    or a
    [Relax NG schema]({{relaxng}}).

    At the top of [=xml] and [=xhtml] documents is a declaration
    that may refer to such a schema.

    Whether a file can be validated or not, depends on the presence of such a
    schema.
    And that is, in itself, a matter of completeness.

### Completeness

Markup may be based on the use of multiple files in additional file formats.

For [=json] and [=yaml] this does not play a role.

For [=tex] this is about style file and package files.
By studying the log file of a `TeX` run one can see which files are needed
for that run.

For [=sgml], [=xml], and [=xhtml] it is a matter
of style sheets (e.g. [=css], [=xslt]),
scripts (e.g. [=javascript]),
fonts (e.g. [=woff]),
and graphics (e.g. [=png])
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
