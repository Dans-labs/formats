

# SIARD

**Software Independent Archiving of Relational Databases**

???+ abstract "In short"
    A modern attempt to represent relational data in a software-indpependent way.

item | info
--- | ---
types | [Database](../dataTypes/database.md)
preferred | ✅ yes
extensions | [`.siard`](../extensions/siard.md)
related formats | [Access](../fileFormats/access.md), [CSV](../fileFormats/csv.md), [dbase](../fileFormats/dbase.md), [HDF5](../fileFormats/hdf5.md), [SQL](../fileFormats/sql.md), [XML](../fileFormats/xml.md)
wikipedia | [`SIARD_Suite`]({{wikipedia}}/SIARD_Suite)

## Description

For relational databases, SIARD is seen as
a suitable and sustainable format. SIARD (Software Independent Archiving of
Relational Databases) is intended for archiving relational databases in a way
that is as independent of the original DBMS as possible. This format takes into
account all the significant characteristics of databases. SIARD is an open,
freely available format, based on clear text formats:
[Unicode]({{unicode}}), [XML](../fileFormats/xml.md), [SQL](../fileFormats/sql.md) (1999).
This makes it accessible for various tools.

SIARD is a relatively young format.

??? tip "Software"
    There are tools for converting databases to SIARD and for validating the format,
    but the possibilities are limited. Some conversion tools such as
    [AccessToSiard]({{coptr}}/AccessToSiard)
    and
    [CSV2SIARD]({{coptr}}/CSV2SIARD)
    can be found via
    [COPTR (Community Owned Preservation ToolRegistry]({{coptr}}/Category:File_Format_Migration).
    Using these tools requires the
    [SIARD Suite]({{coptr}}/SIARD_Suite) (free of charge).

## Recommendations

Databases can use routines which may be
dependent on their own scripting languages or programming languages from the
DBMS. When converting to SIARD there is the potential risk of loss of such
routines, but this risk is not considered to be very big because such
languages are not expected to become obsolete.


## See also
*   [`{{siard}}`]({{siard}})



