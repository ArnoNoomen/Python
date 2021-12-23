
import PySimpleGUI as sg
import runpy
from PySimpleGUI.PySimpleGUI import ListOfLookAndFeelValues
import b64image

sg.theme('LightPurple')

while(True):
	data =  ['Receiving', 'Receiving Pallets', 'Receiving MDA','Unloading', 'Unloading LCL']
	layout=[
			[sg.Listbox(values= data, select_mode='extended', key='fac', size=(15, 8) , font=('Times New Roman',35))],
			[sg.Button('',image_data=b64image.ok,key='START'),
			 sg.Button('',image_data=b64image.cancel,key='CANCEL'),
			 sg.Button('',image_data=b64image.pw,key='LOGIN')]
			]

	win = sg.Window('Select the procedure',layout,no_titlebar=True,size=(370, 550))
	
	e,v=win.read()
	win.close()
	
	if e == 'CANCEL':
		exit()

	if e == 'START':
		runpy.run_module(mod_name='receiving')

	if e == 'LOGIN':
		runpy.run_module(mod_name='login')
		

		
		

           

		



		

		

