#!/usr/bin/env python
#
# Setup prog for Certify certificate management utility

import sys
from distutils.core import setup

from vc3tool import resourcetool
release_version=resourcetool.__version__

setup(
    name="vc3-resource-tool",
    version=release_version,
    description='VC3 End User Resource handling utility.',
    long_description='''VC3 End User Resource handling utility.''',
    license='GPL',
    author='John Hover',
    author_email='jhover@bnl.gov',
    maintainer_email='jhover@bnl.gov',
    url='https://github.com/vc3-project',
    packages=[ 'vc3tool',
              ],
    classifiers=[
          'Development Status :: 3 - Beta',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GPL',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: System Administration :: Management',
    ],
    scripts=[ 'scripts/vc3',
             ],
    data_files=[ 
                #('share/certify', 
                #      ['README.txt',
                #       'NOTES.txt',            
                #       'LGPL.txt',
                #        ]
                #  ),
                #  ('share/certify/config', ['config/certify.conf','config/hosts.conf']              
                #   ),
               ]
)
