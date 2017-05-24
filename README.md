pyHealpix - minimalistic Python interface for Healpix C++
=========================================================

Summary
-------

### Description

This library tries to provide Python bindings for the most important
functionality in Healpix C++. The design goals are
- similarity to the C++ interface (while respecting some Python peculiarities)
- simplicity (no optional function parameters)
- low function calling overhead

The package is implemented purely in C++, making use of the pybind11 package
(https://github.com/pybind/pybind11). It can be compiled for both Python 2 and
3.


Installation
------------

### Requirements

- no external dependencies, all required code is contained in the package
- for building, a modern C++ compiler is required (successfully tested with
  g++ 5.4 clang 4.0 and Intel icpc 17.0)
- for building from the Git repository, GNU autotools are required

### System-wide installation

-   Install dependencies for building:

        sudo apt-get install g++ autoconf libtool git

-   Install pyHealpix:

        git clone https://gitlab.mpcdf.mpg.de/ift/pyHealpix.git
        (cd pyHealpix && autoreconf -i && ./configure --enable-openmp --enable-native-optimizations && make -j4 && sudo make install)

### Local installation for a single user

-   Install dependencies for building:

        sudo apt-get install g++ autoconf libtool git

-   Install pyHealpix:

        git clone https://gitlab.mpcdf.mpg.de/ift/pyHealpix.git
        (cd pyHealpix && autoreconf -i && ./configure --prefix=$HOME/.local --enable-openmp --enable-native-optimizations && make -j4 install)

### Installation on OS X

-   Install pyHealpix:

        git clone https://gitlab.mpcdf.mpg.de/ift/pyHealpix.git
        (cd pyHealpix && autoreconf -i && ./configure --prefix=`python-config --prefix` --enable-openmp --enable-native-optimizations && make -j4 && sudo make install)

    (The last command installs the package system-wide. User-specific
    installation would be preferrable, but we haven't found a simple recipe yet
    how to determine the installation prefix ...)
