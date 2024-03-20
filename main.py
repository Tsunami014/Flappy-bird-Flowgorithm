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
    if keyboard.is_pressed('up') or \
       keyboard.is_pressed('w') or \
       keyboard.is_pressed('space') or \
       keyboard.is_pressed('enter'):
        
        keyboard.press_and_release('w')
    
    if keyboard.is_pressed('left') or \
       keyboard.is_pressed('d'):
        
        keyboard.press_and_release('d')
    
    if keyboard.is_pressed('right') or \
       keyboard.is_pressed('a'):
        
        keyboard.press_and_release('a')
    
    keyboard.press_and_release('enter')
    sleep(0.3)
