

# CSV

**Comma Separated Values**

???+ abstract "In short"
    Plain text files with rows and columns separated by a comma or other character.

item | info
--- | ---
types | [Database](../dataTypes/database.md), [Text (plain)](../dataTypes/textPlain.md)
preferred | ⚠️ under conditions
extensions | [`.csv`](../extensions/csv.md), [`.tsv`](../extensions/tsv.md)
related formats | [Access](../fileFormats/access.md), [CSS](../fileFormats/css.md), [dbase](../fileFormats/dbase.md), [HDF5](../fileFormats/hdf5.md), [HTML](../fileFormats/html.md), [JSON](../fileFormats/json.md), [Markdown](../fileFormats/markdown.md), [SIARD](../fileFormats/siard.md), [SQL](../fileFormats/sql.md), [TeX](../fileFormats/tex.md), [Text](../fileFormats/text.md), [XML](../fileFormats/xml.md), [YAML](../fileFormats/yaml.md)
wikipedia | [`Comma-separated_values`]({{wikipedia}}/Comma-separated_values)

## Description

CSV files contain tabular data as [Text](../fileFormats/text.md).
This format does not support data types and metadata beyond column titles. It is
in fact based on the
[RFC4180]({{csvrfc}})
open standard, although there are different
variants (dialects).

In a CSV file the values/cells from a table are separated
by commas, semicolons, or tabs.

CSV files can be imported into database applications, but they can
also clearly and quickly be opened as a spreadsheet, for example in Microsoft
Excel. These files can also be read as [Text](../fileFormats/text.md) files, for instance in Notepad.
Many applications will be able to open CSV files without problems.

## Separator character
The file extension derives from the original separator character, the **c**omma.
However, other characters such as the semicolon are also frequently used,
especially in regions where they are the default separator character.

??? caution "Complications with the comma"
    A region-independent choice of separator character is the *tab*, and CSV files
    that use it are often given the extension [.tsv](../extensions/tsv.md).

    Depending on
    the computer’s default settings for the use of separators, an application may
    not be able to automatically separate the columns.

    However, within the application it is usually possible to divide text into columns
    on the basis of separation characters chosen by the user;
    alternatively, the default on the computer can be adjusted.

    For Windows systems, this default
    setting can be found under List separator on the Region and Language screen. If
    the same separator is selected as what is found in the CSV file,
    that CSV file will be correctly displayed in distinct columns in all applications.

## Character encoding.

There is no standard to declare the character encoding that is used in a CSV
file.
If the CSV file is in Unicode, there are still many options for the encoding,
such as `utf8`, `utf16 (big endian)`, `utf16 (least endian)`.

??? info "Details"
    These encodings can be indicated by an optional first character in a file,
    the so-called
    [Byte Order Mark (BOM)]({{wikipedia}}/Byte_order_mark).

    If the encoding is `utf8`, the BOM is usually left out.

    A CSV file with non-latin characters is best encoded as `utf16 least endian`
    with BOM mark. It seems to be the only option if one wants Excel to open the
    file without trouble.

See also [Text (plain)](../dataTypes/textPlain.md).


## See also
*   [`{{csvrfc}}`]({{csvrfc}})



