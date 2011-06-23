#!/usr/bin/env python

try:
    import ez_setup

    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = ""
LONG_DESCRIPTION = """
"""

setup(name='pyhar',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author="Flier Lu",
      author_email="flier.lu@gmail.com",
      packages=find_packages(exclude=['ez_setup']),
      platforms=['any'],
      test_suite="pyhar.tests.all_tests_suite",
      zip_safe=True,
    )