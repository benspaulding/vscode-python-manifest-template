#!/usr/bin/env python
import glob
import os.path

from setuptools import find_packages, setup  # type: ignore

SRC = "src"


setup(
    include_package_data=True,
    package_dir={"": SRC},
    packages=find_packages(SRC),
    py_modules=[
        os.path.splitext(os.path.basename(path))[0]
        for path in glob.iglob(f"{SRC}/*.py")
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
