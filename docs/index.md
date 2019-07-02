
## Overview

Here is a list of *file formats* under consideration, some of which
we consider *preferred formats* for archiving.
See [about](about.md) for background.

Click on an entry for more information.
Alternatively, use the navigation menu.

??? explanation "Concepts"
    A *data type* is a way of organizing raw data for specific modelling applications
    such as image, sound, text, structured data, etc. 

    A file format is a way to serialize the data of a specific data type to a file
    such as [PDF](fileFormats/pdf.md), [XLSX](fileFormats/xlsx.md), [SIARD](fileFormats/siard.md), etc.

    Applications that deal with that data are programmed in such a way that they can
    read one or more file formats for that type.

    When data is written to file in a specific file format, the file name often gets
    an extension that indicates that file format
    such as [.pdf](extensions/pdf.md), [.xlsx](extensions/xlsx.md), etc.

    There are usually several file formats associated with one data type.

??? explanation "Legenda"

    icon | meaning
    --- | ---
    ❎ | not applicable
    ✅ | yes
    ⚠️ | under conditions
    ❌ | no
    ❔ | undecided



File format | Preferred ? | Extensions | Related | Data types
--- | --- | --- | --- | ---
[Access](fileFormats/access.md) | ❌ | [`.accdb`](extensions/accdb.md), [`.mdb`](extensions/mdb.md) | [CSV](fileFormats/csv.md), [dbase](fileFormats/dbase.md), [HDF5](fileFormats/hdf5.md), [SIARD](fileFormats/siard.md), [SQL](fileFormats/sql.md), [XML](fileFormats/xml.md) | [Database](dataTypes/database.md)
[C](fileFormats/c.md) | ❎ | [`.c`](extensions/c.md), [`.h`](extensions/h.md) | [CPP](fileFormats/cpp.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[CPP](fileFormats/cpp.md) | ❎ | [`.cpp`](extensions/cpp.md), [`.h`](extensions/h.md) | [C](fileFormats/c.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[CSS](fileFormats/css.md) | ⚠️ | [`.css`](extensions/css.md) | [CSV](fileFormats/csv.md), [HTML](fileFormats/html.md), [JavaScript](fileFormats/javascript.md), [JSON](fileFormats/json.md), [JSX](fileFormats/jsx.md), [Markdown](fileFormats/markdown.md), [SGML](fileFormats/sgml.md), [SQL](fileFormats/sql.md), [TeX](fileFormats/tex.md), [Text](fileFormats/text.md), [XHTML](fileFormats/xhtml.md), [XML](fileFormats/xml.md), [XSLT](fileFormats/xslt.md), [YAML](fileFormats/yaml.md) | [Markup](dataTypes/markup.md), [Text (plain)](dataTypes/textPlain.md)
[CSV](fileFormats/csv.md) | ⚠️ | [`.csv`](extensions/csv.md), [`.tsv`](extensions/tsv.md) | [Access](fileFormats/access.md), [CSS](fileFormats/css.md), [dbase](fileFormats/dbase.md), [HDF5](fileFormats/hdf5.md), [HTML](fileFormats/html.md), [JSON](fileFormats/json.md), [Markdown](fileFormats/markdown.md), [SIARD](fileFormats/siard.md), [SQL](fileFormats/sql.md), [TeX](fileFormats/tex.md), [Text](fileFormats/text.md), [XML](fileFormats/xml.md), [YAML](fileFormats/yaml.md) | [Database](dataTypes/database.md), [Text (plain)](dataTypes/textPlain.md)
[dbase](fileFormats/dbase.md) | ❌ | [`.dbf`](extensions/dbf.md) | [Access](fileFormats/access.md), [CSV](fileFormats/csv.md), [HDF5](fileFormats/hdf5.md), [SIARD](fileFormats/siard.md), [SQL](fileFormats/sql.md), [XML](fileFormats/xml.md) | [Database](dataTypes/database.md)
[DOC](fileFormats/doc.md) | ❌ | [`.doc`](extensions/doc.md) | [DOCX](fileFormats/docx.md), [ODT](fileFormats/odt.md), [PDF/A](fileFormats/pdfa.md) | [Text (formatted)](dataTypes/textFormatted.md)
[DOCX](fileFormats/docx.md) | ✅ | [`.docx`](extensions/docx.md) | [DOC](fileFormats/doc.md), [ODT](fileFormats/odt.md), [PDF/A](fileFormats/pdfa.md) | [Text (formatted)](dataTypes/textFormatted.md)
[GIF](fileFormats/gif.md) | ✅ | [`.gif`](extensions/gif.md) | [JPEG](fileFormats/jpeg.md), [PDF](fileFormats/pdf.md), [PDF/A](fileFormats/pdfa.md), [PNG](fileFormats/png.md), [PostScript](fileFormats/postscript.md), [SVG](fileFormats/svg.md), [TIFF](fileFormats/tiff.md) | [Image](dataTypes/image.md)
[HDF5](fileFormats/hdf5.md) | ❌ | [`.hdf5`](extensions/hdf5.md) | [Access](fileFormats/access.md), [CSV](fileFormats/csv.md), [dbase](fileFormats/dbase.md), [SIARD](fileFormats/siard.md), [SQL](fileFormats/sql.md), [XML](fileFormats/xml.md) | [Database](dataTypes/database.md)
[HTML](fileFormats/html.md) | ⚠️ | [`.htm`](extensions/htm.md), [`.html`](extensions/html.md) | [CSS](fileFormats/css.md), [CSV](fileFormats/csv.md), [JavaScript](fileFormats/javascript.md), [JSON](fileFormats/json.md), [JSX](fileFormats/jsx.md), [Markdown](fileFormats/markdown.md), [SGML](fileFormats/sgml.md), [SQL](fileFormats/sql.md), [TeX](fileFormats/tex.md), [Text](fileFormats/text.md), [XHTML](fileFormats/xhtml.md), [XML](fileFormats/xml.md), [XSLT](fileFormats/xslt.md), [YAML](fileFormats/yaml.md) | [Markup](dataTypes/markup.md), [Text (plain)](dataTypes/textPlain.md)
[JAVA](fileFormats/java.md) | ❎ | [`.java`](extensions/java.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[JavaScript](fileFormats/javascript.md) | ❎ | [`.es`](extensions/es.md), [`.js`](extensions/js.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [CSS](fileFormats/css.md), [HTML](fileFormats/html.md), [JAVA](fileFormats/java.md), [JSX](fileFormats/jsx.md), [Markdown](fileFormats/markdown.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [SGML](fileFormats/sgml.md), [TeX](fileFormats/tex.md), [XHTML](fileFormats/xhtml.md), [XML](fileFormats/xml.md), [XSLT](fileFormats/xslt.md) | [Markup](dataTypes/markup.md), [Program code](dataTypes/programCode.md)
[JPEG](fileFormats/jpeg.md) | ✅ | [`.jpeg`](extensions/jpeg.md), [`.jpg`](extensions/jpg.md) | [GIF](fileFormats/gif.md), [PDF](fileFormats/pdf.md), [PDF/A](fileFormats/pdfa.md), [PNG](fileFormats/png.md), [PostScript](fileFormats/postscript.md), [SVG](fileFormats/svg.md), [TIFF](fileFormats/tiff.md) | [Image](dataTypes/image.md)
[JSON](fileFormats/json.md) | ✅ | [`.json`](extensions/json.md) | [CSS](fileFormats/css.md), [CSV](fileFormats/csv.md), [HTML](fileFormats/html.md), [Markdown](fileFormats/markdown.md), [SQL](fileFormats/sql.md), [TAR](fileFormats/tar.md), [TeX](fileFormats/tex.md), [Text](fileFormats/text.md), [XML](fileFormats/xml.md), [YAML](fileFormats/yaml.md) | [Data (container)](dataTypes/dataContainer.md), [Text (plain)](dataTypes/textPlain.md)
[JSX](fileFormats/jsx.md) | ❎ | [`.jsx`](extensions/jsx.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [CSS](fileFormats/css.md), [HTML](fileFormats/html.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [Markdown](fileFormats/markdown.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [SGML](fileFormats/sgml.md), [TeX](fileFormats/tex.md), [XHTML](fileFormats/xhtml.md), [XML](fileFormats/xml.md), [XSLT](fileFormats/xslt.md) | [Markup](dataTypes/markup.md), [Program code](dataTypes/programCode.md)
[Markdown](fileFormats/markdown.md) | ✅ | [`.md`](extensions/md.md) | [CSS](fileFormats/css.md), [CSV](fileFormats/csv.md), [HTML](fileFormats/html.md), [JavaScript](fileFormats/javascript.md), [JSON](fileFormats/json.md), [JSX](fileFormats/jsx.md), [SGML](fileFormats/sgml.md), [SQL](fileFormats/sql.md), [TeX](fileFormats/tex.md), [Text](fileFormats/text.md), [XHTML](fileFormats/xhtml.md), [XML](fileFormats/xml.md), [XSLT](fileFormats/xslt.md), [YAML](fileFormats/yaml.md) | [Markup](dataTypes/markup.md), [Text (plain)](dataTypes/textPlain.md)
[ODS](fileFormats/ods.md) | ✅ | [`.ods`](extensions/ods.md) | [XLS](fileFormats/xls.md), [XLSX](fileFormats/xlsx.md) | [Spreadsheet](dataTypes/spreadsheet.md)
[ODT](fileFormats/odt.md) | ✅ | [`.odt`](extensions/odt.md) | [DOC](fileFormats/doc.md), [DOCX](fileFormats/docx.md), [PDF/A](fileFormats/pdfa.md) | [Text (formatted)](dataTypes/textFormatted.md)
[Pascal](fileFormats/pascal.md) | ❎ | [`.p`](extensions/p.md), [`.pas`](extensions/pas.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[PDF](fileFormats/pdf.md) | ⚠️ | [`.pdf`](extensions/pdf.md) | [GIF](fileFormats/gif.md), [JPEG](fileFormats/jpeg.md), [PDF/A](fileFormats/pdfa.md), [PNG](fileFormats/png.md), [PostScript](fileFormats/postscript.md), [SVG](fileFormats/svg.md), [TIFF](fileFormats/tiff.md) | [Image](dataTypes/image.md)
[PDF/A](fileFormats/pdfa.md) | ✅ | [`.pdf`](extensions/pdf.md) | [DOC](fileFormats/doc.md), [DOCX](fileFormats/docx.md), [GIF](fileFormats/gif.md), [JPEG](fileFormats/jpeg.md), [ODT](fileFormats/odt.md), [PDF](fileFormats/pdf.md), [PNG](fileFormats/png.md), [PostScript](fileFormats/postscript.md), [SVG](fileFormats/svg.md), [TIFF](fileFormats/tiff.md) | [Image](dataTypes/image.md), [Text (formatted)](dataTypes/textFormatted.md)
[Perl](fileFormats/perl.md) | ❎ | [`.p`](extensions/p.md), [`.pl`](extensions/pl.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Pascal](fileFormats/pascal.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[PNG](fileFormats/png.md) | ✅ | [`.png`](extensions/png.md) | [GIF](fileFormats/gif.md), [JPEG](fileFormats/jpeg.md), [PDF](fileFormats/pdf.md), [PDF/A](fileFormats/pdfa.md), [PostScript](fileFormats/postscript.md), [SVG](fileFormats/svg.md), [TIFF](fileFormats/tiff.md) | [Image](dataTypes/image.md)
[PostScript](fileFormats/postscript.md) | ❌ | [`.eps`](extensions/eps.md), [`.ps`](extensions/ps.md) | [GIF](fileFormats/gif.md), [JPEG](fileFormats/jpeg.md), [PDF](fileFormats/pdf.md), [PDF/A](fileFormats/pdfa.md), [PNG](fileFormats/png.md), [SVG](fileFormats/svg.md), [TIFF](fileFormats/tiff.md) | [Image](dataTypes/image.md)
[Prolog](fileFormats/prolog.md) | ❎ | [`.p`](extensions/p.md), [`.pl`](extensions/pl.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[Python](fileFormats/python.md) | ❎ | [`.p`](extensions/p.md), [`.py`](extensions/py.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[Ruby](fileFormats/ruby.md) | ❎ | [`.rb`](extensions/rb.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Scala](fileFormats/scala.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[Scala](fileFormats/scala.md) | ❎ | [`.scala`](extensions/scala.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [XSLT](fileFormats/xslt.md) | [Program code](dataTypes/programCode.md)
[SGML](fileFormats/sgml.md) | ⚠️ | [`.xml`](extensions/xml.md) | [CSS](fileFormats/css.md), [HTML](fileFormats/html.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Markdown](fileFormats/markdown.md), [TeX](fileFormats/tex.md), [XHTML](fileFormats/xhtml.md), [XML](fileFormats/xml.md), [XSLT](fileFormats/xslt.md) | [Markup](dataTypes/markup.md)
[SIARD](fileFormats/siard.md) | ✅ | [`.siard`](extensions/siard.md) | [Access](fileFormats/access.md), [CSV](fileFormats/csv.md), [dbase](fileFormats/dbase.md), [HDF5](fileFormats/hdf5.md), [SQL](fileFormats/sql.md), [XML](fileFormats/xml.md) | [Database](dataTypes/database.md)
[SQL](fileFormats/sql.md) | ✅ | [`.sql`](extensions/sql.md) | [Access](fileFormats/access.md), [CSS](fileFormats/css.md), [CSV](fileFormats/csv.md), [dbase](fileFormats/dbase.md), [HDF5](fileFormats/hdf5.md), [HTML](fileFormats/html.md), [JSON](fileFormats/json.md), [Markdown](fileFormats/markdown.md), [SIARD](fileFormats/siard.md), [TAR](fileFormats/tar.md), [TeX](fileFormats/tex.md), [Text](fileFormats/text.md), [XML](fileFormats/xml.md), [YAML](fileFormats/yaml.md) | [Data (container)](dataTypes/dataContainer.md), [Database](dataTypes/database.md), [Text (plain)](dataTypes/textPlain.md)
[SVG](fileFormats/svg.md) | ✅ | [`.svg`](extensions/svg.md) | [GIF](fileFormats/gif.md), [JPEG](fileFormats/jpeg.md), [PDF](fileFormats/pdf.md), [PDF/A](fileFormats/pdfa.md), [PNG](fileFormats/png.md), [PostScript](fileFormats/postscript.md), [TIFF](fileFormats/tiff.md) | [Image](dataTypes/image.md)
[TAR](fileFormats/tar.md) | ✅ | [`.tar`](extensions/tar.md) | [JSON](fileFormats/json.md), [SQL](fileFormats/sql.md), [XML](fileFormats/xml.md), [YAML](fileFormats/yaml.md) | [Data (container)](dataTypes/dataContainer.md)
[TeX](fileFormats/tex.md) | ⚠️ | [`.sty`](extensions/sty.md), [`.tex`](extensions/tex.md) | [CSS](fileFormats/css.md), [CSV](fileFormats/csv.md), [HTML](fileFormats/html.md), [JavaScript](fileFormats/javascript.md), [JSON](fileFormats/json.md), [JSX](fileFormats/jsx.md), [Markdown](fileFormats/markdown.md), [SGML](fileFormats/sgml.md), [SQL](fileFormats/sql.md), [Text](fileFormats/text.md), [XHTML](fileFormats/xhtml.md), [XML](fileFormats/xml.md), [XSLT](fileFormats/xslt.md), [YAML](fileFormats/yaml.md) | [Markup](dataTypes/markup.md), [Text (plain)](dataTypes/textPlain.md)
[Text](fileFormats/text.md) | ⚠️ | [`.cfg`](extensions/cfg.md), [`.ini`](extensions/ini.md), [`.log`](extensions/log.md), [`.lst`](extensions/lst.md), [`.text`](extensions/text.md), [`.txt`](extensions/txt.md) | [CSS](fileFormats/css.md), [CSV](fileFormats/csv.md), [HTML](fileFormats/html.md), [JSON](fileFormats/json.md), [Markdown](fileFormats/markdown.md), [SQL](fileFormats/sql.md), [TeX](fileFormats/tex.md), [XML](fileFormats/xml.md), [YAML](fileFormats/yaml.md) | [Text (plain)](dataTypes/textPlain.md)
[TIFF](fileFormats/tiff.md) | ✅ | [`.tif`](extensions/tif.md), [`.tiff`](extensions/tiff.md) | [GIF](fileFormats/gif.md), [JPEG](fileFormats/jpeg.md), [PDF](fileFormats/pdf.md), [PDF/A](fileFormats/pdfa.md), [PNG](fileFormats/png.md), [PostScript](fileFormats/postscript.md), [SVG](fileFormats/svg.md) | [Image](dataTypes/image.md)
[WOFF](fileFormats/woff.md) | ✅ | [`.woff`](extensions/woff.md) | [WOFF2](fileFormats/woff2.md) | [Font](dataTypes/font.md)
[WOFF2](fileFormats/woff2.md) | ✅ | [`.woff2`](extensions/woff2.md) | [WOFF](fileFormats/woff.md) | [Font](dataTypes/font.md)
[XHTML](fileFormats/xhtml.md) | ⚠️ | [`.htm`](extensions/htm.md), [`.html`](extensions/html.md) | [CSS](fileFormats/css.md), [HTML](fileFormats/html.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Markdown](fileFormats/markdown.md), [SGML](fileFormats/sgml.md), [TeX](fileFormats/tex.md), [XML](fileFormats/xml.md), [XSLT](fileFormats/xslt.md) | [Markup](dataTypes/markup.md)
[XLS](fileFormats/xls.md) | ❌ | [`.xls`](extensions/xls.md) | [ODS](fileFormats/ods.md), [XLSX](fileFormats/xlsx.md) | [Spreadsheet](dataTypes/spreadsheet.md)
[XLSX](fileFormats/xlsx.md) | ✅ | [`.xlsx`](extensions/xlsx.md) | [ODS](fileFormats/ods.md), [XLS](fileFormats/xls.md) | [Spreadsheet](dataTypes/spreadsheet.md)
[XML](fileFormats/xml.md) | ⚠️ | [`.xml`](extensions/xml.md) | [Access](fileFormats/access.md), [CSS](fileFormats/css.md), [CSV](fileFormats/csv.md), [dbase](fileFormats/dbase.md), [HDF5](fileFormats/hdf5.md), [HTML](fileFormats/html.md), [JavaScript](fileFormats/javascript.md), [JSON](fileFormats/json.md), [JSX](fileFormats/jsx.md), [Markdown](fileFormats/markdown.md), [SGML](fileFormats/sgml.md), [SIARD](fileFormats/siard.md), [SQL](fileFormats/sql.md), [TAR](fileFormats/tar.md), [TeX](fileFormats/tex.md), [Text](fileFormats/text.md), [XHTML](fileFormats/xhtml.md), [XSLT](fileFormats/xslt.md), [YAML](fileFormats/yaml.md) | [Data (container)](dataTypes/dataContainer.md), [Database](dataTypes/database.md), [Markup](dataTypes/markup.md), [Text (plain)](dataTypes/textPlain.md)
[XSLT](fileFormats/xslt.md) | ⚠️ | [`.xsl`](extensions/xsl.md), [`.xslt`](extensions/xslt.md) | [C](fileFormats/c.md), [CPP](fileFormats/cpp.md), [CSS](fileFormats/css.md), [HTML](fileFormats/html.md), [JAVA](fileFormats/java.md), [JavaScript](fileFormats/javascript.md), [JSX](fileFormats/jsx.md), [Markdown](fileFormats/markdown.md), [Pascal](fileFormats/pascal.md), [Perl](fileFormats/perl.md), [Prolog](fileFormats/prolog.md), [Python](fileFormats/python.md), [Ruby](fileFormats/ruby.md), [Scala](fileFormats/scala.md), [SGML](fileFormats/sgml.md), [TeX](fileFormats/tex.md), [XHTML](fileFormats/xhtml.md), [XML](fileFormats/xml.md) | [Markup](dataTypes/markup.md), [Program code](dataTypes/programCode.md)
[YAML](fileFormats/yaml.md) | ✅ | [`.yaml`](extensions/yaml.md) | [CSS](fileFormats/css.md), [CSV](fileFormats/csv.md), [HTML](fileFormats/html.md), [JSON](fileFormats/json.md), [Markdown](fileFormats/markdown.md), [SQL](fileFormats/sql.md), [TAR](fileFormats/tar.md), [TeX](fileFormats/tex.md), [Text](fileFormats/text.md), [XML](fileFormats/xml.md) | [Data (container)](dataTypes/dataContainer.md), [Text (plain)](dataTypes/textPlain.md)


??? caution "If you are reading an archived copy of these docs"
    If you browsing the raw files,
    [dataTypes]({{formats}}/tree/master/docs/dataTypes/)
    contains a collection of data types
    and
    [fileFormats]({{formats}}/tree/master/docs/fileFormats/)
    contains a collection of file formats.
    and
    [extensions]({{formats}}/tree/master/docs/extensions/)
    contains a collection of file extensions.

    All the content is preserved, but the formatting is just done
    by means of white space and by using [Markdown](fileFormats/markdown.md) formatting.



