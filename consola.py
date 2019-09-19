#!/usr/bin/env python
# -*- coding: utf8 -*-

#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import SimpleMFRC522
print("Grabando Juego")
time.sleep(1.10)

reader = SimpleMFRC522.SimpleMFRC522()
f = open ('/dev/shm/runcommand.info','r+')
gameData = {'console':'','rom':''}
content = []
n = "#########################################"
try:
       
       content = f.readlines()
       
       filename = content[2]
       gameData['console'] = content[0].replace('\n','')
       gameData['rom'] = filename.rpartition('/')[2].replace('\n','')

       
       reader.write(gameData['console'] + gameData['rom'] + n)
       
       print("Grabado")
       print(gameData['rom'])
       time.sleep(2.10)

finally:
        GPIO.cleanup()