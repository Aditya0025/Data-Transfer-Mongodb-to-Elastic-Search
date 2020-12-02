import pathlib
from setuptools import setup

# the Directory containing this file
HERE = pathlib.Path(__file__).parent

with open("README.md","r") as fh:
    long_description = fh.read()


#this call to setup() does all the work
setup(
    name="Mongodb-to-Elastic-Search",
    version = "1.0.0",
    description = "Data Transfer from mongodb to Elastic search",
    long_description = long_description,
    long_description_content_type = "py/markdown",
    url = "https://github.com/Aditya0025/Data-Transfer-Mongodb-to-Elastic-Search",
    author="Aditya",
    author_email="aditya0025@yahoo.com",
    license="MIT",
    classifiers=[
        
        "License :: OSI Approved :: MIT License",
        "Programing Language :: Python ::3",        
    ],
    packages=["Data Transfer"],
    include_package_data = True,
    install_requires=["feedparser","html2text"],
    enry_points = {"console_scripts":[
        "mongo_to_elastic_search = reader.__main__:main",
    ]
    },
)
