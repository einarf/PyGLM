"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension
# To use a consistent encoding
from codecs import open
from os import path

module1 = Extension('glm',
                    sources = ['pyglm.c'])

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description_list = f.readlines()

    long_description = ""

    for line in long_description_list:
        long_description += line
    long_description = long_description.replace("\r", "")

setup(
    name='PyGLM',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.4.8b1',

    description='OpenGL Mathematics library for Python',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Zuzu-Typ/PyGLM',

    # Author details
    author='Zuzu_Typ',
    author_email="zuzu.typ@gmail.com",

    # Choose your license
    license='zlib/libpng license',

##    install_requires=[],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: zlib/libpng License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        "Operating System :: OS Independent",
        "Operating System :: MacOS",
        'Topic :: Software Development :: Libraries'
        
    ],

    # What does your project relate to?
    keywords='GLM OpenGL matrix vector vec mat Mathematics 3D python python2 python3 2 3 library python-c-api c-api math-library pip pypi matrix-manipulation matrix-multiplication matrix-functions quaternion c glsl',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages={},#find_packages(exclude=['contrib', 'docs', 'tests'],include=["*.h"]),

##    package_data={
##        "":["*.h"]
##        },

    platforms = ["Windows", "Linux", "MacOS"],
    
    include_package_data=True,

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #py_modules=["glm"],

    ext_modules = [module1],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
)
