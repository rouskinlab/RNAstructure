from setuptools import setup, find_packages
import sys, os

readme = open('README.md').read()

setup(
    name="rnastructure_wrapper",
    version='0.0.0',
    long_description=readme,
    packages=find_packages(),
    package_dir={'rnastructure_wrapper': 'rnastructure_wrapper'},
    include_package_data=True,
    install_requires=['numpy'],
    python_requires=">=3.10",
)
