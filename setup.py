from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("trade_types", ["./trade_types.pyx"]),
]

setup(
    name="tradebot",
    ext_modules=cythonize(extensions, language_level="3"),
)
