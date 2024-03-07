import setuptools


with open("README.md", "r", encoding="utf-8") as f:## it gives the description of your project
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "cnnClassifier" # from git hub repository
AUTHOR_USER_NAME = "Subash7Lingden" ## gitHub username
SRC_REPO = "cnnClassifier" # from src folder
AUTHO_EMAIL = "subashsubbalingden@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author = AUTHOR_USER_NAME,
    author_email=AUTHO_EMAIL,
    description= "A small python package for CNN app",
    long_description="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)