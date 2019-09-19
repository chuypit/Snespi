#!/usr/bin/env python
# -*- coding: utf8 -*-

#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
f = open ('/home/pi/Nespi/list.txt','r+')

try:



        id, text = reader.read()
        i = f.read(64)
        print(text)
        print(i)



finally:
        GPIO.cleanup()