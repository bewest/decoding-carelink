#!/usr/bin/python

from setuptools import setup, find_packages
import platform

import decocare
def readme():
    with open("README.markdown") as f:
        return f.read()

dataFiles = [ ]
if platform.system( ) == 'Linux':
  dataFiles = [
      ('/etc/udev/rules.d', ['80-medtronic-carelink.rules' ]),
    ]

setup(name='decocare',
    version='0.0.13', # http://semver.org/
    description='Audit, inspect, and command MM insulin pumps.',
    long_description=readme(),
    author="Ben West",
    author_email="bewest+insulaudit@gmail.com",
    url="https://github.com/bewest/decoding-carelink",
    #namespace_packages = ['insulaudit'],
    packages=find_packages( ),
    install_requires = [
      'pyserial', 'python-dateutil', 'argcomplete'
    ],
    scripts = [
      'bin/mm-press-key.py',
      'bin/mm-send-comm.py',
      'bin/mm-set-suspend.py',
      'bin/mm-temp-basals.py',
      'bin/mm-decode-history-page.py',
      'bin/mm-latest.py',
      'bin/mm-bolus.py',
      'bin/mm-set-rtc.py',
      'bin/mm-pretty-csv',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries'
    ],
    include_package_data=True,
    data_files=dataFiles,
    zip_safe=False
)

#####
# EOF
