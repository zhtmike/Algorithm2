from distutils.core import setup

from Cython.Build import cythonize

setup(
    name='Union Finder',
    ext_modules=cythonize('union_finder.pyx'),
)
