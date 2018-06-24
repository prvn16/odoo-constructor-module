#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os, shutil

import templates as templates

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
name = values[0][1]
noOfFields = len(values[1])-1

# Create the module
dirs = [name, name+"/views", name+"/models"]
for directory in dirs :
    if not os.path.exists(directory):
        os.makedirs(directory)


# Create the files
# Create __init__.py
file = open(name + '/__init__.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('from . import models \n')
file.close()


# Create __manifest__.py
file = open(name + '/__manifest__.py','w')
file.write('# -*- coding: utf-8 -*-\n')
file.write('##############################################################################\n')
file.write('#\n')
file.write('#    Automatic creation of modules for Odoo \n')
file.write('#\n')
file.write('##############################################################################\n')
file.write('{\n')
file.write('    \'name\': \'' + name + ' Sumpurn\',\n')
file.write('    \'version\': \'10.0.0.1.0\',\n')
file.write('    \'author\': "Nihon Sumpurn Tsushin Giken...",\n')
file.write('    \'maintainer\': \'Dr. Praveen Bhatia\',\n')
file.write('    \'website\': \'http://www.sumpurn.com\',\n')
file.write('    \'license\': \'AGPL-3\',\n')
file.write('    \'category\': \'account.payment\',\n')
file.write('    \'summary\': \'Sumpurn automatic module builder\',\n')
file.write('    \'depends\': [\'account\',\'account_accountant\'],\n')
file.write('    \'description\': """\n')
file.write('Module base\n')
file.write('===================================================== \n')
file.write('Selections for the module \n')
file.write('""",\n')
file.write('    \'demo\': [],\n')
file.write('    \'test\': [],\n')
file.write('    \'data\': [\'views/'+ name + '_view.xml\',],\n')
file.write('    \'installable\': True,\n')
file.write('    \'auto_install\': False,\n')
file.write('}\n')
file.close()

mymap = {'TRUE': 'True'}
# Create the Model
file = open(name + '/models/__init__.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('import '+name+' \n')
file.close()

# Create the Model
file = open(name + '/models/'+name+'.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('# See LICENSE file for full copyright and licensing details. \n')
file.write('from odoo import api, fields, models \n')
file.write('from datetime import datetime \n')
file.write('\n')
file.write('class '+name+'(models.Model): \n')
file.write('    _name = \'' + name +'.' + name + "' \n" )
arreglo = []
for num in range( 1, noOfFields + 1 ):
    fname = values[1][num]

    ftipo = values[2][num]

    file.write('    '+fname+' = fields.'+ftipo+'(string=\''+fname+'\', required='+mymap[values[3][num]]+') \n')
    file.write(' \n')
    arreglo.append(fname)
file.close()


# Create views _views.xml
file = open(name + '/views/'+ name + '_view.xml','w')
file.write('<?xml version="1.0" encoding="UTF-8"?> \n')
file.write('<odoo> \n')
file.write('<!-- Structure of the view --> \n')
file.write('     <record id="view__' + name + '_form" model="ir.ui.view"> \n')
file.write('        <field name="name">' + name + '.form</field> \n')
file.write('        <field name="model">' + name + '.' + name + '</field> \n')
file.write('        <field name="arch" type="xml"> \n')
file.write('            <form string="Listado de '+name.capitalize()+'"> \n')
file.write('                <group> \n')
for fname in arreglo:
    file.write('                    <field name="'+fname+'"/> \n')
file.write('                </group> \n')
file.write('            </form> \n')
file.write('        </field> \n')
file.write('    </record> \n')

file.write('     <record id="view__' + name + '_tree" model="ir.ui.view"> \n')
file.write('        <field name="name">' + name + '.tree</field> \n')
file.write('        <field name="model">' + name + '.' + name + '</field> \n')
file.write('        <field name="arch" type="xml"> \n')
file.write('           <tree> \n')
for fname in arreglo:
    file.write('                    <field name="'+fname+'"/> \n')
file.write('           </tree> \n')
file.write('        </field> \n')
file.write('    </record> \n')

# Structure of the actions
file.write('    <record model="ir.actions.act_window" id="act_' + name + '"> \n')
file.write('        <field name="name">' + name + '</field> \n')
file.write('        <field name="type">ir.actions.act_window</field> \n')
file.write('        <field name="res_model">' + name + '.' + name + '</field> \n')
file.write('        <field name="view_type">form</field> \n')
file.write('        <field name="view_mode">tree,form</field> \n')
file.write('    </record> \n')

# Structure of the Menu
file.write('<!--  Declare the Menus --> \n')
file.write('<menuitem id="' + name + '_menu" name="' + name.capitalize() + '" sequence="10"/> \n')
file.write('<menuitem id="submenu_' + name + '_menu" name="'+ name.capitalize() +'" sequence="10" parent="' + name + '_menu"/> \n')
file.write('<menuitem id="submenu_' + name + '_action" name="'+ name.capitalize() + '" sequence="10" parent="submenu_' + name + '_menu" action="act_' + name + '"/> \n')

file.write('</odoo> \n')
file.close()

print ("Following module has been created:" + name)



myaddonpath = 'addons/'+name

print(myaddonpath)
print('日本語')

shutil.rmtree(myaddonpath, True)


shutil.copytree(name, myaddonpath, symlinks=False, ignore=None)

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname ( os.path.abspath ( __file__ ) )
print(PATH)
TEMPLATE_ENVIRONMENT = Environment (
    autoescape=False,
    loader=FileSystemLoader ( os.path.join ( PATH, 'templates' ) ),
    trim_blocks=False )


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template ( template_filename ).render ( context )


def create_index_html():
    fname = "output.html"
    urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
    context = {
        'urls': urls
    }
    #
    with open ( fname, 'w' ) as f:
        html = render_template ( 'index.html', context )
        f.write ( html )



