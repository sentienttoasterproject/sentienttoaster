import os
from setuptools import setup
from nvpy import nvpy

setup(
    name = "sentienttoaster",
    version = "1.0",
    author = "",
    author_email = "",
    description = "Simple rock paper scissors guesser with a bit of randomness",
    license = "",
    url = "https://github.com/sentienttoasterproject/sentienttoaster",
    packages=['sentienttoaster'],
    entry_points = {
        'gui_scripts' : ['sentienttoaster = sentienttoaster.sentienttoaster:main']
    },
    data_files = [
        ('share/applications/', ['vxlabs-myscript.desktop'])
    ],
    classifiers=[
        "",
    ],
)
