import setuptools
from __version__ import __version__

IMAGE_FILES = ["/resources/images/icon.ico"]

setuptools.setup(
    name="ankipythia",
    version=__version__,
    author="1898Angelo",
    description="Barebones flashcard app insipired by Anki -- https://apps.ankiweb.net/",
    license="GPL",
    install_requires=[
        'customtkinter>=5.1.3',
        'platformdirs>=2.6.2'
    ],
    data_files=[
        ("resources/images", IMAGE_FILES)
    ],
    url="https://github.com/1898Angelo",
    packages=setuptools.find_packages(),
    classifiers = [
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Framework :: customtkinter"]
)
