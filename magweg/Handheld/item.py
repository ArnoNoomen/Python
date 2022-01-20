
import PySimpleGUI as sg
import b64image

sg.theme('LightPurple')

text_list = []

sg.set_options(font=('Helvetica', 25))
layout = [
            [sg.Text('Item:',size=(20,1))],
            [sg.InputText(key='item',size=(20,1),enable_events=True)],
            [sg.Listbox(values=text_list,size=(20,9),  change_submits=True,
                                                  bind_return_key=True,
                                             auto_size_text=True,
                                             key='_FLOATING_LISTBOX_', enable_events=True)],
            [sg.Button('',image_data=b64image.ok),sg.Button('',image_data=b64image.cancel,key='Quit'),sg.Button('',image_data=b64image.list)]
            
         ]
window = sg.Window('Items on receipt', layout, finalize=True,no_titlebar=True,size=(370, 550))
window.SetIcon('bol.ico')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break

    if len(values['item']) and values['item'][-1] not in ('0123456789'):
        window['item'].update(values['item'][:-1])
    
    if len(values['item']) > 14:
        sg.popup('Item too long ',no_titlebar=True)  
        window['item'].update(values['item'][:-1])      
    
window.close()