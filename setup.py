"""
Configuration for package installation
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="contact-manager-pro",
    version="1.0.0",
    author="zourgani",
    author_email="zourgani.achraf@gmail.com",
    description="Professional contact management system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zourgani/ContactManagerPro",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rich>=13.0.0",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "contacts=contact_manager.main:main",
        ],
    },
)