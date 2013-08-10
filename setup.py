#!/usr/bin/env python
# flake8: noqa

from setuptools import setup
from setuptools.command.test import test as TestCommand

# get version
with open('memsql/__init__.py') as f:
    exec(f.read())

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest, sys
        errno = pytest.main(self.test_args)
        raise sys.exit(errno)

setup(
    name='memsql',
    version=__version__,    # this is defined by the "exec(f.read())" at the top of this file.
    author='MemSQL',
    author_email='support@memsql.com',
    url='http://github.com/memsql/memsql-python',

    license='LICENSE.txt',
    description='Useful utilities and plugins for MemSQL integration.',
    long_description=open('README.rst').read(),

    packages=[
        'memsql',
        'memsql.collectd',
        'memsql.common',
    ],
    install_requires=['ordereddict', 'MySQL-python>=1.2.4', 'wraptor'],
    tests_require=['pytest', 'mock'],
    cmdclass={ 'test': PyTest },
)
