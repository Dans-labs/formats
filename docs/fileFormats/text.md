![img](../images/formats.png){: width="100" align="right"}
![img](../images/DANS.png){: width="200" align="right"}

---

**this documentation is under development**

[current docs]({{preferredFormats}})

---



# Text

**Plain text**

???+ abstract "In short"
    Various instances where plain text is used such as running text, lists, log files, configuration files.

item | info
--- | ---
types | [Text (plain)](../dataTypes/textPlain.md)
preferred | ⚠️ under conditions
extensions | [`.cfg`](../extensions/cfg.md), [`.ini`](../extensions/ini.md), [`.log`](../extensions/log.md), [`.lst`](../extensions/lst.md), [`.text`](../extensions/text.md), [`.txt`](../extensions/txt.md)
related formats | [CSS](../fileFormats/css.md), [CSV](../fileFormats/csv.md), [HTML](../fileFormats/html.md), [JSON](../fileFormats/json.md), [Markdown](../fileFormats/markdown.md), [SQL](../fileFormats/sql.md), [TeX](../fileFormats/tex.md), [XML](../fileFormats/xml.md), [YAML](../fileFormats/yaml.md)
wikipedia | [`Plain_text`]({{wikipedia}}/Plain_text), [`UTF-8`]({{wikipedia}}/UTF-8), [`Byte_order_mark`]({{wikipedia}}/Byte_order_mark)

## Description

Plain text is a data type that requires very little software to interpret it.
The software that is required, is usually part of the operating system, such 
as *notepad* on Windows, *Text Edit* on the Mac, or the *Terminal* or *command
prompt* on all systems.

Plain text is used for text without formatting, for configuration documents,
for logging, for data, and for programming.

It can be produced by humans, typing on the keyboard or dictating in a
microphone, but also by programs, scripts and commands on the terminal.

## Recommendations

We are confident that uncategorized plain text files
using the Unicode character set,
encoded as
[UTF8]({{wikipedia}}/UTF-8)
without
[Byte Order Mark (BOM)]({{wikipedia}}/Byte_order_mark)
or in an other UTF encoding with
[Byte Order Mark (BOM)]({{wikipedia}}/Byte_order_mark),
can be represented correctly in most computing environments.

??? explanation "Programm code"
    For program files, it is recommended to follow the best practices for
    that programming language.
    It is dependent on the programming language how the character encoding must be
    specified, and what the default encoding is.


## See also
*   [`{{unicode}}`]({{unicode}})




---

Preferred Formats Documention **(under development)**

---

[Current documentation]({{preferredFormats}})

[Data Archiving and Networked Services (DANS)]({{dans}})

![img](../images/formats.png){: width="100" align="right"}
![img](../images/DANS.png){: width="200" align="right"}
