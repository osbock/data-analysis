from setuptools import setup, find_packages

setup(
    name= 'data_analysis',
    version = '0.0.1',
    url= 'www.github.com/osbock/data-analysis',
    author='Kevin Osborn',
    packages=find_packages(),
    install_requires =['PyQt5',
                       'pandas',
                       'sqlalchemy',
                       'nltk',
                       'numpy',
                       'jupyter',
                       'python-twitter'],
    entry_points={},
    extras_require={'dev':['flake8',]},
    )
