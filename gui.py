import random
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Window normal', size=(30, 1), key='Status')],
    [sg.Text("Press start too randomly select a killer for your lobby")],
    [sg.Image('Kicon.png')], 
    [sg.Button('Start',)],
    [sg.Text('Output', key='Output')],
]

# create the window
Window = sg.Window("Dead By daylight kyf rng", layout, resizable=True, finalize=True,)
Window.bind('<Configure>', "Configure")
status = Window['Status']

# create an event loop
while True:
    event, values = Window.read()
    if event == 'Start':
        players = ['NAME', 'NAME', 'NAME', 'NAME']

        random_killer = random.choice(players)

        Window['Output'].update(random_killer)

    # events for resize and closing the window
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Configure':
        if Window.TKroot.state() == 'zoomed':
            status.update(value='Window zoomed and maximized !')
        else:
            status.update(value='Window normal')

Window.close()
