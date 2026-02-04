from setuptools import find_packages,setup

setup(
    name="e-commerce-bot",
    version="0.0.1",
    author="ajith narayanan",
    author_email="ajithnarayananka@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain'])