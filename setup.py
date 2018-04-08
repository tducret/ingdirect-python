# -*- coding: utf-8 -*-
from setuptools import setup
from pip.req import parse_requirements

# Basé sur http://peterdowns.com/posts/first-time-with-pypi.html

_VERSION = '0.0.1'
_NOM_PACKAGE = 'ingdirect'
_URL_GITHUB = 'https://github.com/tducret/ingdirect-python'
_DESCRIPTION = 'Package pour consulter ses comptes bancaires ING Direct'
_MOTS_CLES=['api', 'banque', 'ING', 'ingdirect', 'comptes']


install_reqs = parse_requirements('requirements.txt', session='hack')
requirements = [str(ir.req) for ir in install_reqs]

setup(
  name = _NOM_PACKAGE,
  packages = [_NOM_PACKAGE],
  version = _VERSION,
  license='MIT',
  platforms='Posix; MacOS X',
  description = _DESCRIPTION,
  author = 'Thibault Ducret',
  author_email = 'thibault.ducret@gmail.com',
  url = _URL_GITHUB,
  download_url = '%s/tarball/%s' % (_URL_GITHUB, _VERSION),
  keywords = _MOTS_CLES,
  setup_requires=requirements,
  install_requires=requirements,
  classifiers = ['Programming Language :: Python :: 3'],
  python_requires='>=3',
  tests_require=['pytest'],
)
