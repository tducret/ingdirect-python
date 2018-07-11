# -*- coding: utf-8 -*-
from setuptools import setup
try:  # Pour pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # Pour pip <= 9.0.3
    from pip.req import parse_requirements

# Basé sur http://peterdowns.com/posts/first-time-with-pypi.html

__version__ = '0.0.10'  # En cohérence avec __init.py__
_NOM_PACKAGE = 'ingdirect'
_URL_GITHUB = 'https://github.com/tducret/ingdirect-python'
_DESCRIPTION = 'Package pour consulter ses comptes bancaires ING Direct'
_MOTS_CLES = ['api', 'banque', 'ING', 'ingdirect', 'comptes']
_PACKAGE_DATA = ['images_chiffres_keypad/*.png']
# A supprimer ici + 'package_data' dans setup()
# si aucun fichier (autre que .py) n'est utilisé par le package
_SCRIPTS = ['ing.py']
# A supprimer ici + 'scripts' dans setup()
# si aucune commande exécutable n'est utilisée par le package

install_reqs = parse_requirements('requirements.txt', session='hack')
requirements = [str(ir.req) for ir in install_reqs]

setup(
    name=_NOM_PACKAGE,
    packages=[_NOM_PACKAGE],
    package_data={_NOM_PACKAGE: _PACKAGE_DATA, },
    scripts=_SCRIPTS,
    version=__version__,
    license='MIT',
    platforms='Posix; MacOS X',
    description=_DESCRIPTION,
    long_description=_DESCRIPTION,
    author='Thibault Ducret',
    author_email='thibault.ducret@gmail.com',
    url=_URL_GITHUB,
    download_url='%s/tarball/%s' % (_URL_GITHUB, __version__),
    keywords=_MOTS_CLES,
    setup_requires=requirements,
    install_requires=requirements,
    classifiers=['Programming Language :: Python :: 3'],
    python_requires='>=3',
    tests_require=['pytest'],
)

# ------------------------------------------
# Pour faire une nouvelle version sur pypi
# ------------------------------------------
# S'assurer que tout a été commité et pushé via git status
# (sinon git commit --am "Commentaire" et git push)
# git tag VERSION -m "Commentaire"
# git push --tags

# Test de génération du package sur le repository de test pypi
# python3 setup.py sdist register -r pypitest

# Test d'upload du package sur le repository de test pypi
# python3 setup.py sdist upload -r pypitest

# Upload du package sur le repository officiel de pypi
# python3 setup.py sdist upload -r pypi

# En cas de soucis, pour effacer un tag
# git push --delete origin VERSION
# git tag -d VERSION
