from distutils.core import setup, Extension

setup(name='unionFinder', version='1.0', ext_modules=[Extension('unionFinder', ['union_find.c'])])
