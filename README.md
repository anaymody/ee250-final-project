# ee250-final-project
Anay Mody and Jalan Zhu

To run our project, first run server.py in a VM. Also run rpi.py in a raspberry pi. Once running, press the first button to retrieve a piece of advice from the API. This will take several seconds. After the encryption and decryption finishes, you will see the advice begin to scroll on the LCD connected to the RPi. If you would like to save this piece of advice, hit the second button. This will save the piece of advice to the HTML file. Refreshing the HTML file will update the page to show the newly added piece of advice. 


external libraries used: RSA, paho, grovepi, cryptography, requests