from setuptools import setup, find_packages
import sys, os

requirements = []
with open('requirements.txt', 'r') as fh:
    for line in fh:
        requirements.append(line.strip())

readme = open('README.md').read()

setup(
    name="rnastructure_wrapper",
    version='0.0.0',
    long_description=readme,
    packages=find_packages(),
    package_dir={'rnastructure_wrapper': 'rnastructure_wrapper'},
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.10",
)
