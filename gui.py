import random
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text("Press Player too randomly select the person who will play killer")],
    [sg.Text("Press Killer for a random killer")],
    [sg.Image('Kicon.png')], 
    [sg.Button('Player', key='-START-'), sg.Button('Killer', key='-START2-')],
    [sg.Text('Output', key='-OUTPUT-')],
    [sg.Text('Output', key='-OUTPUT2-')]
]

# create the window
Window = sg.Window("Dead By daylight kyf rng", layout, margins=(30,15),resizable=False, finalize=True,)

# create an event loop
while True:
    event, values = Window.read()

# event for the player selection
    if event == '-START-':
        players = ['NAME HERE', 'NAME HERE', 'NAME HERE', 'NAME HERE']

        random_player = random.choice(players)

        Window['-OUTPUT-'].update(random_player)

# event for the random killer
    if event == '-START2-':
        f = open("killers.txt", 'r')
        killers = f.readlines()
        f.close()
        
        last = 27
        rnd = random.randint(0, last)

        Window['-OUTPUT2-'].update(killers[rnd])
        
# event closing the window
    if event == sg.WINDOW_CLOSED:
            break
Window.close()
