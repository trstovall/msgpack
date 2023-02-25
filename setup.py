
from setuptools import setup, find_packages, Extension


_mpack = Extension(
    name="mpack",
    sources=["mpackmodule.c"],
)

setup(
    name="mpack",
    version="0.0.1",
    description="short description",
    long_description="long description",
    packages=find_packages(where="."),
    python_requires=">=3.10, <4",
    ext_modules=[_mpack]
)
