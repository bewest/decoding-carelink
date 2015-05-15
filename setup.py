#!/usr/bin/python

from setuptools import setup, find_packages
import platform
import subprocess

def is_virtualenv ( ):
  import os
  proc = subprocess.Popen(['which', 'virtualenvwrapper'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  has_venv = proc.poll( ) == 0
  return os.environ.get('VIRTUAL_ENV', has_venv)


import decocare
def readme():
    with open("README.markdown") as f:
        return f.read()

dataFiles = [ ]
if platform.system( ) == 'Linux':
  prefix = '/etc/udev/rules.d'
  if is_virtualenv( ):
    prefix = ''
  dataFiles = [
      (prefix, ['80-medtronic-carelink.rules' ]),
    ]

setup(name='decocare',
    version='0.0.14', # http://semver.org/
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
