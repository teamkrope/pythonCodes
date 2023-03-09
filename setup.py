from setuptools import setup, find_packages

setup(
    name="pythonProjects",
    author="Huzaifa Asim",
    maintainer="HunerOn Codes",
    maintainer_email="toyoureply@gmail.com",
    description="A collection of simple and good Python projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/huneron/pythonProjects",
    packages=find_packages(),
    install_requires=[
        "qrcode",
        "tk",
        "Pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License 2.0",
        "Operating System :: OS Independent :: Windows Recommended",
    ],
    python_requires=">=3.6",
)
