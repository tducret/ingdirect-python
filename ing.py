#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import ingdirect as ing

# Utilisation possible
# ing --numero-client <numero_client> --date-naissance <date_naissance>
# --code <code>
# ing (avec les variables d'environnement définies :
# ING_NUM_CLIENT, ING_DATE_NAISSANCE, ING_CODE)


@click.command()
@click.option(
    '--numero-client', '-n',
    envvar="ING_NUM_CLIENT",
    type=str,
    help='votre numéro client ING Direct',
    prompt='votre numéro client ING Direct',
    required=True,
)
@click.option(
    '--date-naissance', '-d',
    envvar="ING_DATE_NAISSANCE",
    type=str,
    help='votre date de naissance au format JJMMAAAA (ex: 30121982)',
    prompt='votre date de naissance au format JJMMAAAA (ex: 30121982)',
    required=True,
)
@click.option(
    '--code', '-c',
    envvar="ING_CODE",
    type=str,
    help='votre mot de passe ING Direct (ex : 123456)',
    prompt='votre mot de passe ING Direct (ex : 123456)',
    hide_input=True,
    required=True,
)
@click.version_option(
    version=ing.__version__,
    message='%(prog)s, basé sur le module ingdirect version %(version)s'
)
def main(numero_client, date_naissance, code):
    """ Récupère la synthèse des comptes bancaires ING Direct """
    synthese_comptes = ing.synthese_comptes(
        num_client=numero_client,
        date_naissance=date_naissance,
        code=code)

    # for compte in synthese_comptes:
    #     print(compte)
    # print(synthese_comptes)

    print(synthese_comptes.csv())


if __name__ == "__main__":
    main()
