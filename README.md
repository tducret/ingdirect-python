# ingdirect

[![Travis](https://img.shields.io/travis/tducret/ingdirect-python.svg)](https://travis-ci.org/tducret/ingdirect-python)
[![Coveralls github](https://img.shields.io/coveralls/github/tducret/ingdirect-python.svg)](https://coveralls.io/github/tducret/ingdirect-python)
[![PyPI](https://img.shields.io/pypi/v/ingdirect.svg)](https://pypi.org/project/ingdirect/)
[![Docker Image size](https://img.shields.io/microbadger/image-size/thibdct/ing.svg)](https://hub.docker.com/r/thibdct/ing/)
![License](https://img.shields.io/github/license/tducret/ingdirect-python.svg)

# Description

Ce package permet de consulter très simplement ses comptes bancaires [ING Direct](https://www.ing.fr/).

J'ai écrit un article sur la création de ce module [sur mon blog](https://www.tducret.com/scraping/2018/05/24/reverse-engineering-de-l-application-mobile-ing-direct.html)

🎁 Vous pouvez maintenant utiliser la commande via [son image Docker](#docker)

# Pré-requis

- Python 3
- pip3

# Installation

```bash
pip3 install -U ingdirect
```

# Utilisation via la commande en ligne `ing.py`

Après installation, la commande `ing.py` est disponible dans le terminal.

```bash
ing.py
```

Après saisie des paramètres de connexion, la commande renverra le solde de chaque compte au format csv :

```csv
Nom du compte;Solde;Devise
Compte Courant XXXX 1234;1500,50;EUR
Livret A XXXX 3456;10000,00;EUR
```

Plus d'informations sur la commande, via :

```bash
ing.py --help
```

Les paramètres de connexion peuvent également être stockés dans des variables d'environnement.
Par exemple :

```bash
export ING_NUM_CLIENT="1234567"
```

Variable d'environnement    | Description
--------------------------- | ---------------------------------------
ING_NUM_CLIENT              | Numéro de client ING Direct
ING_DATE_NAISSANCE          | Date de naissance au format JJMMAAAA (ex: 30121982)
ING_CODE                    | Mot de passe ING Direct (ex : 123456)


# Utilisation via le package Python

```python
# -*- coding: utf-8 -*-
import ingdirect as ing

synthese_comptes = ing.synthese_comptes(num_client=<NUMERO_CLIENT>, date_naissance=<DATE_NAISSANCE>, code=<CODE_SECRET>)

for compte in synthese_comptes:
    print("%s %s : %.2f€" % (compte.type, compte.label, compte.solde))

print("Solde total des comptes : %.2f€" % (synthese_comptes.solde_total))

```

Ce qui renverra ce type de résultats :

```
Compte Courant XXXX 1234 : 1500.50€
Livret A XXXX 3456 : 10000.00€
Solde total des comptes : 11500.50€
```

### Attributs de l'objet `Synthese_comptes` renvoyé par la fonction `synthese_comptes`

Nom de l'attribut   | Description
------------------- | ---------------------------------------
dict                | Dictionnaire complet renvoyé par ING
solde_total         | Solde total des comptes
liste_comptes       | Liste des objets de type Compte (cf. ci-dessous)

### Attributs des objets de type `Compte`, obtenus via l'attribut `liste_comptes`

Nom de l'attribut   | Description
------------------- | ---------------------------------------
dict                | Dictionnaire complet renvoyé par ING
solde               | Solde du compte
label               | Nom du compte (ex: "XXXX 1234")
type                | Type du compte (ex: "Compte Courant")
uid                 | Identifiant unique du compte

# Docker

Vous pouvez utiliser l'outil `ing` avec son [image Docker](https://hub.docker.com/r/thibdct/ing/)

Pour cela, exécutez :

`docker run -it --rm thibdct/ing`

## 🤘 Encore plus facile 🤘

J'ai créé un script bash pour créer le container Docker encore plus facilement.

Installation :

```bash
curl -s https://raw.githubusercontent.com/tducret/ingdirect-python/master/ing.sh \
> /usr/local/bin/ing && chmod +x /usr/local/bin/ing
```
*Vous pouvez remplacer `/usr/local/bin` par un autre répertoire connu dans la variable d'environnement $PATH*

On vérifie que cela fonctionne :

```bash
ing --help
ing -n NUMERO_CLIENT -d DATE_NAISSANCE -c CODE_SECRET
```

Vous pouvez mettre à jour l'outil avec :

```bash
ing --upgrade
```

et le désinstaller avec :

```bash
ing --uninstall
```