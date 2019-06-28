![img](../images/formats.png){: width="100" align="right"}
![img](../images/DANS.png){: width="200" align="right"}

---

**this documentation is under development**

[current docs]({{preferredFormats}})

---



# JavaScript

**JavaScript**

???+ abstract "In short"
    Fast and elegant scripting language that runs inside the browser, although it can also run stand alone; it has a checkered history.

item | info
--- | ---
types | [Markup](../dataTypes/markup.md), [Program code](../dataTypes/programCode.md)
preferred | ❎ not applicable
extensions | [`.es`](../extensions/es.md), [`.js`](../extensions/js.md)
related formats | [C](../fileFormats/c.md), [CPP](../fileFormats/cpp.md), [CSS](../fileFormats/css.md), [HTML](../fileFormats/html.md), [JAVA](../fileFormats/java.md), [JSX](../fileFormats/jsx.md), [JSX](../fileFormats/jsx.md), [Markdown](../fileFormats/markdown.md), [Pascal](../fileFormats/pascal.md), [Perl](../fileFormats/perl.md), [Prolog](../fileFormats/prolog.md), [Python](../fileFormats/python.md), [Ruby](../fileFormats/ruby.md), [Scala](../fileFormats/scala.md), [SGML](../fileFormats/sgml.md), [TeX](../fileFormats/tex.md), [XHTML](../fileFormats/xhtml.md), [XML](../fileFormats/xml.md), [XSLT](../fileFormats/xslt.md), [XSLT](../fileFormats/xslt.md)
wikipedia | [`JavaScript`]({{wikipedia}}/JavaScript)

## Description

JavaScript or more formally ECMAScript or ES6 is a scripting language that has
been developed in a web context, but that has evolved into a full-fledged
programming language.

??? explanation "History"
    It used to be a rather ugly and slow scripting language, snippets of which
    were included in [HTML](../fileFormats/html.md) pages to add interaction to elements on the page and
    to submit forms. 
    In those times it had competitors such as VBScript and PerlScript.

    When Google introduced the Chrome browser it included a
    [Javascript engine]({{chromev8}}) 
    that had a performance that was unheard of.

    Nowadays JavaScript is a capable, performant, and neat language that runs inside
    the browser as well outside it, through [Node]({{nodejs}}).

    Since 2015 JavaScript is undergoing extensive development in a backwards
    compatible way.
    In that year, 
    [ECMA Script 6, or more fondly, ES6]({{es6}})
    was standardized.
    Now, in 2019, nearly all of ES6 is nearly fully implemented in nearly all major
    browsers on nearly all platforms and form factors.
    See the [details]({{es6features}}).

    Despite the lack of implementation during the years 2015-2019, many
    websites have been developed with ES6, using 
    [Babel]({{babel}}), a transpiler that converts ES6 into pre-2015 Javascript.
    By the same approach, newer, post-ES6 features can be used in applications.

??? explanation "Modern uses"
    Modern websites have taken a lot of advantage from modern JavaScript.
    There has been a tendency to move processing on the server to the client,
    which has lead to so-called 
    [Single Page Applications (SPA)](Single-page_application),
    where the whole website is generated dynamically inside the browser.

    This poses new challenges for the archiving of websites in general.

    For SPAs to work correctly and optimally, web-frameworks such as
    [React]({{react}}) and [Angular]({{angular}}) and [Vue]({{vue}}) are needed that 
    supply basic functions in the information flow.
    These package require subpackages, and they in turn require subpackages, and the
    app has a whole needs a build framework such as 
    [WebPack]({{webpack}}) to bundle everything together, often for a development
    scenario as well as a production scenario.
    A moderate SPA requires easily hundreds of packages.
    It is nearly a miracle that is works, and even a greater miracle that these SPAs
    tend to work in most browsers.

    Like [CSS](../fileFormats/css.md), the JavaScript in an SPA tends to be `uglified`, i.e. compressed by
    removing all unnecessary whitespace and line-breaks and replacing all names by
    meaningless short names.

## Recommendations

In order to archive a website that has been built as an SPA, one needs to
archive the full build environment in its original organization.
Care must be taken that the subfolder `node_modules` exists and contains
all the dependencies used by the SPA and not much more.


## See also
*   [`{{js}}`]({{js}})
*   [`{{jsmdn}}`]({{jsmdn}})




---

Preferred Formats Documention **(under development)**

---

[Current documentation]({{preferredFormats}})

[Data Archiving and Networked Services (DANS)]({{dans}})

![img](../images/formats.png){: width="100" align="right"}
![img](../images/DANS.png){: width="200" align="right"}
