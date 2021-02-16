import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="명이",  # Replace with your own username
    version="1.0.0",
    author="명이",
    author_email="aiden080605@gmail.com",
    description="Minecraft Server Setup Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myoung2namur/MCServerLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
