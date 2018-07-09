# -*- coding: utf-8 -*-
r"""La banque ING Direct <https://www.ingdirect.fr/> propose de gérer
ses comptes en ligne via son site web ou ses applications mobiles.
:mod:`ingdirect` permet la consultation en Python ou par ligne de commande.
"""
from builtins import object
from ingdirect.client import Client

__version__ = '0.0.9'  # En cohérence avec setup.py
# Permet à Sphinx de récupérer ces éléments pour la documentation
__all__ = ['Client']


class Synthese_comptes(object):
    """ Classe regroupant la liste des comptes bancaires """
    def __init__(self, synthese_comptes):
        self.dict = synthese_comptes
        self.solde_total = synthese_comptes.get('aggregatedBalance')
        self.liste_comptes = synthese_comptes.get('accounts')

    def __len__(self):
        """ Méthode pour demander le nombre de comptes
        (ex : len(synthese_comptes)) """
        return len(self.liste_comptes)

    def __getitem__(self, key):
        """ Méthode pour interroger l'objet comme une liste
        (ex : liste_comptes[1]) """
        return Compte(self.liste_comptes[key])

    def csv(self):
        chaine_csv = "Nom du compte;Solde;Devise"
        for compte in self:
            chaine_csv += (
                "\n%s %s;%.2f;EUR" %
                (
                    compte.type, compte.label,
                    compte.solde))
        chaine_csv = chaine_csv.replace('.', ',')
# On remplace le séparateur '.' dans compte.solde par ',' pour Excel français
        return chaine_csv

    def __repr__(self):
        """ Méthode d'affichage de l'objet """
        return ("Solde total des comptes : %.2f€" % self.solde_total)


class Compte(object):
    """ Classe d'un compte bancaire """
    def __init__(self, compte):
        self.dict = compte
        self.solde = compte.get('ledgerBalance')
        self.label = compte.get('label')
        self.type = compte.get('type').get('label')
        self.uid = compte.get('uid')

    def __repr__(self):
        """ Méthode d'affichage de l'objet """
        return ("%s %s : %.2f€" % (self.type, self.label, self.solde))


def synthese_comptes(num_client, date_naissance, code):
    """ Obtenir la synthèse des comptes sous forme de dictionnaire """
    ing = Client()
    ing._login(num_client=num_client, date_naissance=date_naissance)
    ing._recuperer_keypad()
    ing._code_a_saisir(code_complet=code)
    ing._recuperer_coord_chiffres()
    ing._saisie_code()
    ing._infos_client()
    retour_synthese_comptes = ing._synthese_comptes()
    ing._logout()

    return Synthese_comptes(retour_synthese_comptes)
