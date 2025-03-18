import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
print(long_description)

__version__ = "0.0.3"

REPO_NAME="E2E-Wine-Quality-project"
AUTHOR_USER_NAME="sundar-nallalagappan"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "nsundar.1990@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)