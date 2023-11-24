import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

# Modules for my apps
#import my_app  # TODO: Create my_app.py using another API, following the examples as a template
import app

GEN_ADVICE = 4     # D4
SAVE_ADVICE = 2     # D2

LCD_LINE_LEN = 16

# Setup
grovepi.pinMode(SAVE_ADVICE, "INPUT")
grovepi.pinMode(GEN_ADVICE, "INPUT")

lcd.setRGB(0, 128, 0)

advice = app.MY_APP

CACHE = '  ' + advice['init']()

ind = 0     # Output index
saved = False

potentiometer = 0
grovepi.pinMode(potentiometer, "INPUT")


while True:
    try:
        # Check for input
        if grovepi.digitalRead(GEN_ADVICE):
            advice = app.MY_APP
            CACHE = '  ' + advice['init']()

            # Reset index
            ind = 0
            saved = False

        if grovepi.digitalRead(SAVE_ADVICE) and not saved:
            print(CACHE[2:])
            saved = True


        time.sleep(0.1)


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
        grovepi.digitalWrite(SAVE_ADVICE, 0)

        break

    except IOError as ioe:
        if str(ioe) == '121':
            # Retry after LCD error
            time.sleep(0.25)

        else:
            raise
