import sys, os, time, json, subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
ti = 0
i = 1

while True:
    
         if GPIO.input(2) == False:
           
                        # we held the reset button then we want to write to the nfc, else we reset the rom
            if ti < 1:
                if GPIO.input(2) == False:
                     print("encendido")
                     os.system("sudo killall emulationstation && sleep 1s && sudo openvt -c 1 -s -f emulationstation 2>&1")

                     time.sleep(.3)
                     ti = ti + i
                     print(ti)
                     

    
         if GPIO.input(2) == False:
           
                        # we held the reset button then we want to write to the nfc, else we reset the rom
            if ti == 1:
                if GPIO.input(2) == False:
                     print("Apagadp")
                     os.system("sudo killall retroarch && sudo emulationstation")

                     time.sleep(.3)
                     ti = ti - i
                     print(ti)
                     
          