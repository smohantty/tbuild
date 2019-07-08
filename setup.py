#!/usr/bin/env python3

import sys

if sys.version_info < (3, 5, 0):
    print('Tried to install with an unsupported version of Python. '
          'cbuild requires Python 3.5.0 or greater')
    sys.exit(1)

from setuptools import setup

# On windows, will create Scripts/meson.exe and Scripts/meson-script.py
# Other platforms will create bin/meson
entries = {'console_scripts': ['cbuild=crossbuild.crossbuildmain:main']}
packages = ['crossbuild',
           ]

if __name__ == '__main__':
    setup(name='cbuild',
          version=0.1,
          description='A high performance build system',
          author='Subhransu Mohanty',
          author_email='smohantty@gmail.com',
          url='http://mesonbuild.com',
          license=' Apache License, Version 2.0',
          python_requires='>=3.5',
          packages=packages,
          entry_points=entries,
          classifiers=['Development Status :: 5 - Production/Stable',
                       'Environment :: Console',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: Apache Software License',
                       'Natural Language :: English',
                       'Operating System :: MacOS :: MacOS X',
                       'Operating System :: Microsoft :: Windows',
                       'Operating System :: POSIX :: BSD',
                       'Operating System :: POSIX :: Linux',
                       'Programming Language :: Python :: 3 :: Only',
                       'Topic :: Software Development :: Build Tools',
                       ],
          long_description='''Meson is a cross-platform build system designed to be both as
    fast and as user friendly as possible. It supports many languages and compilers, including
    GCC, Clang and Visual Studio. Its build definitions are written in a simple non-turing
    complete DSL.''')
