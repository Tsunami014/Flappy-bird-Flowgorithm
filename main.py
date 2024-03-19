import keyboard
from time import sleep
print('Now launch up a game! REMEMBER TO ALWAYS PRESS THE Q KEY TO EXIT THE PROGRAM!')
for key in list('failsafe'):
    while not keyboard.is_pressed(key):
        pass
keyboard.wait('enter')
while True:
    if keyboard.is_pressed('q'):
        break
    key = False
    if keyboard.is_pressed('up') or \
       keyboard.is_pressed('space') or \
       keyboard.is_pressed('enter'):
        
        key = True
    if key:
        keyboard.press_and_release(' ')
    keyboard.press_and_release('enter')
    sleep(0.1)
