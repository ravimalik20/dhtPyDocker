# DISTRIBUTED HASH TABLE using Python and Docker

This is an implementation of a Distributed Hash Table based on the Chord Ring
design. Distributed System is emulated using Docker containers. Currently, all
the data is in-memory, but future plans are to make it persistent.

## Architecture

Core and the storage layer is separated from each other. Storage layer is
responsible for saving the data. Core is responsible for providing an interface
on top of the storage and also make adequate network communication to store and
fetch data from a node.
