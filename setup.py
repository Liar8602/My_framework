import setuptools

with open("README.md", "r") as file:
    description = file.read()

setuptools.setup(
    name="My framework",
    version="dev",
    author="Rail Bagautdinov",
    author_email="rail.bagautdinov.92@gmail.com",
    description=description,
    description_content_type="text/markdown",
    url="https://github.com/Liar8602/my_framework",
    py_modules={'wsgi'},
    packages=setuptools.find_packages(),
    install_requires=['Jinja2==3.0.1'],
    license="MIT",
)