import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("requirements.txt") as fin:
    REQUIRED_PACKAGES = fin.read()

setuptools.setup(
    name="vdldraw",
    version="0.1.5",
    author="geoyee",
    author_email="geoyee@yeah.net",
    description="Batch plot the log files exported from VisualDL using Matplotlib.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/geoyee/VDLdraw",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License"
    ],
)