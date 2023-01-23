import os
os.system('cls')

import pygame
import win32api
import win32gui
from subprocess import call

def mute():
    win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)


WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

hwnd_active = win32gui.GetForegroundWindow()


pygame.init()
xbox_joystick = pygame.joystick.Joystick(0)
xbox_joystick.init()

ps_joystick = pygame.joystick.Joystick(1)
ps_joystick.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:

                #XBOX
                if event.joy == 0:
                    if event.button == 1:
                        print("Xbox: Button: ", event.button, 'pressed')
                        mute()
                    else: 
                        print("Xbox: Button: ", event.button, 'pressed')

                #PS
                elif event.joy == 1:
                    if event.button == 6:
                        print("PS: Button: ", event.button, 'pressed')
                        mute()
                    else: 
                        print("PS: Button: ", event.button, 'pressed')
                    
except KeyboardInterrupt:
    print("EXITING NOW")
    xbox_joystick.quit()
    ps_joystick.quit()
    os.system('python menu.py')

    #exec(open('Menu.py').read())


'''elif event.type == pygame.JOYBUTTONDOWN:
                print(event.dict, event.joy, event.button, 'pressed')'''
