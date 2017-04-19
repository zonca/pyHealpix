AC_INIT([pyHealpix], [0.1],,[pyHealpix],)
AM_INIT_AUTOMAKE([foreign subdir-objects -Wall -Werror])
AM_MAINTAINER_MODE([enable])

dnl Needed for linking on Windows.
dnl Protect with m4_ifdef because AM_PROG_AR is required in
dnl autoconf >= 1.12 when using -Wall, but the macro is
dnl absent in old versions of autoconf.
m4_ifdef([AM_PROG_AR], [AM_PROG_AR])

LT_INIT([disable-static])
AC_CONFIG_MACRO_DIR([m4])

dnl Enable silent build rules if this version of Automake supports them
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

dnl locate python and python-config
AM_PATH_PYTHON
AC_ARG_VAR([PYTHON_CONFIG], [Path to python-config])
AS_IF([test -z "$PYTHON_CONFIG"], [
  AC_PATH_PROGS([PYTHON_CONFIG],
                [python$PYTHON_VERSION-config python-config],
                [no],
                [`dirname $PYTHON`])
  AS_IF([test "$PYTHON_CONFIG" = no], [AC_MSG_ERROR([cannot find python-config for $PYTHON.])])
])
AC_MSG_CHECKING([python include flags])
PYTHON_INCLUDE=`$PYTHON_CONFIG --includes`
AC_MSG_RESULT([$PYTHON_INCLUDE])
AC_MSG_CHECKING([python linker flags])
PYTHON_LDFLAGS=`$PYTHON_CONFIG --ldflags`
AC_MSG_RESULT([$PYTHON_LDFLAGS])

dnl Introduce --enable-native-optimizations command line argument to turn on
dnl -march=native compiler flag, disabled by default.
AC_ARG_ENABLE(
    [native-optimizations],
    [AS_HELP_STRING([--enable-native-optimizations], [Enable non-portable optimizations for your own CPU by compiling with -march=native @<:@default=no@:>@])]
)

AC_PROG_CC_C99
: ${enable_openmp=no}
AC_OPENMP
CPPFLAGS="$CPPFLAGS $OPENMP_CFLAGS"
CFLAGS="$CFLAGS $OPENMP_CFLAGS"
LDFLAGS="$LDFLAGS $OPENMP_CFLAGS"
AS_IF(
    [test "x$enable_native_optimizations" = "xyes"],
    [AX_CHECK_COMPILE_FLAG([-march=native],[CC="$CC -march=native"])],
)

AX_CHECK_COMPILE_FLAG([-fvisibility=hidden],[CFLAGS="$CFLAGS -fvisibility=hidden"])
AX_CHECK_COMPILE_FLAG([-O3],[CFLAGS="$CFLAGS -O3"])
AX_CHECK_COMPILE_FLAG([-ffast-math],[CFLAGS="$CFLAGS -ffast-math"])
AX_CHECK_COMPILE_FLAG([-ffunction-sections -fdata-sections],[CFLAGS="$CFLAGS -ffunction-sections -fdata-sections"])
dnl AX_CHECK_COMPILE_FLAG([-flto],[CFLAGS="$CFLAGS -flto"])

AC_PROG_CXX
AC_LANG_PUSH([C++])
AX_CXX_COMPILE_STDCXX([14], [noext], [mandatory])
AC_OPENMP
CXXFLAGS="$CXXFLAGS $OPENMP_CXXFLAGS"
LDFLAGS="$LDFLAGS $OPENMP_CXXFLAGS"
AS_IF(
    [test "x$enable_native_optimizations" = "xyes"],
    [AX_CHECK_COMPILE_FLAG([-march=native],[CXX="$CXX -march=native"])],
)
CXXFLAGS="$CXXFLAGS $PYTHON_INCLUDE"
LDFLAGS="$LDFLAGS $PYTHON_LDFLAGS"

AX_CHECK_COMPILE_FLAG([-fvisibility=hidden],[CXXFLAGS="$CXXFLAGS -fvisibility=hidden"])
AX_CHECK_COMPILE_FLAG([-O3],[CXXFLAGS="$CXXFLAGS -O3"])
AX_CHECK_COMPILE_FLAG([-ffast-math],[CXXFLAGS="$CXXFLAGS -ffast-math"])
AX_CHECK_COMPILE_FLAG([-ffunction-sections -fdata-sections],[CXXFLAGS="$CXXFLAGS -ffunction-sections -fdata-sections"])
AX_CHECK_LINK_FLAG([-Wl,-gc-sections],[LDFLAGS="$LDFLAGS -Wl,-gc-sections"])
dnl AX_CHECK_COMPILE_FLAG([-flto],[CXXFLAGS="$CXXFLAGS -flto"])

AC_PROG_LIBTOOL
gl_LINKER_SCRIPT
dnl Create pkgconfig .pc file.
AX_CREATE_PKGCONFIG_INFO(,,,,[$OPENMP_CFLAGS])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
