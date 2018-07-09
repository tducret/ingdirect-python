# ingdirect

# Description

Ce package permet de consulter très simplement ses comptes bancaires [ING Direct](https://www.ingdirect.fr/).

# Pré-requis

- Python 3
- pip3

# Installation

```bash
pip3 install -U ingdirect
```

# Utilisation via la commande en ligne `ing`

Après installation, la commande `ing` est disponible dans le terminal.

```bash
ing
```

Après saisie des paramètres de connexion, la commande renverra le solde de chaque compte au format csv :

```csv
Nom du compte;Solde;Devise
Compte Courant XXXX 1234;1500,50;EUR
Livret A XXXX 3456;10000,00;EUR
```

Plus d'informations sur la commande, via :

```bash
ing --help
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
