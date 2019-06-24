<img src="../images/formats.png" width="100" align="right"/>
<img src="../images/DANS.png" width="200" align="right"/>

# HDF5

## Extensions

`.hdf5`

## Preferred status

No.

### Recommendation

The format is open and can be read in a variety of
applications, but it is very difficult to process without the use of HDF5
software.

Use one of the tools on
[HDF Group Support (legacy)](https://support.hdfgroup.org/products/hdf5_tools/)
to convert data to [SQL](sql.md) or [CSV](csv.md).

## Description

[Hierarchical Data Format (HDF5)](https://en.wikipedia.org/wiki/Hierarchical_Data_Format)
(version 5, not compatible with earlier versions) is a
common dataset format with the ability to store data in multidimensional arrays,
grouped into collections and/or hierarchies. Relationships between data in the
arrays can be saved, but the format does not allow for storing structured
(descriptive) metadata.

