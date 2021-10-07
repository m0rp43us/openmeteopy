import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name = "openmeteo_py",
    version = "0.0.1",
    author = "Wail Chalabi",
    author_email = "wail.agroconcept@gmail.com",
    description = "Download Meteorological Data from OPEN-METEO API (https://open-meteo.com/en/)",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/m0rp43us/openmeteopy",
    packages = setuptools.find_packages(),
    license="GNU General Public License v3 or later (GPLv3+)",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    install_requires=required,
)
