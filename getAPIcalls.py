#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Meraki API 101
Session 4: 	Meraki Dashboard
Task:		1 - Datenschutzbeauftragter
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
import datetime
import time
import pytz
import json
import os
import tkinter as tk
import pandas as pd
import xlsxwriter
from PIL import ImageTk, Image

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
print(datetime.datetime.now())
    
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
    button_getapi.config(state = tk.NORMAL)

   

def get_APIcalls():
    
    # Get the selected timezone
    timezone_choosen = timezone.get()
    # Change of time has only be done if the input was in local time
    # otherwise input and output can be used in UTC
    if timezone_choosen == 'local_tz': 
        # Get time offset between local time and UTC
        # offset to UTC in seconds
        utc_offset_s = time.localtime().tm_gmtoff
        # offset in hours
        utc_offset_h = int(utc_offset_s/3600)
    
    # UTC time was choosen and no correction needed
    else:
        utc_offset_h = 0

    
    
    # Read the input of the dropdown menu
    org_choosen = variable.get()
    # Get Organization ID out of string
    organization_id = org_choosen.split('[')[1].split(']')[0]
    
    # Get information of date input
    start_date_day_input = start_date_day.get()
    start_date_month_input = start_date_month.get()
    start_date_year_input = start_date_year.get()
    start_time_h_input = str(int(start_time_h.get()) - utc_offset_h)
    start_time_min_input = start_time_min.get()
    end_date_day_input = end_date_day.get()
    end_date_month_input = end_date_month.get()
    end_date_year_input = end_date_year.get()
    end_time_h_input = str(int(end_time_h.get()) - utc_offset_h)
    end_time_min_input = end_time_min.get()
    
    # build string for start time t0
    t0_input = start_date_year_input + '-' + start_date_month_input + '-' + start_date_day_input + 'T' + start_time_h_input + ':' + start_time_min_input + ':00Z'
    #build string for endtime t1
    t1_input = end_date_year_input + '-' + end_date_month_input + '-' + end_date_day_input + 'T' + end_time_h_input + ':' + end_time_min_input + ':00Z'
    
    print(t0_input)
    print(t1_input)
    # Actual request for the API Request 
    response = dashboard_call.organizations.getOrganizationApiRequests(
        organization_id,
        total_pages = 'all',
        perPage = '1000',
        t0= t0_input,
        t1= t1_input
        )
    
    
    ### Save results to excel file
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
        table_length = len(response) + 1
        table_length_string = str(table_length)
        worksheet.add_table('A1:I'+table_length_string, {'style': 'Table Style Light 11',
                                                         'columns': [{'header': 'Nr'},
                                                                     {'header': 'Admin ID'},
                                                                     {'header': 'Admin Name'},
                                                                     {'header': 'Source IP'},
                                                                     {'header': 'Method'},
                                                                     {'header': 'Response Code'},
                                                                     {'header': 'Host'},
                                                                     {'header': 'Request'},
                                                                     {'header': 'Time'}
                                                                     ]})
    
 
    admin_list = dashboard_call.organizations.getOrganizationAdmins(organization_id)

    
    
    # Tabellenkopf
    table_head = 'Nr'.ljust(7,' ') + 'Admin ID'.ljust(20,' ') + 'Admin Name'.ljust(25,' ') + 'Source IP'.ljust(18,' ') + 'Method'.ljust(8,' ') + 'Response Code'.ljust(22,' ') + 'Host'.ljust(19,' ') + 'Request'.ljust(28,' ') + 'Time'.ljust(15,' ')+ '\n' 
    label_output_data.insert(tk.INSERT, table_head)
    
    # Iterate over all API Requests
    for i, listelement in enumerate(response):
        
        ### A: Create output for GUI
        # Translate Response Code
        if listelement['responseCode'] == 200:
            response_for_request = "200-OK"
        elif listelement['responseCode'] == 400:
            response_for_request = "400-Bad Request"
        elif listelement['responseCode'] == 401:
            response_for_request = "401-Unauthorized"
        elif listelement['responseCode'] == 403:
            response_for_request = "403-Forbidden"  
        elif listelement['responseCode'] == 404:
            response_for_request = "404-Not Found"
        elif listelement['responseCode'] == 429:
            response_for_request = "429-Too Many Requests"
        else:
            response_for_request = "429-Server Errors"
        
        # Requested Path
        req_path = listelement['path'].split('/')[-1]
        
        # Change timestamp to local time (if needed)
        timestamp = listelement['ts']
        if timezone_choosen == 'local_tz':
            t = timestamp.split('T')[1].split(':')[0]
            t = str(int(t) + utc_offset_h).zfill(2)
            timestamp = timestamp.split('T')[0] + 'T' + t + ':' + timestamp.split(':')[1] + ':' + timestamp.split(':')[2]
            # delete last character "Z" as indication of UTC
            timestamp = timestamp[:-1]
        
        # Get Admin Name out of Admin ID
        for element_adminlist in admin_list:
            if element_adminlist['id'] == listelement['adminId']:
                admin_name = element_adminlist['name']
            
        
        row = (str(i+1).ljust(7, ' ')
        + listelement['adminId'].ljust(20, ' ')
        + admin_name.ljust(25, ' ')
        + listelement['sourceIp'].ljust(18, ' ') 
        + listelement['method'].ljust(8, ' ') 
        + response_for_request.ljust(22, ' ')
        + listelement['host'].ljust(19, ' ')
        + req_path.ljust(28, ' ')
        + timestamp.ljust(15, ' ')
        + '\n')
        
        label_output_data.insert(tk.INSERT, row)
        
        ### B: Create output for excel
        if save_excel.get() == '1':
            row_data = [str(i+1),
                        listelement['adminId'],
                        admin_name,
                        listelement['sourceIp'],
                        listelement['method'],
                        response_for_request,
                        listelement['host'],
                        req_path,
                        timestamp                        
                        ]
            # check the response and highlight the line in case of error
            format_red = workbook.add_format({'bg_color': '#FFC7CE',
                               'font_color': '#9C0006'})
            if listelement['responseCode'] == 200:
                worksheet.write_row('A'+str(i+2), row_data)
            else:
                worksheet.write_row('A'+str(i+2), row_data, format_red)
        
        list_source_req.append(listelement['sourceIp'])
    
    
    
    # In case output is needed as indented JSON file
    #apicall_output = json.dumps(response, indent = 2)
    #print(apicall_output)
    
    
    if save_excel.get() == '1':
        # Draw chart for number of requests per source IP
        dict_count_source_ip = {}
        # iterate over list
        for element in list_source_req:
            # source IP is not in list
            if element in dict_count_source_ip:
                count = dict_count_source_ip.get(element)
                dict_count_source_ip[element] = count + 1
            
            # source IP is already in list
            else:
                dict_count_source_ip[element] = 1
        
        # Bar Chart on Excel Sheet
        # Create a new chart object.
        chart1 = workbook.add_chart({'type': 'column'})
        
        # Add a chart title and some axis labels.
        chart1.set_title ({'name': 'Number of Requests per Source IP'})
        chart1.set_x_axis({'name': 'Source IP'})
        chart1.set_y_axis({'name': 'Number of Requests'})

        table2_length_string = str(len(dict_count_source_ip)+1)
        worksheet.add_table('L1:M'+table2_length_string, {'style': 'Table Style Light 11',
                                                         'columns': [{'header': 'Source IP'},
                                                                     {'header': 'Number of Requests'}]})
                                                         
        x_series = []
        y_series = []
        for j, key in enumerate(dict_count_source_ip):
            x_series.append(key)
            y_series.append(dict_count_source_ip.get(key))
            
            row_helper = str(j + 2)
            worksheet.write('L'+row_helper, key)
            worksheet.write('M'+row_helper, dict_count_source_ip.get(key))
            
        # Add a series to the chart.
        chart1.add_series({'name': '=Sheet1!$L$2:$L$'+table2_length_string,
                          'values': '=Sheet1!$M$2:$M$'+table2_length_string})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('O9', chart1)
        
        
        # Save the spreadsheet
        workbook.close()
                  

    label_output_data.config(state='disabled')
    label_output_data.pack(side = 'bottom')
    
    # Integrate Scrollbar to Data Output Area
    vscroll = tk.Scrollbar(frame4, orient='vertical', command=label_output_data.yview)
    label_output_data['yscroll'] = vscroll.set

    vscroll.pack(side="right", fill="y")
    label_output_data.pack(side="left", fill="both", expand=True)
    

    button_getapi.config(bg = 'green')
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
window.geometry('{}x{}'.format(1550, 1320))

canvas = tk.Canvas(window)

### Frame 1 - Header
frame1 = tk.Frame(window, width='500', height='100', relief = 'raised')
frame1.pack(side='top', padx='5',  pady='5')
# App Description Text
label_description = tk.Label(frame1, text = 'Get API calls for specified Organization',font='Helvetica 14 bold')
label_description.grid(row=0, column = col_halfmax)


### Frame 2 - Data Input
frame2 = tk.Frame(window, relief = 'raised')
#frame2.grid(row=1,column=col_halfmax)
frame2.pack(side='top', fill = 'x', padx='5',  pady='5')
frame2_1 = tk.Frame(window, relief = 'raised')
frame2_1.pack(fill = 'x', padx='5', pady='5')

label_apikey = tk.Label(frame2, text = "API Key")
label_apikey.grid(row=0,column=0)

label_start = tk.Label(frame2_1, text='Start', font='bold').grid(row=1,column=0)

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

# START
label_startdate = tk.Label(frame2_1, text = "Start Date [DD/MM/YYYY]")
label_startdate.grid(row=2,column=1)

start_date_day = tk.Entry(frame2_1, width='5')
start_date_day.grid(row=2, column=2)
start_date_day.insert(10, "21")
label_slash_1 = tk.Label(frame2_1, text = " / ").grid(row=2,column=3)

start_date_month = tk.Entry(frame2_1, width='5')
start_date_month.grid(row=2, column=4)
start_date_month.insert(10, "04")
label_slash_2 = tk.Label(frame2_1, text = " / ").grid(row=2,column=5)

start_date_year = tk.Entry(frame2_1, width='5')
start_date_year.grid(row=2, column=6)
start_date_year.insert(10, "2020")

label_starttime = tk.Label(frame2_1, text = "Start Time [hh:mm]").grid(row=3,column=1)
start_time_h = tk.Entry(frame2_1, width='5')
start_time_h.grid(row=3,column=2)
start_time_h.insert(10, "08")
start_time_min = tk.Entry(frame2_1,width='5')
start_time_min.grid(row=3,column=4)
start_time_min.insert(10, "00")
label_slash_3 = tk.Label(frame2_1, text = " : ").grid(row=3,column=3)

# END
label_end = tk.Label(frame2_1, text='End', font='bold').grid(row=4,column=0)
label_enddate = tk.Label(frame2_1, text = "End Date [DD/MM/YYYY]")
label_enddate.grid(row=5,column=1)

end_date_day = tk.Entry(frame2_1, width='5')
end_date_day.grid(row=5, column=2)
end_date_day.insert(10, "23")
label_slash_4 = tk.Label(frame2_1, text = " / ").grid(row=5,column=3)

end_date_month = tk.Entry(frame2_1, width='5')
end_date_month.grid(row=5, column=4)
end_date_month.insert(10, "04")
label_slash_5 = tk.Label(frame2_1, text = " / ").grid(row=5,column=5)

end_date_year = tk.Entry(frame2_1, width='5')
end_date_year.grid(row=5, column=6)
end_date_year.insert(10, "2020")

label_endtime = tk.Label(frame2_1, text = "Start Time [hh:mm]").grid(row=6,column=1)
end_time_h = tk.Entry(frame2_1, width='5')
end_time_h.grid(row=6,column=2)
end_time_h.insert(10,"17")
end_time_min = tk.Entry(frame2_1,width='5')
end_time_min.grid(row=6,column=4)
end_time_min.insert(10, "00")
label_slash_6 = tk.Label(frame2_1, text = " : ").grid(row=6,column=3)

# Radio Button for timezone
label_radiobutton_text = tk.Label(frame2_1, text = '     Input Timezone', font ='bold')
label_radiobutton_text.grid(row=1, column=9)
timezone = tk.StringVar(value='1')
timezone.set('local_tz')
local_tz = tk.Radiobutton(frame2_1, text='Local Timezone', variable=timezone, value='local_tz')
local_tz.grid(row=2, column=10)
utc_tz = tk.Radiobutton(frame2_1, text='UTC Timezone  ', variable=timezone, value='utc_tz')
utc_tz.grid(row=3, column=10)

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
button_getapi = tk.Button(frame3, text='Get API Call Informations', fg = 'black', 
                          font='bold', state = tk.DISABLED, 
                          command = get_APIcalls)
button_getapi.pack()


### Frame 4 - Data Output
frame4 = tk.Frame(window, borderwidth=1, relief = 'raised')
frame4.pack()
# Label Output Data
label_output_text = tk.Label(frame4, text = "Output Data", font = 'bold')
label_output_text.pack(side = "top")
# Textbox for Data Output
label_output_data = tk.Text(frame4, wrap = None, height=50, width=180, borderwidth=0)


### Frame 5 - Finish Buttons
frame5 = tk.Frame(window, relief = 'raised')
frame5.pack(side = 'bottom')

# Quit button
button_quit = tk.Button(frame5, text = "Quit", bg='white', fg = 'red', command = window.destroy, padx = 15, pady = 5)
button_quit.pack(side = 'bottom', pady = '10')



window.mainloop()

