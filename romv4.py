#!/usr/bin/env python
# -*- coding: utf8 -*-
import RPi.GPIO as GPIO
import SimpleMFRC522
import MFRC522
import subprocess

continue_reading = True
MIFAREReader = MFRC522.MFRC522()
reader = SimpleMFRC522.SimpleMFRC522()
def getEmulatorpath(console):
    path = "/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ " + console + " "
    return path

def getGamePath(console, game):
    
    game = game.replace(" ", "\ ")
    game = game.replace("(", "\(")
    game = game.replace(")", "\)")
    game = game.replace("'", "\\'")
    game = game.replace("#", " ")

    gamePath = "/home/pi/RetroPie/roms/" + console + "/" + game
    return gamePath

emulators = ["SMYI", "b", "apple2", "arcade", "atari800", "atari2600", "atari5200", "atari7800",
                 "atarilynx", "atarist", "c64", "coco", "dragon32", "dreamcast", "fba", "fds", "gamegear", "gb", "gba",
                 "gbc", "intellivision", "macintosh", "mame-advmame", "mame-libretro", "mame-mame4all", "mastersystem",
                 "megadrive", "msx", "n64", "neogeo", "nes", "ngp", "ngpc", "pc", "ports", "psp", "psx", "scummvm",
                 "sega32x", "segacd", "sg-1000", "snes", "vectrex", "videopac", "wonderswan", "wonderswancolor",
                 "zmachine", "zxspectrum"]

while continue_reading:
       (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

       if status == MIFAREReader.MI_OK:
           
                 id, text = reader.read()

                 if text[:4] == "snes":
           

                   console = text[:4]
                   game = text[4:]
                 
               
                   if console in emulators:
                      print("cargando")
                      subprocess.call(getEmulatorpath(console) + getGamePath(console, game), shell=True)
                      continue_reading = False                
                
                                              
       else:
                 print "inserte cartucho"
                 continue_reading = False

                 GPIO.cleanup()
continue_reading = False



