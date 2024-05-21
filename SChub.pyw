import keyboard as kb
import subprocess as sp
import PySimpleGUI as sg

layout = [[sg.Text('Welcome to the shortcut shortcut station!')], [sg.Button("Testing Button")]]

while True:
        if(kb.is_pressed('ctrl+alt+k')):
            window = sg.Window('Shortcut Station', layout)
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == "Testing Button":
                    sp.Popen(['D:/Steam Games/steamapps/common/Stardew Valley/Stardew Valley.exe', '-new-window'])
        
    