#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Meraki API 101
Session 4: 	Meraki Dashboard
Task:		2 - Sales
name:     	Sebastian Metzner
company:  	E.INFRA GmbH
"""
__author__ = 'Sebastian Metzner'
__version__ = '1.0'
__license__ = 'GPL'
__date__ = 'April 2020'

# Modules
#import meraki
import meraki_v1
import requests
import datetime
import time
import pytz
import json
import os
import tkinter as tk
import pandas as pd
import xlsxwriter
from PIL import ImageTk, Image
from bs4 import BeautifulSoup

# default variables
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
organization_def = 'DevNet Sandbox'
org_list_dd = ['none']
save_to_excel = 1
list_source_req = []
#org_list = []
row_max = 10 
col_max = 10
# middle of window
col_halfmax = int(round(col_max/2,0)-1)

print('Meraki Version: ', meraki_v1.__version__)
    
# Instantiate Meraki Dashboard API session
dashboard_call = meraki_v1.DashboardAPI(
    base_url = 'https://api-mp.meraki.com/api/v1/',
    api_key = API_KEY,
    #log_file_prefix=os.path.basename(__file__)[:-3],
    #log_path='./logs/',
    print_console=False
	)

def get_org():
    # Abrufen aller möglichern Organization-IDs
    organizations = dashboard_call.organizations.getOrganizations()
    #print(json.dumps(organizations, indent=2))

    # Ausgabe der verfügbaren Organisationen
    org_list = organizations
    #print("Übersicht der verfügbaren Organisationen:")
    for counter, org in enumerate(org_list):
        orgName = org['name']
    
    # reset list of organizations
    variable.set('')
    org_menu['menu'].delete(0, 'end')
    
    # Insert list of new organizations 
    new_org = []
    for counter, org in enumerate(org_list):
        orgName = org['name']  + ' [' + org['id'] + ']'
        
        new_org.append(orgName)
    
    #print(org['id'])
    print('Organization List updated')
    for choice in new_org:
        org_menu['menu'].add_command(label=choice, command=tk._setit(variable, choice))
    button_getorg.config(bg = 'green')
    button_getdev.config(state = tk.NORMAL)
    #return org_list

   

def get_DevInfo():

    
    # Read the input of the dropdown menu
    org_choosen = variable.get()
    # Get Organization ID out of string
    organization_id = org_choosen.split('[')[1].split(']')[0]
    
    
    # Actual request for the Devices of the organization
    dev_org = dashboard_call.organizations.getOrganizationDevices(
        organization_id,
        total_pages='all'
        )

    
    # Online/Offline Status erhalten 
    helper_online = dashboard_call.organizations.getOrganizationDevicesStatuses(organization_id)
    #helper_online_json = json.dumps(helper_online, indent = 2)
    #print(helper_online_json)
    online_list = {}
    for element_overall in helper_online:
        #print(element_overall['name'],element_overall['serial'],': ', element_overall['status'])
        online_list[element_overall['serial']] = element_overall['status']
    
    
    ### Web Scrapping
    URL = 'https://documentation.meraki.com/zGeneral_Administration/Other_Topics/Product_End-of-Life_(EOL)_Policies'
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='section_2')
    #print(results.prettify())
    
    # a) get text out of section 2 of the webpage
    web_text = results.get_text()
    end_list = []
        
    for i, line in enumerate(web_text.splitlines()):     
        # fill list with data
        '''
        if line != '':
            end_list.append(line)
        '''
        end_list.append(line)
    #print(end_list)  
    
    # b) get the links to the pdf files from the site
    data = []
    table = soup.find('table')
    #table_body = table.find('tbody')
    
    
    
    thead = table.find('thead')
    column_names = [th.text.strip() for th in thead.find_all('th')]
    column_names.insert(0, 'model')
    for row in table.find_all('tr'):
        row_data = []
        for td in row.find_all('td'):
            td_check = td.find('a')
            if td_check is not None:
                model = td.find('a').get_text()
                row_data.append(model)
                link = td.a['href']
                row_data.append(link)
            else:
                not_link = ''.join(td.stripped_strings)
                if not_link == '':
                     not_link = None
                row_data.append(not_link)
        data.append(row_data)
    df = pd.DataFrame(data[1:], columns=column_names)
    df_table_list = df.to_dict('records')
    
    '''
    for row in df_table_list:
        print(row)
    '''
    
    
    #A: Tablehead on GUI
    table_head = 'Nr'.ljust(7,' ') + 'Name'.ljust(30,' ') + 'Model'.ljust(15,' ') + 'Network ID'.ljust(25,' ') + 'Serial'.ljust(20,' ') + 'Status'.ljust(15,' ') + 'End-of-Sale Date'.ljust(20,' ') + 'End-of-Support Date'.ljust(15,' ') + '\n' + 160*'_' + '\n' 
    label_output_data.insert(tk.INSERT, table_head)
    
    #B: Prepare Excel list
    if save_excel.get() == '1':
    #if save_to_excel == 1:
        # Define path for saving excel file
        time_now1 = str(datetime.datetime.now()).split(' ')[0]
        time_now2 = str(datetime.datetime.now()).split(' ')[1].split(':')[0]
        time_now3 = str(datetime.datetime.now()).split(' ')[1].split(':')[1]
        time_now = time_now1 + '_' + time_now2 + '-' + time_now3
        path = time_now + '_' + org_choosen
        
        # Create folder for this function call, if no one exists
        if os.path.exists(path) == False:
                os.mkdir(path)
        
        excel_filename = org_choosen + ".xlsx"
        # Opening Excel Workbook
        workbook = xlsxwriter.Workbook(path + '/' + excel_filename)
        worksheet = workbook.add_worksheet()
        
        # Prepare excel sheet with table
        table_length = len(dev_org) + 1
        table_length_string = str(table_length)
        worksheet.add_table('A1:I'+table_length_string, {'style': 'Table Style Light 11',
                                                         'columns': [{'header': 'Nr'},
                                                                     {'header': 'Name'},
                                                                     {'header': 'Model'},
                                                                     {'header': 'Network ID'},
                                                                     {'header': 'Serial'},
                                                                     {'header': 'Status'},
                                                                     {'header': 'End-of-Sale Date'},
                                                                     {'header': 'End-of-Support Date'},
                                                                     {'header': 'Link'}
                                                                     ]})
    
    
    for i, listelement in enumerate(dev_org):
        # Convert elements to empty string if they are None
        if listelement['name'] == None:
            listelement_name = ''
        else:
            listelement_name = listelement['name']
            
        if listelement['model'] == None:
            listelement_model = ''
        else:
            listelement_model = listelement['model']
        
        if listelement['networkId'] == None:
            listelement_networkId = ''
        else:
            listelement_networkId = listelement['networkId']
            
        if listelement['serial'] == None:
            listelement_serial = ''
        else:
            listelement_serial = listelement['serial']
        
        # Get offline/online status
        serial_nr = listelement['serial']
        element_status = online_list[serial_nr]
        
        # Get information for End of Support, End of Sale and PDF Link        
        for k, element_from_web in enumerate(df_table_list):
            # Shorten name of model to hit also 'series' categories
            if len(listelement_model) > 5:
                listelement_model_compare = listelement_model[0:6]
            else:
                listelement_model_compare = listelement_model
                
            if element_from_web['model'].startswith(listelement_model_compare):
                end_sale = element_from_web['End-of-Sale Date']
                end_support = element_from_web['End-of-Support Date']
                link = element_from_web['Product']
                break
            else:
                end_sale = 'N/A'
                end_support = 'N/A'
                link = 'N/A'
        

        ### A: Create output for GUI
        row = (str(i+1).ljust(7, ' ')
        + listelement_name.ljust(30, ' ') 
        + listelement_model.ljust(15, ' ') 
        + listelement_networkId.ljust(25, ' ') 
        + listelement_serial.ljust(20, ' ')
        + element_status.ljust(15, ' ')
        + end_sale.ljust(20, ' ')
        + end_support.ljust(15, ' ')
        + '\n')
        
        
        label_output_data.insert(tk.INSERT, row)
        
        ### B: Create output for excel
        if save_excel.get() == '1':
            row_data = [str(i+1),
                        listelement_name,
                        listelement_model,
                        listelement_networkId,
                        listelement_serial,
                        element_status,
                        end_sale,
                        end_support,
                        link
                        ]
            
            # check, if there is an End of Support Date and highlight the line in case an entry exists
            format_red = workbook.add_format({'bg_color': '#FFC7CE',
                               'font_color': '#9C0006'})
            if end_support == 'N/A':
                worksheet.write_row('A'+str(i+2), row_data)
            else:
                worksheet.write_row('A'+str(i+2), row_data, format_red)
        
        #list_source_req.append(listelement['sourceIp'])
    
    
    
    # Save the spreadsheet
    workbook.close()
         

    label_output_data.config(state='disabled')
    label_output_data.pack(side = 'bottom')
    
    # Integrate Scrollbar to Data Output Area
    vscroll = tk.Scrollbar(frame4, orient='vertical', command=label_output_data.yview)
    label_output_data['yscroll'] = vscroll.set

    vscroll.pack(side="right", fill="y")
    label_output_data.pack(side="left", fill="both", expand=True)
    

    button_getdev.config(bg = 'green')
    print('finish')

# Application Window
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
    
    
window = tk.Tk()
window.title('API calls')
window.geometry('{}x{}'.format(1400, 1320))

canvas = tk.Canvas(window)

### Frame 1 - Header
frame1 = tk.Frame(window, width='600', height='100', relief = 'raised')
frame1.pack(side='top', padx='5',  pady='5')
# App Description Text
label_description = tk.Label(frame1, text = 'Get API calls for specified Organization',font='Helvetica 14 bold')
label_description.grid(row=0, column = col_halfmax)

#seperator1 = tk.Frame(width=200, bd=10, relief='sunken')
#seperator1.grid(column=0)

### Frame 2 - Data Input
frame2 = tk.Frame(window, relief = 'raised')
#frame2.grid(row=1,column=col_halfmax)
frame2.pack(side='top', fill = 'x', padx='5',  pady='5')
frame2_1 = tk.Frame(window, relief = 'raised')
frame2_1.pack(fill = 'x', padx='5', pady='5')

label_apikey = tk.Label(frame2, text = "API Key")
label_apikey.grid(row=0,column=0)


api_key_input = tk.Entry(frame2, width='50')
api_key_input.insert(10, "6bec40cf957de430a6f1f2baa056b99a4fac9ea0")
api_key_input.grid(row=1, column=2)
#api_key_input.pack(side='right', padx='5')


# unconventional method to make extra space before the Meraki logo to place it more
# on the right side
label_space = tk.Label(frame2, text = '                                           ')
label_space.grid(row=1,column=13)


# Meraki Logo
pic_meraki = Image.open("Meraki_Logo.png")
#pic_meraki = pic_meraki.
meraki_logo = ImageTk.PhotoImage(Image.open("Meraki_Logo.png").resize((170, 70)))
label_meraki = tk.Label(frame2, image = meraki_logo)
label_meraki.grid(row=1, column = 14)
 

variable = tk.StringVar(frame2_1)
# Set default value for Dropdown Menu
variable.set(org_list_dd[0])

org_menu = tk.OptionMenu(frame2, variable, *org_list_dd)
org_menu.grid(row=2, column=2, padx='50', sticky='nsew')

button_getorg = tk.Button(frame2, text='Get Organizations', fg = 'black', 
                          font='bold', command = get_org)
button_getorg.grid(row=1, column=3)


# Save some space between Elements
label_space = tk.Label(frame2_1, text = '                    ').grid(row=1, column=12)
# Checkbox for Save as Excel
label_checkboxSave_text = tk.Label(frame2_1, text = '     Save as Excel File', font ='bold')
label_checkboxSave_text.grid(row=1, column=13)
save_excel = tk.StringVar(value='1')
checkbutton_save = tk.Checkbutton(frame2_1, text='Save Excel', variable=save_excel)
checkbutton_save.grid(row=2, column=13)


### Frame 3 - Get Button
frame3 = tk.Frame(window, relief = 'raised')
frame3.pack()

# Button for get API Call action
button_getdev = tk.Button(frame3, text='Get Device Informations', fg = 'black', 
                          font='bold', state = tk.DISABLED, 
                          command = get_DevInfo)
button_getdev.pack()


### Frame 4 - Data Output
frame4 = tk.Frame(window, borderwidth=1, relief = 'raised')
frame4.pack()
# Label Output Data
label_output_text = tk.Label(frame4, text = "Output Data", font = 'bold')
label_output_text.pack(side = "top")
# Textbox for Data Output
label_output_data = tk.Text(frame4, wrap = None, height=50, width=170, borderwidth=0)


### Frame 5 - Finish Buttons
frame5 = tk.Frame(window, relief = 'raised')
frame5.pack(side = 'bottom')

# Quit button
button_quit = tk.Button(frame5, text = "Quit", bg='white', fg = 'red', command = window.destroy, padx = 15, pady = 5)
button_quit.pack(side = 'bottom', pady = '10')



window.mainloop()

