
import PySimpleGUI as sg
import b64image

sg.theme('LightPurple')

sg.set_options(font=('Helvetica', 25))
layout = [
            [sg.Text('User:',size=(20,1))],
            [sg.InputText(key='User',size=(20,1))],
            [sg.Text('Passwd:',size=(20,1))],
            [sg.InputText(key='Passwd',size=(20,1))],
             [sg.Text('',size=(20,7))],
          
            [sg.Button('',image_data=b64image.ok),
             sg.Button('',image_data=b64image.cancel,key='Quit'),
            ]
            
         ]
window = sg.Window('Login', layout, finalize=True,no_titlebar=True,size=(370, 550))
window.SetIcon('bol.ico')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    
window.close()