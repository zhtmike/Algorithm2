from distutils.core import setup

from Cython.Build import cythonize

setup(
    name='Union Finder',
    ext_modules=cythonize('cython_module/union_find.pyx'),
)
