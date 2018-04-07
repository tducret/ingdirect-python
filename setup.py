# -*- coding: utf-8 -*-
from setuptools import setup
from pip.req import parse_requirements

_VERSION = '0.0.1'
install_reqs = parse_requirements('requirements.txt', session='hack')
requirements = [str(ir.req) for ir in install_reqs]

setup(
  name = 'ingdirect',
  packages = ['ingdirect'],
  version = _VERSION,
  license='MIT',
  platforms='Posix; MacOS X',
  description = 'Package pour consulter ses comptes bancaires ING Direct',
  author = 'Thibault Ducret',
  author_email = 'thibault.ducret@gmail.com',
  url = 'https://github.com/tducret/ingdirect-python',
  download_url = 'https://github.com/tducret/bibliotheque-toulouse-python/tarball/%s' % (_VERSION), # I'll explain this in a second
  keywords = ['api', 'banque', 'ING', 'ingdirect', 'comptes'],
  setup_requires=requirements,
  install_requires=requirements,
  classifiers = ['Programming Language :: Python :: 3.6'],
  tests_require=['pytest'],
)
