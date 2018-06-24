#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

print "#################################################################"
print "# Simple es una aplicacion para generar Modulo para Odoo ERP    #"
print "# www.falconsolutions.cl                                        #"
print "# Autor: Marlon Falcon Herandez                                 #"
print "# mail: mfalcon@falconsolutions.cl                              #"
print "#################################################################"

# Enter the name of the module:
name = raw_input("Enter the name of the module:")
noOfFields = int( raw_input( "Number of fields:" ) )
print ""
print "###############  Fields  ##############################"
print ""
print ""
# Create the module
os.makedirs(name)
os.makedirs(name+"/views")
os.makedirs(name+"/models")

# Create the files
# Create __init__.py
file = open(name + '/__init__.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('import models \n')
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
file.write('    \'license\': \'Sumpurn runtime\',\n')
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
file.write('    _name = \'ej.'+name+'\' \n')
arreglo = []
for num in range( 1, noOfFields + 1 ):
    fname = raw_input("Name of the field:")
    print "Char,Text,Boolean,Datetime,Integer"
    ftipo = raw_input("Type of field:")
    print "-----------------------------------"
    print ""
    print ""
    file.write('    '+fname+' = fields.'+ftipo+'(string=\''+fname+'\', required=True) \n')
    file.write(' \n')
    arreglo.append(fname)
file.close()


# Create views _views.xml
file = open(name + '/views/'+ name + '_view.xml','w')
file.write('<?xml version="1.0" encoding="UTF-8"?> \n')
file.write('<odoo> \n')
file.write('<!-- Structure of the view --> \n')
file.write('     <record id="view_ej_' + name + '_form" model="ir.ui.view"> \n')
file.write('        <field name="name">ej.' + name + '.form</field> \n')
file.write('        <field name="model">ej.' + name + '</field> \n')
file.write('        <field name="arch" type="xml"> \n')
file.write('            <form string="Listado de '+name.capitalize()+'"> \n')
file.write('                <group> \n')
for fname in arreglo:
    file.write('                    <field name="'+fname+'"/> \n')
file.write('                </group> \n')
file.write('            </form> \n')
file.write('        </field> \n')
file.write('    </record> \n')

file.write('     <record id="view_ej_' + name + '_tree" model="ir.ui.view"> \n')
file.write('        <field name="name">ej.' + name + '.tree</field> \n')
file.write('        <field name="model">ej.' + name + '</field> \n')
file.write('        <field name="arch" type="xml"> \n')
file.write('           <tree> \n')
for fname in arreglo:
    file.write('                    <field name="'+fname+'"/> \n')
file.write('           </tree> \n')
file.write('        </field> \n')
file.write('    </record> \n')

# Structure of the actions
file.write('    <record model="ir.actions.act_window" id="act_ej_' + name + '"> \n')
file.write('        <field name="name">' + name + '</field> \n')
file.write('        <field name="type">ir.actions.act_window</field> \n')
file.write('        <field name="res_model">ej.' + name + '</field> \n')
file.write('        <field name="view_type">form</field> \n')
file.write('        <field name="view_mode">tree,form</field> \n')
file.write('    </record> \n')

# Structure of the Menu
file.write('<!--  Declare the Menus --> \n')
file.write('<menuitem id="ej_' + name + '_menu" name="' + name.capitalize() + '" sequence="10"/> \n')
file.write('<menuitem id="submenu_ej_' + name + '_menu" name="'+ name.capitalize() +'" sequence="10" parent="ej_' + name + '_menu"/> \n')
file.write('<menuitem id="submenu_ej_' + name + '_action" name="'+ name.capitalize() + '" sequence="10" parent="submenu_ej_' + name + '_menu" action="act_ej_' + name + '"/> \n')

file.write('</odoo> \n')
file.close()

print "Following module has been created:" + name





