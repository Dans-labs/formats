# Description

HDF (version 5, not compatible with earlier versions) is a
common dataset format with the ability to store data in multidimensional arrays,
grouped into collections and/or hierarchies. Relationships between data in the
arrays can be saved, but the format does not allow for storing structured
(descriptive) metadata.

# Recommendation

The format is open and can be read in a variety of
applications, but it is very difficult to process without the use of HDF5
software.

Use one of the tools on
[HDF Group Support (legacy)]({{hdf5tools}})
to convert data to [=sql] or [=csv].
