from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.3'
DESCRIPTION = 'An easy way to lookup APIs.'
LONG_DESCRIPTION = 'A package that makes API requests much easier.'

email_address = "<coding.wizard4[at]gmail.com>"

# Setting up
setup(
    name="apilookup",
    version=VERSION,
    author="Hamdi Vazim",
    author_email=email_address.replace("[at]", "@"),
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api', 'apicalls', 'requests', 'json', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)