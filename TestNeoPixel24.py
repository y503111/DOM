

# rpi_ws281x library example


import time
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 60      # Anazahl NeoPixel
LED_PIN        = 18      # Gewaehlter GPIO pin
LED_FREQ_HZ    = 800000  # LED signal Frequenz in Hertz (800khz)
LED_DMA        = 10      # DMA (Direkt Memory Acces) channel (10 vom Hersteller empfohlen)
LED_BRIGHTNESS = 255     # Helligkeit von 0 bis max. 255
LED_INVERT     = False   # Invertiertes Signal für Transistorschaltung
LED_CHANNEL    = 0       # auf '1' setzten wenn GPIOs 13, 19, 41, 45 oder 53 genutzt werden sollen


def colorWipe(strip, color, wait_ms=50):
    i = 0
    for i in range(15):                                 #Angabe wie viele Neopixel angesteuert werden sollen
        i = i+1                                         #Position für den Ersten NeoPixel der angestuert werden soll 
        strip.setPixelColor(i, color)                   #den Anzusteuernden Pixeln die Farbwerte übergeben
        strip.show()                                    #Pixel Ansteuern
        

def colorWipe1(strip, color, wait_ms=50):
    i = 0
    for i in range(15):
        i = i+16
        strip.setPixelColor(i, color)
        strip.show()
            
def colorWipe2(strip, color, wait_ms=50):
    i = 0
    for i in range(15):
        i = i+31
        strip.setPixelColor(i, color)
        strip.show()
            
def colorWipe3(strip, color, wait_ms=50):
     i = 0
     for i in range(15):
        i = i+46
        strip.setPixelColor(0, color)
        strip.setPixelColor(i, color)
        strip.show()

def left(strip, color, wait_ms=50):
    i = 0
    for i in range(30):
        i=i+1
        strip.setPixelColor(i, color)
        strip.show()
            
def right(strip, color, wait_ms=50):
    i = 0
    for i in range(30):
        i= i+31
        strip.setPixelColor(0, color)
        strip.setPixelColor(i, color)
        strip.show()

def all(strip, color, wait_ms=50):
    i = 0
    for i in range(60):
        strip.setPixelColor(i, color)
        strip.show()
 

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        x=1                                                     
        while x<9:                                      #Nur Eingaben kleiner 9 werden verarbeitet                                         
            
            print ('Dom Beleuchtung')
            x=int(input("Position waehlen : "))         #Aufforderung im Terminal ausgeben
            if x == 1:                                  #Eingabe vergleichen
                print("Bereich 1 gewaehlt")             #Konsolenausgabe welcher Bereich gaehlt wurde
                colorWipe(strip, Color(127, 127, 127))  #Farbwerte Vergeben 
                
            
            if x == 2:
                print("Bereich 2 gewaehlt")
                colorWipe1(strip, Color(127, 127, 127))
                
            
            if x == 3:
                print("Bereich 3 gewaehlt")
                colorWipe2(strip, Color(127, 127, 127))
                
            if x == 4:
                print("Bereich 4 gewaehlt")
                colorWipe3(strip, Color(127, 127, 127))
            
            if x == 5:
                print("Bereich 5 gewaehlt")
                left(strip, Color(127, 127, 127))
                
            if x == 6:
                print("Bereich 6 gewaehlt")
                right(strip, Color(127, 127, 127))
                
            if x == 7:
                print("Bereich 7 gewaehlt")
                all(strip, Color(127, 127, 127))
                
                
            if x == 8:
                print("Ausschalten ")
                all(strip, Color(0,0,0))
               

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)

