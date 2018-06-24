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
        output = template.render ( new_module='sumpurn_entry' )
        print(output)
        # file-output.py
        if not os.path.exists ( os.path.dirname ( 'src/' +  filepath ) ):
            os.makedirs ( os.path.dirname ('src/' +  filepath ) )
        f = open ( 'src/' + filepath, 'w' )

        f.write ( output )
        f.close ()
