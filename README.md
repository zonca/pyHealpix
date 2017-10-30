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

- no library dependencies, all required code is contained in the package
- for building, a modern C++ compiler is required (successfully tested with
  g++ 5.4 clang 4.0 and Intel icpc 17.0)

### System-wide installation

-   Install dependencies for building:

        sudo apt-get install g++ git python

-   Install pyHealpix:

        git clone https://gitlab.mpcdf.mpg.de/ift/pyHealpix.git -b setuptools_test
        (cd pyHealpix && python setup.py install)

### Local installation for a single user

-   Install dependencies for building:

        sudo apt-get install g++ git python

-   Install pyHealpix:

        git clone https://gitlab.mpcdf.mpg.de/ift/pyHealpix.git -b setuptools_test
        (cd pyHealpix && python setup.py install --user)
