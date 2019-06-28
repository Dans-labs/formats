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
