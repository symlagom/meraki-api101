#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Meraki API 101
Session 3: Meraki Dashboard
name:     Sebastian Metzner
company:  E.INFRA GmbH
"""
__author__ = 'Sebastian Metzner'
__version__ = '1.0'
__license__ = 'GPL'
__date__ = 'April 2020'

# Modules
import meraki
import json
import os
import datetime
import time
#import requests
#import warnings
#from requests.packages.urllib3 import exceptions

'''
class APIError(Exception):

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)
'''

def main():
    
    
    # variables
    #base_url = 'https://api-mp.meraki.com/api/v0/'
    #api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
    
    # default variables
    organization_def = 'DevNet Sandbox'
    
    # Instantiate Meraki Dashboard API session
    dashboard_call = meraki.DashboardAPI(
        base_url = 'https://api-mp.meraki.com/api/v0/',
        api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0',
        log_file_prefix=os.path.basename(__file__)[:-3],
        log_path='./logs/',
        print_console=False
	) 
    
    print('### Cisco Meraki API 101 - Hausaufgabe 3 ###')

    # Task 0) Abfrage von Eingaben
    # Task 0a) Organisation 
    
    # Abrufen aller möglichern Organization-IDs
    organizations = dashboard_call.organizations.getOrganizations()
    #print(json.dumps(organizations, indent=2))
 
    # Ausgabe der verfügbaren Organisationen
    org_list = organizations
    print('Übersicht der verfügbaren Organisationen:')
    for counter, org in enumerate(org_list):
        orgName = org['name']
        print(f'  [{counter}] {orgName}')
        
        # Werte für Default (Devnet Sandbox) ermitteln
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
    
    # Folgende Zeile wäre eigentlich die Abfrage gewesen -> aber diese Abfrage liefert viele nicht mehr aktive Devices im Netzwerk, die keine eindeutige
    # NetzwerkId und keine Konfiguration besitzen
    devices_helper = dashboard_call.organizations.getOrganizationInventory(organizationID)
    
    # Device List enthält viele ungültige Einträge (gelöschte Devices usw.) => aufräumen, indem man neue List von Devices erstellt,
    # die nur Elemente enthält, die eine networkId besitzen
    devices = []
    for i, listelement in enumerate(devices_helper):
        if listelement['networkId'] != None:
            devices.append(listelement)
    
    # 1b) Ausgabe der Devices
    devicesNr = len(devices)
    print(f'{organization} hat folgende Device-Anzahl:    {devicesNr}')
    # Zählvariable j indizieren
    switchNr = 0
    for listelement in devices:
        if listelement['model'].startswith('MS') and listelement['networkId'] != None:
            switchNr += 1
    print(f'{organization} hat folgende Switch-Anzahl:    {switchNr}')
    
    # Online/Offline Status erhalten 
    helper_online = dashboard_call.organizations.getOrganizationDeviceStatuses(organizationID)
    #helper_online_json = json.dumps(helper_online, indent = 2)
    #print(helper_online_json)
    online_list = {}
    for element_overall in helper_online:
        #print(element_overall['name'],element_overall['serial'],': ', element_overall['status'])
        online_list[element_overall['serial']] = element_overall['status']
    
    #print(online_list)
    #print(json.dumps(devices, indent = 2))
    
    
    # Output for Switches
    print('\n', 'Switch')
    # Tabellenkopf
    print('Nr'.ljust(4, ' '), 'name'.ljust(15, ' '), 'model'.ljust(10, ' '), 'networkId'.ljust(25, ' '), 'serial'.ljust(15, ' '), 'status'.ljust(15, ' '))
    print(82*'_')
    
    # Darstellung der Switche durch Iteration über Device-Liste
    # "i" is variable to show the row number of the table
    i = 0
    for listelement in devices:
        if listelement['networkId'] != None:
            if listelement['model'].startswith('MS'):
                # Ausgabe aller Keys eines Dictionaries
                i += 1
                row_nr = str(i)
                serial_nr = listelement['serial']
                element_status = online_list[serial_nr]
                
                print(row_nr.ljust(4, ' '),
                      listelement['name'].ljust(15, ' '),
                      listelement['model'].ljust(10, ' '), 
                      listelement['networkId'].ljust(25, ' '), 
                      listelement['serial'].ljust(15, ' '), 
                      element_status.ljust(15, ' ')
                      )
    
    # Output for all other device (without switches)
    # Tabellenkopf
    print('\n', 'Other Devices')
    print('Nr'.ljust(4, ' '), 'name'.ljust(15, ' '), 'model'.ljust(10, ' '), 'networkId'.ljust(25, ' '), 'serial'.ljust(15, ' '), 'status'.ljust(15, ' '))
    print(82*'_')
    i = 0
    for listelement in devices:
        if listelement['networkId'] != None:
            if not listelement['model'].startswith('MS'):
                # Ausgabe aller Keys eines Dictionaries
                i += 1
                row_nr = str(i)
                serial_nr = listelement['serial']
                element_status = online_list[serial_nr]
                
                print(row_nr.ljust(4, ' '),
                      listelement['name'].ljust(15, ' '),
                      listelement['model'].ljust(10, ' '), 
                      listelement['networkId'].ljust(25, ' '), 
                      listelement['serial'].ljust(15, ' '), 
                      element_status.ljust(15, ' ')
                      )
    
    
    # Task 2) Gib die Portconfig der vorhandenen Switches aus
    print('\n', 80*'-')
    print(' ### Aufgabe 2 ###')
    allSwitches = {}
    
    # Unterordner anlegen, wenn Portconfig gespeichert werden soll
    if save_portConf:
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
        if element['networkId'] != None:
            # Prüfen, ob das Device ein Switch ist (Model beginnt mit 'MS')
            if element['model'].startswith('MS'):
                serial = element['serial']
                switchModel = element['model']
                #switch_config = dashboard_call.switch_ports.getDeviceSwitchPorts(serial)
                
                switch_config = dashboard_call.switch_ports.getDeviceSwitchPorts(serial)
                # Ausgabe der Portconfig in Datei
                if save_portConf:
                    with open(f'{job_path}/data_switch-{serial}.txt', 'w', encoding = 'utf-8') as f:
                        json.dump(switch_config, f, ensure_ascii=False, indent=4)
                    a = {serial:switch_config}
                    allSwitches.update(a)
                    print(switchModel.ljust(12, ' '), 'Serial: ', f'{serial} - Portconfiguration saved to file')
                # Ausgabe der Portkonfig in CLI
                else:
                    print(switchModel.ljust(12, ' '), 'Serial: ', f'{serial} - Portconfiguration:')
                    # Ausgabe formatieren
                    switch_config_formatted = json.dumps(switch_config, sort_keys = True, indent = 4)
                    print(switch_config_formatted)
            else:
                continue
        
        # Auf 5 Anfragen/Sekunde gegen die API begrenzen
        # Da die Anfragen der Portconfig aber einige Zeit benötigen, ist dies eigentlich nicht notwendig
        if counter % 5 == 0:
            time.sleep(1)
    
    print('\n', 80*'-')
    print(' ### Finish ###')

# Main
if __name__ == "__main__":
    main()
