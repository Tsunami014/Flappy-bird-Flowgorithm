import keyboard
from time import sleep
print('Press enter to play! BE CAREFUL, PRESSING ENTER ANYWHERE ELSE WILL BREAK YOUR COMPUTER')
for key in list('failsafe'):
    keyboard.wait(key)
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
        keyboard.press_and_release('w')
    keyboard.press_and_release('enter')
    sleep(0.1)
