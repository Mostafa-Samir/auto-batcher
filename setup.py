import setuptools

with open("README.md", encoding="utf-8") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setuptools.setup(
    name="auto-batcher",
    version="0.1.0",
    author="Mostafa Samir",
    author_email="mostafa.3210@gmail.com",
    description="A lightweight library to scale your ML model deployment",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Mostafa-Samir/auto-batcher",
    project_urls={
        "Bug Tracker": "https://github.com/Mostafa-Samir/auto-batcher/issues",
    },
    packages=["auto_batcher"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)