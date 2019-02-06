# pylint: disable=missing-docstring
import setuptools

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name="ballgame-eduardomezencio",
    version="0.0.1",
    author="Eduardo Mezêncio",
    author_email="eduardomezencio@protonmail.com",
    description="A simple game",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/eduardomezencio/ballgame",
    packages=setuptools.find_packages(),
    classifiers=[
        'Intended Audience :: Education',
        'Topic :: Games/Entertainment'
    ],
)
