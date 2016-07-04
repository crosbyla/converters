from setuptools import setup, find_packages
setup(
    name = "citeproc-preprocess",
    version = "1.0",
    packages = ['citeproc_preprocess'],
    entry_points = {'console_scripts': ['citeproc-preprocess=citeproc_preprocess.citeproc_preprocess:main'] },

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },

    # metadata for upload to PyPI
    author = "Lawrence Crosby",
    author_email = "crosbyla@u.northwestern.edu",
    description = "Python module for parsing markdown citation keys",
    license = "MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License (MIT)'
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Visualization'],
    # List of classifiers:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    # could also include long_description, download_url, classifiers, etc.
)
