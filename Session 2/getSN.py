#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Meraki API 101
Session 2: REST API
name:     Sebastian Metzner
company:  E.INFRA GmbH
"""
__author__ = 'Sebastian Metzner'
__version__ = '1.0'
__license__ = 'GPL'
__date__ = 'April 2020'

# Modules
import json
import os
import datetime
import time
import requests
import warnings
from requests.packages.urllib3 import exceptions

class APIError(Exception):

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)


def main():
    # variables
    base_url = 'https://api-mp.meraki.com/api/v0/'
    api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
    # default variables
    organization_def = 'DevNet Sandbox'
    
    print('### Cisco Meraki API 101 - Hausaufgabe 2 ###')

    # Task 0) Abfrage von Eingaben
    # Task 0a) Organisation 
    
    # Abrufen aller möglichern Organization-IDs
    url_id = f'{base_url}organizations' 
    header_id = {'X-Cisco-Meraki-API-Key': api_key, 'Content-Type': 'application/json'} 
    warnings.simplefilter("ignore", exceptions.InsecureRequestWarning) 
    response_id = requests.get(url_id, headers=header_id, verify=False) 
    # Errorhandling
    if response_id.status_code != 200:
        raise APIError('Fehler {}'.format(response_id.status_code))
    
    # Ausgabe der verfügbaren Organisationen
    org_list = response_id.json()
    print('Übersicht der verfügbaren Organisationen:')
    for counter, org in enumerate(org_list):
        orgName = org['name']
        print(f'  [{counter}] {orgName}')
        
        # Werte für Default (Devnet Sandbox ermitteln
        if orgName == organization_def:
            orgNr_def = counter
    
    # Schleife zur Abfrage der zu untersuchenden Organisation
    while True:
        eingabe_org = input(f'1. Welche Organisation [0-{counter}] soll abgefragt werden? [[{orgNr_def}] {organization_def}] :')
        # Eingabe auf Sinnhaftigkeit prüfen:
        # Ohne Eingabe => es werden Default Parameter genutzt
        if eingabe_org == '':
            orgNr = orgNr_def
            break
        # Prüfen, ob Eingabe eine Zahl ist
        try:
            orgNr = int(eingabe_org)
            isINT = True
        # Eingabe ist keine Zahl
        except:
            isINT = False
        # Prüfen, ob Zahl im Bereich
        if isINT:
            # Prüfen, ob Eingabe auf einer der verfügbaren Organisationen verweist
            if (0 <= orgNr <= counter):
                # Schleife zum Abfragen der Eingabe kann verlassen werden
                break
        
        # Nutzereingabe war nicht korrekt => Fehlermeldung und erneuter Schleifendurchlauf
        print('\033[31m' + 'Bitte die Listennummer der Organisation eingeben'  + '\033[0m')
    
    # Nutzereingabe in Variablen schreiben
    organization = org_list[orgNr]['name']
    organizationID = org_list[orgNr]['id']
    print(f'Organisation: [{orgNr}] {organization}')
    
    # Schleife zur Abfrage der Speicherung der Portkonfiguration
    while True:
        eingabe_outpFormat = input(f'2. Sollen Dateien zur Portkonfiguration gespeichert werden? [Ja] :')
        if eingabe_outpFormat == 'Ja' or eingabe_outpFormat == 'J' or eingabe_outpFormat == 'ja' or eingabe_outpFormat == 'j' or eingabe_outpFormat == '' :
            # Hilfsvariable, die festhält, ob Konfiguration als Dateien gespeichert werden soll
            save_portConf = True
            break
        elif eingabe_outpFormat == 'Nein' or eingabe_outpFormat == 'N' or eingabe_outpFormat == 'nein' or eingabe_outpFormat == 'n':
            # Hilfsvariable, die festhält, ob Konfiguration als Dateien gespeichert werden soll
            save_portConf = False
            break
        
    
    # Task 1) Liste die vorhandenen Switches und deren SN der ausgewählten Organisation auf:
    print(' ### Aufgabe 1 ###')
    print(organization, 'hat folgende Organization-ID: ', organizationID)
    
    # Task 1a) Liste der Devices erhalten
    """
    	curl 	-L 
    			-H 'X-Cisco-Meraki-API-Key: <key>' 
    			-H 'Content-Type: application/json' 
    			-X GET 'https://api.meraki.com/api/v0/organizations/{organizationId}/devices'
    """

    url_dev = f'{base_url}organizations/{organizationID}/devices'
    header_dev = {'X-Cisco-Meraki-API-Key': api_key, 'Content-Type': 'application/json'}
    
    response_dev = requests.get(url_dev, headers=header_dev, verify=False)
    # Errorhandling
    if response_dev.status_code != 200:
        raise APIError('Fehler {}'.format(response_dev.status_code))
    
    
    # 1b) Ausgabe der Devices
    devices = response_dev.json()
    devicesNr = len(devices)
    print(f'{organization} hat folgende Device-Anzahl:    {devicesNr}')
    # Tabellenkopf
    print('model'.ljust(15, ' '), 'networkId'.ljust(25, ' '), 'serial'.ljust(25, ' '))
    print(56*'_')
    # Darstellung der Switche durch Iteration über Device-Liste
    for i, listelement in enumerate(devices):
        # Ausgabe aller Keys eines Dictionaries
        print(listelement['model'].ljust(15, ' '), listelement['networkId'].ljust(25, ' '), listelement['serial'].ljust(25, ' '))
    

    # Task 2) Gib die Portconfig der vorhandenen Switches aus
    print('\n', 30*'-')
    print(' ### Aufgabe 2 ###')
    
    '''
    curl    -L
            -H 'X-Cisco-Meraki-API-Key: <key>' 
            -H 'Content-Type: application/json' 
            -X GET 'https://api.meraki.com/api/v0/devices/{serial}/switchPorts'
    '''
    header_port = {'X-Cisco-Meraki-API-Key': api_key, 'Content-Type': 'application/json'}
    allSwitches = {}
    
    # Task 2a) Pfad für Unterordner zum Speichern der Portconfig vorbereiten 
    # Step 1: Ordnernamen definieren
    curr_time = datetime.datetime.now()
    # Ausgabe der Zeit formatieren
    time_path = curr_time.strftime('%Y-%m-%d_%H%M%S')
    # Namen für Unterordner zum Speichern der Dateien definieren
    job_path = f'{organization}_{time_path}'
    # Step 2: Prüfen, ob Unterordner bereits existiert, falls nicht muss Ordner angelegt werden
    if os.path.exists(job_path) == False:
        # Ordner mit der Organisation und der aktuellen Zeit erstellen
        os.mkdir(job_path)
    
    # Task 2b) Über Device-Liste iterieren und für jeden Switch die Portconfig abfragen
    for counter, element in enumerate(devices):
        # Prüfen, ob das Device ein Switch ist (Model beginnt mit 'MS')
        if element['model'].startswith('MS'):
            serial = element['serial']
            switchModel = element['model']
            url_port = f'{base_url}/devices/{serial}/switchPorts'
            warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
            response_port = requests.get(url_port, headers=header_port, verify=False)
            # Errorhandling
            if response_port.status_code != 200:
                raise APIError('Fehler {}'.format(response_port.status_code))
            
            switch_config = response_port.json()
            # Ausgabe der Portconfig in Datei
            if save_portConf:
                with open(f'{job_path}/data_switch-{serial}.txt', 'w', encoding = 'utf-8') as f:
                    json.dump(response_port.json(), f, ensure_ascii=False, indent=4)
                a = {serial:switch_config}
                allSwitches.update(a)
                print(switchModel.ljust(12, ' '), 'Serial: ', f'{serial} - Portconfiguration saved to file')
            # Ausgabe der Portkonfig in CLI
            else:
                print(switchModel.ljust(12, ' '), 'Serial: ', f'{serial} - Portconfiguration:')
                # Ausgabe formatieren
                switch_config_formatted = json.dumps(response_port.json(), sort_keys = True, indent = 4)
                print(switch_config_formatted)
        else:
            continue
        
        # Auf 5 Anfragen/Sekunde gegen die API begrenzen
        # Da die Anfragen der Portconfig aber einige Zeit benötigen, ist dies eigentlich nicht notwendig
        if counter % 5 == 0:
            time.sleep(1)
    
    print('\n', 30*'-')
    print(' ### Finish ###')

# Main
if __name__ == "__main__":
    main()
