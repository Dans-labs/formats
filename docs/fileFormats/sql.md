[go to current production version]({{preferredFormats}})

---



# SQL

**Structured Query Language**

???+ abstract "In short"
    A long standing, ubiquitous way of handling and packaging relational databases.

item | info
--- | ---
types | [Data (container)](../dataTypes/dataContainer.md), [Database](../dataTypes/database.md), [Text (plain)](../dataTypes/textPlain.md)
preferred | ✅ yes
extensions | [`.sql`](../extensions/sql.md)
related formats | [Access](../fileFormats/access.md), [CSS](../fileFormats/css.md), [CSV](../fileFormats/csv.md), [CSV](../fileFormats/csv.md), [dbase](../fileFormats/dbase.md), [HDF5](../fileFormats/hdf5.md), [HTML](../fileFormats/html.md), [JSON](../fileFormats/json.md), [JSON](../fileFormats/json.md), [Markdown](../fileFormats/markdown.md), [SIARD](../fileFormats/siard.md), [TAR](../fileFormats/tar.md), [TeX](../fileFormats/tex.md), [Text](../fileFormats/text.md), [XML](../fileFormats/xml.md), [XML](../fileFormats/xml.md), [XML](../fileFormats/xml.md), [YAML](../fileFormats/yaml.md), [YAML](../fileFormats/yaml.md)
wikipedia | [`SQL`]({{wikipedia}}/SQL)

## Description

Many DBMSs
support the ISO standardized version of
Structured Query Language (SQL).
This is
a language for querying and updating relational databases. Together with the
data definition language, used to define and modify schemas, the contents of a
database can be stored as a collection of schema and data statements.

The
language rarely changes, but various modifications and additions may change
along with software updates. When extensions are used, the documentation must
show which SQL version has been used.

## Recommendations

In SQL it is possible to refer to
non-existent or external data without invalidating the file. If SQL is used for
data exchange, any references must therefore be supplied, or each reference must
be replaced by the data referred to.


## See also
*   [`{{mysql}}`]({{mysql}})
*   [`{{sqldoc}}`]({{sqldoc}})




---

[go to current production version]({{preferredFormats}})
