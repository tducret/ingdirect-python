# ingdirect

# Description

Ce package permet de consulter très simplement ses comptes bancaires [ING Direct](https://www.ingdirect.fr/).

# Pré-requis

- Python 3

# Installation

    $ pip3 install -U ingdirect

# Utilisation

```python
# -*- coding: utf-8 -*-
import ingdirect as ing

synthese_comptes = ing.synthese_comptes(num_client=<NUMERO_CLIENT>, date_naissance=<DATE_NAISSANCE>, code=<CODE_SECRET>)

print("Solde total des comptes : %.2f€" % (synthese_comptes.solde_total))

for compte in synthese_comptes:
    print("%s %s : %.2f€" % (compte.type, compte.label, compte.solde))

```

Ce qui renverra ce type de résultats :

```
Solde total des comptes : 11500.50€
Compte Courant XXXX 1234 : 1500.50€
Livret A XXXX 3456 : 10000.00€
``