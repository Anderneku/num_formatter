from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='number_formatter',
    version='0.1',
    long_description=long_description,
    description="Add comma separation to your larger numbers!",
    long_description_content_type="text/markdown",
    author="SiXFeet",
    author_email='chukunekunwanwene@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=['number_formatter'],
    keywords='number formatter',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
