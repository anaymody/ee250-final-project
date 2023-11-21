import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

# Modules for my apps
#import my_app  # TODO: Create my_app.py using another API, following the examples as a template
import app

PORT_BUZZER = 2     # D2
PORT_BUTTON = 4     # D4

LCD_LINE_LEN = 16

# Setup
grovepi.pinMode(PORT_BUZZER, "OUTPUT")
grovepi.pinMode(PORT_BUTTON, "INPUT")

lcd.setRGB(0, 128, 0)

# Installed Apps!
# APPS = [
#     # TODO: Add your new app here
#     app.MY_APP
# ]

advice = app.MY_APP

CACHE = '  ' + advice['init']()

# app = 0     # Active app
ind = 0     # Output index

potentiometer = 0
grovepi.pinMode(potentiometer, "INPUT")


while True:
    try:
        # Check for input
        if grovepi.digitalRead(PORT_BUTTON):
            # BEEP!
            grovepi.digitalWrite(PORT_BUZZER, 1)
            advice = app.MY_APP
            print(advice)

            # Switch app
            # app = (app + 1) % len(APPS)
            ind = 0
        
        curr_threshold = round((grovepi.analogRead(potentiometer) / 1023 * 5)) #400 is the max range
        if curr_threshold == 0:
            lcd.setRGB(0,0,0)
        elif curr_threshold == 1:
            lcd.setRGB(0,0,255)
        elif curr_threshold == 2:
            lcd.setRGB(0,255,0)
        elif curr_threshold == 3:
            lcd.setRGB(255,0,0)
        elif curr_threshold == 4:
            lcd.setRGB(0,255,255)
            


        time.sleep(0.1)

        grovepi.digitalWrite(PORT_BUZZER, 0)

        # Display app name
        lcd.setText_norefresh(advice['name'])

        # Scroll output
        lcd.setText_norefresh('\n' + CACHE[ind:ind+LCD_LINE_LEN])
        # TODO: Make the output scroll across the screen (should take 1-2 lines of code)
        # for i in range(65):
            # delay(150)
            # lcd.setText_norefresh('\n' + CACHE[app][ind:ind+LCD_LINE_LEN])
        ind += 1

    except KeyboardInterrupt:
        # Gracefully shutdown on Ctrl-C
        lcd.setText('')
        lcd.setRGB(0, 0, 0)

        # Turn buzzer off just in case
        grovepi.digitalWrite(PORT_BUZZER, 0)

        break

    except IOError as ioe:
        if str(ioe) == '121':
            # Retry after LCD error
            time.sleep(0.25)

        else:
            raise
