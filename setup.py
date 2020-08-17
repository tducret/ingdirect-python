# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup

HERE = Path(__file__).parent
reqs_path = HERE / 'requirements.txt'
with open(reqs_path) as reqs_file:
    requirements = reqs_file.read().splitlines()

# Basé sur http://peterdowns.com/posts/first-time-with-pypi.html

__version__ = '0.1.2'  # En cohérence avec __init.py__
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
    setup_requires=['setuptools>=38.2.0'],
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
# export VERSION=0.1.2; git tag $VERSION -m "Fix #2: modification setup.py pour la récupération des requirements"; git push --tags

# Pour effacer un tag
# git push --delete origin $VERSION; git tag -d $VERSION