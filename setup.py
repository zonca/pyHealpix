from setuptools import setup, Extension, Distribution
import setuptools.command.build_ext

import sys
import sysconfig
import os
import os.path
import distutils.sysconfig
import itertools
from glob import iglob


def _get_sharp_libname():
    builder = setuptools.command.build_ext.build_ext(Distribution())
    full_name = builder.get_ext_filename('libsharp')
    without_lib = full_name.split('lib', 1)[-1]
    without_so = without_lib.rsplit('.so', 1)[0]
    return without_so


def _get_distutils_build_directory():
    """
    Returns the directory distutils uses to build its files.
    We need this directory since we build extensions which have to link
    other ones.
    """
    pattern = "lib.{platform}-{major}.{minor}"
    return os.path.join('build', pattern.format(platform=sysconfig.get_platform(),
                                                major=sys.version_info[0],
                                                minor=sys.version_info[1]))

class _deferred_pybind11_include(object):
    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        return pybind11.get_include(self.user)

def _strip_inc(input):
    res = []
    for i in input:
        if ("inc.c" not in i) and ("inc2.c" not in i) and \
           ("inchelper.c" not in i):
            res.append(i)
    return res


def _get_cc_files(directory):
    path = directory
    iterable_sources = (iglob(os.path.join(root, '*.cc'))
                        for root, dirs, files in os.walk(path))
    source_files = itertools.chain.from_iterable(iterable_sources)
    return list(source_files)


def _get_c_files(directory):
    path = directory
    iterable_sources = (iglob(os.path.join(root, '*.c'))
                        for root, dirs, files in os.walk(path))
    source_files = itertools.chain.from_iterable(iterable_sources)
    return _strip_inc(list(source_files))


def _remove_strict_prototype_option_from_distutils_config():
    strict_prototypes = '-Wstrict-prototypes'
    config = distutils.sysconfig.get_config_vars()
    for key, value in config.items():
        if strict_prototypes in str(value):
            config[key] = config[key].replace(strict_prototypes, '')

_remove_strict_prototype_option_from_distutils_config()

extra_compile_args = ['-fopenmp', '-march=native']
extra_cc_compile_args = []
include_dirs = ['c_utils/', 'libfftpack/', 'libsharp/', 'cxxsupport',
                'Healpix_cxx', _deferred_pybind11_include(),
                _deferred_pybind11_include(True)]

library_dirs = [_get_distutils_build_directory()]
python_module_link_args = []
base_library_link_args = []

if sys.platform == 'darwin':
    extra_cc_compile_args.append('--std=c++14')
    extra_cc_compile_args.append('--stdlib=libc++')
    extra_compile_args.append('-mmacosx-version-min=10.9')

    vars = distutils.sysconfig.get_config_vars()
    vars['LDSHARED'] = vars['LDSHARED'].replace('-bundle', '')
    python_module_link_args.append('-bundle')
    builder = setuptools.command.build_ext.build_ext(Distribution())
    full_name = builder.get_ext_filename('libsharp')
    base_library_link_args.append(
                   '-Wl,-dylib_install_name,@loader_path/{}'.format(full_name))
    base_library_link_args.append('-dynamiclib')
else:
    extra_cc_compile_args.append('--std=c++14')
    python_module_link_args.append("-Wl,-rpath,$ORIGIN")

extra_cc_compile_args = extra_compile_args + extra_cc_compile_args


def get_extension_modules():
    extension_modules = []

    """
    Extension module which is actually a plain C library without Python
    bindings
    """
    sharp_sources = _get_c_files('c_utils') + _get_c_files('libfftpack') + \
        _get_c_files('libsharp')
    sharp_library = Extension('libsharp',
                              sources=sharp_sources,
                              include_dirs=include_dirs,
                              extra_compile_args=extra_compile_args,
                              extra_link_args=base_library_link_args,
                              libraries=[],
                              library_dirs=library_dirs)
    sharp_libs = [_get_sharp_libname()]
    extension_modules.append(sharp_library)

    """
    Healpix C++ and Python bindings
    """
    pyhealpix_sources = _get_cc_files('.')
    pyhealpix_library = Extension('pyHealpix',
                                  sources=pyhealpix_sources,
                                  include_dirs=include_dirs,
                                  extra_compile_args=extra_cc_compile_args,
                                  libraries=['gomp']+sharp_libs,
                                  extra_link_args=python_module_link_args,
                                  library_dirs=library_dirs)
    extension_modules.append(pyhealpix_library)

    return extension_modules


setup(name='pyHealpix',
      version='0.0.1',
      description='Python bindings for some HEALPix C++ functionality',
      include_package_data=True,
      author='Martin Reinecke',
      author_email='martin@mpa-garching.mpg.de',
      packages=[],
      extras_require={'numpy': 'numpy>=1.10.4', 'pybind11': 'pybind11>=2.2.0'},
      ext_modules=get_extension_modules(),
      install_requires=['pybind11>=2.2.0']
      )
