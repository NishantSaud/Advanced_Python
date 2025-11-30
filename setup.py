from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([
        "reverse_string.pyx",
        "dot_product.pyx",
        "sum_of_squares.pyx"
    ])
)
