{{header}}

key | value
--- | ---
extensions | `.mdb` `.accdb`
data types | [database](../dataTypes/database.md)
preferred | ❌

## Description

[Microsoft Access]({{wikipedia}}/Microsoft_Access#File_extensions)
is widely used for creating databases. The Access
MDB
and
ACCDB
formats are, however, very poorly supported outside the commercial
versions of Microsoft Access. Owing to the different versions of these formats,
even Access itself will not always support the files very well.

DANS has
enabled many databases created with Microsoft Access to be processed in a
sustainable and accessible manner by storing the tables from the database as
separate [CSV](csv.md) text files.

### Recommendation

Export data as [CSV](csv.md) and data description as [PDF/A](pdfa.md).

When storing the tables as CSV files, only the
tabular data from a database are retained.

In Microsoft Access databases, the Database
Documentation feature can be used to generate a document with column
descriptions and table relationships.

This document has data type [formatted text](../dataTypes/formattedText.md)
and can be stored as a [PDF/A](pdfa.md) file.

It must be
ensured that all codes and variables used can be explained.
This may mean
providing more detailed descriptions in a separate document or “code book”.

{{footer}}
