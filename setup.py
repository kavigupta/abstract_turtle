import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abstract_turtle", # Replace with your own username
    version="0.2.0",
    author="Kavi Gupta",
    author_email="abstract_turtle@kavigupta.org",
    description="Reimplementation of the builtin turtle module that allows for arbitrary backends.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kavigupta/abstract_turtle",
    download_url="https://github.com/kavigupta/abstract_turtle/archive/0.2.0.zip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[],
    extras_require={
        "pillow_canvas" : ["numpy==1.18.0", "Pillow==6.2.1"]
    }
)
