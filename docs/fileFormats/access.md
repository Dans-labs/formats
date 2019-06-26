![img](../images/formats.png){: width="100" align="right"}
![img](../images/DANS.png){: width="200" align="right"}

---

**this documentation is under development**

[current docs]({{preferredFormats}})

---



# Access

**Microsoft Access Database**

item | info
--- | ---
type | Database
preferred | ❌ no
extensions | [`accdb`](../extensions/accdb.md), [`mdb`](../extensions/mdb.md)
wikipedia | [`Microsoft_Access`]({{wikipedia}}/Microsoft_Access)

# Description

Microsoft Access is widely used for creating databases. The Access
[.mdb](../extensions/mdb.md) and [.accdb](../extensions/accdb.md)
formats are, however, very poorly supported outside the commercial
versions of Microsoft Access.
Owing to the different versions of these formats,
even Access itself will not always support the files very well.

DANS has
enabled many databases created with Microsoft Access to be processed in a
sustainable and accessible manner by storing the tables from the database as
separate [CSV](../fileFormats/csv.md) text files.

# Recommendation

Export data as [CSV](../fileFormats/csv.md) and data description as [PDF/A](../fileFormats/pdfa.md).

When storing the tables as CSV files, only the
tabular data from a database are retained.

In Microsoft Access databases, the Database
Documentation feature can be used to generate a document with column
descriptions and table relationships.
This document has data type [Text (formatted)](../dataTypes/textFormatted.md)
and can be stored as a [PDF/A](../fileFormats/pdfa.md) file.

It must be
ensured that all codes and variables used can be explained.
This may mean
providing more detailed descriptions in a separate document or “code book”.


## See also
*   [`{{msaccess}}`]({{msaccess}})
*   [`{{msaccesscom}}`]({{msaccesscom}})




---

Preferred Formats Documention **(under development)**

---

[Current documentation]({{preferredFormats}})

[Data Archiving and Networked Services (DANS)]({{dans}})

![img](../images/formats.png){: width="100" align="right"}
![img](../images/DANS.png){: width="200" align="right"}
