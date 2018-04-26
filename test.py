# -*- coding: utf-8 -*-
import ingdirect as ing
import os

# Récupération des éléments pour se connecter
# dans les variables d'environnement
# Executer dans bash : export ING_NUM_CLIENT="1111111"
numero_client = os.environ['ING_NUM_CLIENT']
date_naissance = os.environ['ING_DATE_NAISSANCE']
code = os.environ['ING_CODE']

synthese_comptes = ing.synthese_comptes(
                num_client=numero_client,
                date_naissance=date_naissance,
                code=code)

print(synthese_comptes)
print("Nombre de comptes : %d" % len(synthese_comptes))
for compte in synthese_comptes:
    print(compte)
