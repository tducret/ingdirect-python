# -*- coding: utf-8 -*-
import ingdirect as ing

# Valeurs à modifier
# ==========================
_NUM_CLIENT="1111111"
_DATE_NAISSANCE="01011980"
_CODE="123456"
# ==========================

synthese_comptes = ing.synthese_comptes(num_client=_NUM_CLIENT, date_naissance=_DATE_NAISSANCE, code=_CODE)

print(synthese_comptes)
print("Nombre de comptes : %d" % len(synthese_comptes))
for compte in synthese_comptes:
    print(compte)
