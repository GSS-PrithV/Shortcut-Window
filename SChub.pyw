import keyboard as kb
import subprocess as sp
import PySimpleGUI as sg

SC_List = { #List of Shortcuts TODO: Add more shortcuts and add a way to add more shortcuts in GUI
     "Stardew Valley": "D:/Steam Games/steamapps/common/Stardew Valley/Stardew Valley.exe", 
     "Geometry Dash": "D:/Steam Games/steamapps/common/Geometry Dash/GeometryDash.exe",
     "Stick Notes": "stickycut.exe",
     }


def make_window():
    layout = [[sg.Text('Welcome to the shortcut shortcut station!')]]

    for key in SC_List: #Creates a button for each shortcut, will change once I figure out how to add shortcuts in GUI
        layout.append([sg.Button(key)])

    return sg.Window('Shortcut Station', layout)

while True: #Main loop
        if(kb.is_pressed('ctrl+alt+k')):
            window = make_window()
            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED:
                    print("Window Closed")
                    break
                if SC_List.get(event) != None:
                    print(SC_List[event])
                    sp.Popen([SC_List[event], '-new-window'])
        
    