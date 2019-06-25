# Data (container)

## Description

Structured data needs a concept of *container* to hold the structure
by which various items of data are kept together.

Think of parts and wholes, files and directories, text and markup.

Data containers are a generic concept. They can be used for a variety
of purposes, which may overlap with other data types, such as formatted
text.

Often, data containers are just plain text files that adhere to a defined
scheme that gives structure to their contents.

## Representations

There are several data container methods, such as

*   [TAR](../fileFormats/tar.md):
    a long standing, ubiquitous way of storing files and folders
*   [XML](../fileFormats/xml.md):
    a fine-grained way to store records and fields, but also 
    elements and sub-elements. It is used for 
    [databases](database.md) as well as formatted text.
*   [JSON](../fileFormats/json.md):
    a fine-grained way to store lists and mappings, recursively nested.
    It is used for generic data exchange, especially between web clients and web servers.
    It is lighter-weight than XML.
*   [YAML](../fileFormats/yaml.md):
    a fine-grained way to store lists and mappings, recursively nested.
    It is to configuration files what [Markdown](../fileFormats/markdown.md) is
    to [formatted text](formattedText.md).

## See also

[Database](database.md), [Formatted text](formattedText.md).
