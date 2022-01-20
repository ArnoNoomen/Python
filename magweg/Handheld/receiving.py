
import PySimpleGUI as sg
import runpy
from PySimpleGUI.PySimpleGUI import Output
import b64image

sg.theme('LightPurple')

text_list=[ ' ', 'Receipt selected']

sg.set_options(font=('Helvetica', 25))
layout = [
            [sg.Text('Receipt:',size=(20,1))],
            [sg.InputText(key='receipt',enable_events=True,size=(20,1))],
            [sg.Listbox(values=text_list,size=(20,7),  change_submits=True,
                                                  bind_return_key=True,
                                             auto_size_text=True,
                                             key='listbox', enable_events=True)],
            [sg.Text('Dock:',size=(20,1))],
            [sg.Combo(['DOCK.EXC','DOCK133'],key='dock',enable_events=True,size=(20,1))],
            [sg.Button('',image_data=b64image.cancel,key='Quit'),
             sg.Button('',image_data=b64image.ok,key='Ok'),
             sg.Button('',image_data=b64image.item,key='Item')
            ]
         ]
window = sg.Window('Receipt to Proces', layout, finalize=True,no_titlebar=True,size=(370, 550))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    if event in (sg.WIN_X_EVENT, 'Item'):
        window.close()
        runpy.run_module(mod_name='item')
    
    if len(values['receipt']) and values['receipt'][-1] not in ('0123456789'):
        window['receipt'].update(values['receipt'][:-1])
           
    if event in (sg.WIN_X_EVENT, 'Ok'):
        if len(values['receipt']) == 0:
            sg.popup('No receipt ',no_titlebar=True)
        if len(values['dock']) == 0:
            sg.popup('No dock ',no_titlebar=True)

        # window['listbox'[0]].update(values['listbox'][0]['jaja'])

window.close()