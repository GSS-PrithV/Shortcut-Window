import keyboard as kb
import subprocess as sp
import PySimpleGUI as sg
import fileinput 

SC_List = {} #List of Shortcuts 


print(SC_List)

def make_window(): #creates the window for the GUI

    layout = [
     [sg.Text('Welcome to the shortcut shortcut station!')],
     [sg.Text('Enter the name of the shortcut you want to add and the path of the file you want to open')],
     [sg.InputText(key="-SHORTCUT_NAME-")],
     [sg.InputText(key="-FILE_PATH-"),
      sg.FileBrowse(initial_folder="C:\\Users\\Public\\Desktop", file_types=(("Executables", "*.exe"),))],
     [sg.Button('Submit')]
    ]

    for line in fileinput.input("executables.txt"): #creates Shortcut list 
        SC_List[line.split(",")[0]] = line.split(",")[1][:-1]

    for key in SC_List: #Creates a button for each shortcut, will change once I figure out how to add shortcuts in GUI
        layout.append([sg.Button(key)])

    return sg.Window('Shortcut Station', layout)


while True: #Main loop
        if(kb.is_pressed('ctrl+alt+k')):
            window = make_window()
            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED: #when window is closed
                    print("Window Closed")
                    break

                if event == "Submit": #when user inputs a file path for an .exe
                    # print(values["-SHORTCUT_NAME-"])
                    # print(values["-FILE_PATH-"])
                    file = open("executables.txt", "a")
                    file.write(values["-SHORTCUT_NAME-"] + "," + values["-FILE_PATH-"] + "\n")
                    file.close()
                    window.close()
                    window = make_window()

                if SC_List.get(event) != None: #when user clicks a shortcut button
                    print(SC_List[event])
                    sp.Popen([SC_List[event], '-new-window'])
        
    