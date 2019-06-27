![img](../images/formats.png){: width="100" align="right"}
![img](../images/DANS.png){: width="200" align="right"}

---

**this documentation is under development**

[current docs]({{preferredFormats}})

---



# Text (plain)

**Readable text without special formatting codes**

item | info
--- | ---
formats | [CSS](../fileFormats/css.md), [CSV](../fileFormats/csv.md), [HTML](../fileFormats/html.md), [JSON](../fileFormats/json.md), [Markdown](../fileFormats/markdown.md), [SQL](../fileFormats/sql.md), [TeX](../fileFormats/tex.md), [Text](../fileFormats/text.md), [XML](../fileFormats/xml.md), [YAML](../fileFormats/yaml.md)
extensions | [`cfg`](../extensions/cfg.md), [`css`](../extensions/css.md), [`csv`](../extensions/csv.md), [`htm`](../extensions/htm.md), [`html`](../extensions/html.md), [`ini`](../extensions/ini.md), [`json`](../extensions/json.md), [`log`](../extensions/log.md), [`lst`](../extensions/lst.md), [`md`](../extensions/md.md), [`sql`](../extensions/sql.md), [`sty`](../extensions/sty.md), [`tex`](../extensions/tex.md), [`text`](../extensions/text.md), [`tsv`](../extensions/tsv.md), [`txt`](../extensions/txt.md), [`xml`](../extensions/xml.md), [`yaml`](../extensions/yaml.md)

## Description

Text is a broad category of data.
For some, text is something that you type with Microsoft Word,
for others it is what they read in a [PDF](../fileFormats/pdf.md), and for yet others it is the
program code they hack in a text editor.

For the purposes of archiving we divide the text data type in 
[Text (formatted)](../dataTypes/textFormatted.md) and [Text (plain)](../dataTypes/textPlain.md).

Plain text consists of text strings without any particular layout information
other than that which can be achieved by spaces, tabs and newlines.

Plain text is mostly used for IT purposes:

*   writing quick notes, using a simple program like *notepad*
    often with extension [.txt](../extensions/txt.md);
    note that [Markdown](../fileFormats/markdown.md) files are themselves
    plain text, but they are used to represent [Text (formatted)](../dataTypes/textFormatted.md) as well;
*   writing software code (programs), using a *text editor* or
    an *IDE* (integrated developing environment);
    see also [Program code](../dataTypes/programCode.md);
*   for data with formal characteristics, such as 
    [JSON](../fileFormats/json.md)
    [CSV](../fileFormats/csv.md)
    [XML](../fileFormats/xml.md)
    [SQL](../fileFormats/sql.md)

## Information representation

Computer files are either binary, in which case they are just a sequence of bits
(1 and 0), or they are text files, in which case they are interpreted as a
sequence of characters, separated by line breaks.

### Text files versus binary files

There are several notions of what a character is and what a line break is.
A Windows line break is different from a Unix/Linux/Mac line break, and line
breaks on OS9 Macs are yet different.

### Character encoding

What a character is, is determined by an *encoding*, which is a system to map
characters to sequences of bits.

The most ubiquitous character encoding is
[ASCII]({{wikipedia}}/ASCII).
It encodes a set of 128 characters.
This is a basic set consisting of letters, uppercase and lowercase,
digits, punctuation, arithmetical symbols, a few currency symbols, space, tab,
newline, carriage return, and a few others.

Later came the extensions for letters with accents, for other scripts such as
Cyrillic and Greek.
The first was IBM's [CP437]({{wikipedia}}/Code_page_437)
These extension sets were defined by
[code pages]({{wikipedia}}/ISO/IEC_8859),
each of which defined a limited supply of non-ascii characters.

Windows had its own notion of code page: 
[125x]({{wikipedia}}/Windows_code_page).

All this was common before UNICODE.
Text files from this era pose the difficulty that nothing in the file itself
declares which code page is being used. It is a matter of trial and error to
determine the right code page, and sometimes it is impossible.

This problem is carried over to older text-based formats such as 
[CSV](../fileFormats/csv.md) and [SQL](../fileFormats/sql.md).

While the structure of [SQL](../fileFormats/sql.md) and [CSV](../fileFormats/csv.md) files is usually well-defined, the use of
undeclared code pages remains a liability.

### Unicode

When [Unicode]({{unicode}})
arrived, it had the promise to tidy up most character issues.
The Unicode standard is a major achievement.
It not only maps nearly every written glyph unto a unique number, it also
defines the notions of upper case and lower case intelligently, and it defines
types of characters, such as letters, numerals, punctuation, and much more.

Last but not least, associated with Unicode are severel encodings to map the
unique numbers to streams of bits in efficient ways.

In today's world, 
[UTF8]({{wikipedia}}/UTF-8)
is very common, and especially
suited to Western languages, because it coincides with ASCII for
the ASCII characters. 

Other encodings are [UTF16]({{wikipedia}}/UTF-16)
and [UTF32]({{wikipedia}}/UTF-32).

### Specifying a Unicode encoding

File formats such as [XML](../fileFormats/xml.md) make it clear which Unicode
encoding is being used.

But in general, file types for plain text do not specify the encoding in a
standard way.

The recommendation is to let a non-UTF8 file start with a special character,
the [Byte Order Mark (BOM)]({{wikipedia}}/Byte_order_mark), from
which most applications can deduce the encoding that is being used.



---

Preferred Formats Documention **(under development)**

---

[Current documentation]({{preferredFormats}})

[Data Archiving and Networked Services (DANS)]({{dans}})

![img](../images/formats.png){: width="100" align="right"}
![img](../images/DANS.png){: width="200" align="right"}
