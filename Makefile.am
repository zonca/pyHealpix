ACLOCAL_AMFLAGS = -I m4

pyexec_LTLIBRARIES = pyHealpix.la

src_c_utils = \
  c_utils/c_utils.c \
  c_utils/c_utils.h \
  c_utils/walltime_c.c \
  c_utils/walltime_c.h \
  c_utils/trig_utils.c \
  c_utils/trig_utils.h
src_libfftpack = \
  libfftpack/bluestein.h \
  libfftpack/bluestein.c \
  libfftpack/fftpack.h \
  libfftpack/fftpack.c \
  libfftpack/ls_fft.h \
  libfftpack/ls_fft.c
src_libsharp = \
  libsharp/sharp.c \
  libsharp/sharp.h \
  libsharp/sharp_cxx.h \
  libsharp/sharp_almhelpers.c \
  libsharp/sharp_almhelpers.h \
  libsharp/sharp_complex_hacks.h \
  libsharp/sharp_core.c \
  libsharp/sharp_core.h \
  libsharp/sharp_geomhelpers.c \
  libsharp/sharp_geomhelpers.h \
  libsharp/sharp_internal.h \
  libsharp/sharp_lowlevel.h \
  libsharp/sharp_vecsupport.h \
  libsharp/sharp_vecutil.h \
  libsharp/sharp_ylmgen_c.c \
  libsharp/sharp_ylmgen_c.h \
  libsharp/sharp_legendre_roots.c \
  libsharp/sharp_legendre_roots.h
src_cxxsupport = \
  cxxsupport/geom_utils.cc \
  cxxsupport/string_utils.cc \
  cxxsupport/pointing.cc \
  cxxsupport/rotmatrix.cc \
  cxxsupport/wigner.cc \
  cxxsupport/error_handling.cc \
  cxxsupport/alloc_utils.h \
  cxxsupport/arr.h \
  cxxsupport/datatypes.h \
  cxxsupport/error_handling.h \
  cxxsupport/geom_utils.h \
  cxxsupport/lsconstants.h \
  cxxsupport/math_utils.h \
  cxxsupport/openmp_support.h \
  cxxsupport/planck_rng.h \
  cxxsupport/pointing.h \
  cxxsupport/rangeset.h \
  cxxsupport/rotmatrix.h \
  cxxsupport/share_utils.h \
  cxxsupport/sse_utils_cxx.h \
  cxxsupport/string_utils.h \
  cxxsupport/vec3.h \
  cxxsupport/wigner.h \
  cxxsupport/xcomplex.h \
  cxxsupport/sort_utils.h
src_healpix_cxx= \
  Healpix_cxx/alm.cc \
  Healpix_cxx/alm.h \
  Healpix_cxx/alm_healpix_tools.cc \
  Healpix_cxx/alm_healpix_tools.h \
  Healpix_cxx/alm_powspec_tools.cc \
  Healpix_cxx/alm_powspec_tools.h \
  Healpix_cxx/healpix_tables.cc \
  Healpix_cxx/healpix_tables.h \
  Healpix_cxx/healpix_base.cc \
  Healpix_cxx/healpix_base.h \
  Healpix_cxx/healpix_map.cc \
  Healpix_cxx/healpix_map.h \
  Healpix_cxx/powspec.cc \
  Healpix_cxx/powspec.h
src_pyhealpix = \
  pyHealpix.cc \
  pybind11/attr.h \
  pybind11/cast.h \
  pybind11/class_support.h \
  pybind11/common.h \
  pybind11/complex.h \
  pybind11/descr.h \
  pybind11/numpy.h \
  pybind11/options.h \
  pybind11/pybind11.h \
  pybind11/pytypes.h \
  pybind11/typeid.h

EXTRA_DIST = \
  COPYING \
  pybind11/LICENSE \
  libfftpack/fftpack_inc.c \
  libsharp/sharp_core_inc.c \
  libsharp/sharp_core_inc2.c \
  libsharp/sharp_core_inchelper.c \
  exports.version \
  tests/pyHealpix_test.py \
  tests/pyHealpix_perftest.py \
  tests/testscript.sh \
  compile_and_install.sh

#TESTS=tests/testscript.sh

pyHealpix_la_SOURCES = $(src_pyhealpix) $(src_c_utils) $(src_libfftpack) $(src_libsharp) $(src_cxxsupport) $(src_healpix_cxx)
pyHealpix_la_LDFLAGS= -module -avoid-version -shared
AM_CPPFLAGS = -I$(top_srcdir)/c_utils -I$(top_srcdir)/libfftpack -I$(top_srcdir)/libsharp -I$(top_srcdir)/cxxsupport -I$(top_srcdir)/Healpix_cxx

if HAVE_LD_VERSION_SCRIPT
pyHealpix_la_LDFLAGS += -Wl,--version-script=$(top_srcdir)/exports.version
endif

pkgconfigdir = $(libdir)/pkgconfig
nodist_pkgconfig_DATA = @PACKAGE_NAME@.pc

DISTCLEANFILES=@PACKAGE_NAME@.pc @PACKAGE_NAME@.pc.in  @PACKAGE_NAME@-uninstalled.pc  @PACKAGE_NAME@-uninstalled.sh
