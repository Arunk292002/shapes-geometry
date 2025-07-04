import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shapes-geometry",  # Use hyphen for PyPI name if you published with that
    version="0.1.1",  # Make sure this is updated from previous upload
    author="Arunkumar",
    author_email="arun5412ten@gmail.com",
    description="Functions to calculate geometric properties of 2D and 3D shapes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
    ],
    python_requires=">=3.6",
    keywords="geometry shapes math area volume 2D 3D",
    repository="https://github.com/Arunk292002/shapes-geometry"
)
