#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os, shutil

# import templates as templates

"""
Build model from googlesheet
"""
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage ( 'credentials.json' )
creds = store.get ()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets ( 'client_secret.json', SCOPES )
    creds = tools.run_flow ( flow, store )
service = build ( 'sheets', 'v4', http=creds.authorize ( Http () ) )

# Call the Sheets API
SPREADSHEET_ID = '13FlaKMuYcGPzT8ropua_RYC_09kKvhrLWytErRODEYA'
RANGE_NAME = 'SumpurnEntryModel'
result = service.spreadsheets ().values ().get ( spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME ).execute ()
values = result.get ( 'values', [] )
if not values:
    print ( 'No data found.' )
else:
    print ( 'Name, Major:' )
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print ( row )
        # print('%s, %s' % (row[0], row[4]))

# Enter the name of the module:
new_module = values[0][1]
noOfFields = len(values[1])-1

print(values[1])

# Create the module

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment (
    loader=FileSystemLoader ( '.' ),
    autoescape=select_autoescape ( ['html', 'xml'] ),
)

import os

# Create the module
dirs = ['src']
for directory in dirs:
    if not os.path.exists ( directory ):
        os.makedirs ( directory )

myroot = os.path.join ( 'templates', 'sumpurn_entry' )

for root, dirs, files in os.walk ( myroot, topdown=False ):
    for name in files:
        filepath = os.path.join ( root, name ).replace ( "\\", "/" )
        print(name)
        # filepath='sumpurn_entry/models/models.py'
        print(filepath)
        print(os.getcwd ())
        template = env.get_template ( filepath )
        output = template.render ( new_module=new_module, noOfFields=noOfFields, fields=values[1],fieldTypes=values[2],fieldRequired=values[3] )
        print(output)
        # file-output.py
        if not os.path.exists ( os.path.dirname ( 'src/' +  filepath ) ):
            os.makedirs ( os.path.dirname ('src/' +  filepath ) )
        f = open ( 'src/' + filepath, 'w' )

        f.write ( output )
        f.close ()
print ("Following module has been created:" + name)



myaddonpath = 'addons/'+new_module

print(myaddonpath)
print('日本語')

shutil.rmtree(myaddonpath, True)


shutil.copytree('src/templates/'+new_module, myaddonpath, symlinks=False, ignore=None)
