# -*- coding: utf-8 -*-
import ingdirect as ing
import os

# To best tested with : python -m pytest -vs

numero_client = os.environ['ING_NUM_CLIENT']
date_naissance = os.environ['ING_DATE_NAISSANCE']
code = os.environ['ING_CODE']


def test_synthese_comptes():
    synthese_comptes = ing.synthese_comptes(
                num_client=numero_client,
                date_naissance=date_naissance,
                code=code)
    assert type(synthese_comptes) == ing.Synthese_comptes
    assert len(synthese_comptes) > 0
    assert "Nom du compte;Solde;Devise" in synthese_comptes.csv()
    assert synthese_comptes.solde_total > 0
