import cmd
import textwrap
import sys
import os
import time
import random
screen_width = 100
"""
##### Player setup #####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status = []
myPlayer = player()

##### Title Screen #####
def title_screen_selections():
    title_screen()
    option = input(">")
    if option.lower() == ("play"):
        start_game() #placeholder
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        option = input(">")
        if option.lower() == ("play"):
            start_game() #placeholder
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('######################')
    print('# Welcome :DDDDDDDDD #')
    print('######################')
    print('       - Play -       ')
    print('       - Help -       ')
    print('       - Quit -       ')
  
def help_menu():
    print('######################')
    print('# Welcome :DDDDDDDDD #')
    print('######################')
    print('- Use Up, Down, Left, Right to move -')
    print('- Use "look" to inspect -')

#main code
title_screen_selections()
"""

import PySimpleGUI as gui

gui.change_look_and_feel("DarkBlue")

layout = [
            [gui.Output(key="-OUTPUT-", size=(110, 30), font=("Helvetica 10"), text_color="white", background_color="black")],
            [gui.MLine(size=(60, 5), enter_submits=True, key="-QUERY-", do_not_clear=False)],
            [gui.Button("Perform Action", key="-SEND-", button_color=(gui.YELLOWS[0], gui.BLUES[0]), bind_return_key=True)],
            [gui.Button("Exit Game", key="-EXIT-", button_color=(gui.YELLOWS[0], gui.GREENS[0]))]
          ]

window = gui.Window("Placeholder", layout, font=("Helvetica", " 13"), default_button_element_size=(8, 2))
window.Finalize()

window["-OUTPUT-"].update("Welcome to TextRPG.\nType help for available commands.\n")

while True:
    event, value = window.read();
    if event in (None, "-EXIT-"):
        break
    if event == "-SEND-":
        query = value["-QUERY-"]
        print("Command = {}".format(query))


