#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Meraki API 101
Session 1: Datatypes and structured output
name:     Sebastian Metzner
company:  E.INFRA GmbH
"""
__author__ = 'Sebastian Metzner'
__version__ = '1.0<'
__license__ = 'GPL'
__date__ = 'April 2020'

# Modules
import json


def main():
    # variables
    result = b'[\
        {"id":"865776","name":"Cisco Live US2019","url":"https://n22.meraki.com/o/CVQqTb/manage/organization/overview"},\
        {"id":"646829496481089588","name":"DevNetMultiDomainDemo","url":"https://n149.meraki.com/o/rw48vavc/manage/organization/overview"},\
        {"id":"549236","name":"DevNet Sandbox","url":"https://n149.meraki.com/o/-t35Mb/manage/organization/overview"},\
        {"id":"52636","name":"Forest City -Other","url":"https://n42.meraki.com/o/E_utnd/manage/organization/overview"},\
        {"id":"463308","name":"DevNet San Jose","url":"https://n18.meraki.com/o/vB2D8a/manage/organization/overview"},\
        {"id":"566327653141842188","name":"DevNetAssoc","url":"https://n6.meraki.com/o/dcGsWag/manage/organization/overview"},\
        {"id":"566327653141842061","name":"ENLabs","url":"https://n6.meraki.com/o/iY6FHcg/manage/organization/overview"},\
        {"id":"681155","name":"DeLab","url":"https://n6.meraki.com/o/49Gm_c/manage/organization/overview"}]'

    # Task 1) was ist dies für ein Datentyp
    print(' Aufgabe 1:')
    # dt ... datatype
    dt_result = type(result)
    print("Die Variable \'result\' hat den Datentyp " + str(dt_result))
    # Datentyp ist bytes literal

    # Task 2) Script mit formatierter Ausgabe:
    print('\n Aufgabe 2:')
    # a) Analyse von Datum "result"
    result_list = json.loads(result)
    dt_result_list = type(result_list)
    result_dict_1 = result_list[1]
    # => result ist eine Liste von Dictionaries
    
    # b1) Print Tabellenkopf = Keys
    print('id'.ljust(25, ' '), 'name'.ljust(25, ' '), 'url'.ljust(25, ' '))
    print(115*'-')
    # b2) Print Tabelleninhalt = Values
    for i, listelement in enumerate(result_list):
        # Ausgabe aller Keys eines Dictionaries
        print(listelement['id'].ljust(25, '.'), listelement['name'].ljust(25, '.'), listelement['url'].ljust(25, '.'))
        
    # Task 3) Script, welches die id zu 'DevNet Sandbox' ermittelt.
    print('\n Aufgabe 3:')
    
    for listelement in result_list:
        if listelement['name'] == 'DevNet Sandbox':
            print('DevNet Sandbox hat folgende ID: ', listelement['id'])


# Main
if __name__ == "__main__":
    main()
