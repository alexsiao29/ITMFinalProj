import PySimpleGUI as sg

layout = [[sg.Text("Pick an Ateneo Food Stall")], [sg.Button("EBAIS")], [sg.Button("KRAVERS")],[sg.Button("GONZ")],[sg.Button("IGGY'S")]]
# Create the window
window = sg.Window("Eating in Ateneo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "KRAVERS":
        break
    else:
        break

window.close()