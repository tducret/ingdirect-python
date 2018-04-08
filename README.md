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

# Utilisation

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