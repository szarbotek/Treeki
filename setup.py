from setuptools import setup, find_packages

setup(
    name="Treeki",  # nazwa pakietu (unikalna na PyPI)
    version="0.1.0",  # wersja pakietu
    author="szarbotek",  # autor
    author_email="szarbotek.dev@gamil.com",  # email kontaktowy
    description="A simple library for managing tree structures",  # krótki opis
    long_description=open("README.md").read(),  # długi opis (z pliku README.md)
    long_description_content_type="text/markdown",  # format README.md
    url="https://github.com/szarbotek/Treeki",  # link do repozytorium
    packages=find_packages(),  # automatycznie znajdź pakiety
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # wymagana wersja Pythona
)