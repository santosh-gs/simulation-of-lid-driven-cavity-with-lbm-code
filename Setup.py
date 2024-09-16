from setuptools import Extension, setup
from Cython.Build import cythonize
from Cython.Compiler import Options
import numpy

extensions = [Extension(
                "LBM_Cython",
                sources=["LBM_Cython.pyx"],
                extra_compile_args=["/openmp"],
                extra_link_args=["/openmp"]
            )]

setup(
    ext_modules = cythonize(extensions, compiler_directives={'boundscheck': False, 'cdivision': False}, annotate = True, language_level = 3), include_dirs=[numpy.get_include()]
)

# # python setup.py build_ext --inplace