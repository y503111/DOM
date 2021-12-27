
#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


 #Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
   # while True:
        #for i in range(12):
       #while True:
    strip.setPixelColor(1, color)
    strip.setPixelColor(2, color)
    strip.setPixelColor(3, color)
    strip.setPixelColor(4, color)
    strip.setPixelColor(5, color)
    strip.setPixelColor(6, color)
    strip.show()
    time.sleep(wait_ms/1000.0)
        

def colorWipe1(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    #while True:
       # for i in range(12):
       #while True:
    strip.setPixelColor(7, color)
    strip.setPixelColor(8, color)
    strip.setPixelColor(9, color)
    strip.setPixelColor(10, color)
    strip.setPixelColor(11, color)
    strip.setPixelColor(12, color)
    strip.show()
    time.sleep(wait_ms/1000.0)
            
def colorWipe2(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    #while True:
       # for i in range(12):
       #while True:
    strip.setPixelColor(13, color)
    strip.setPixelColor(14, color)
    strip.setPixelColor(15, color)
    strip.setPixelColor(16, color)
    strip.setPixelColor(17, color)
    strip.setPixelColor(18, color)
    strip.show()
    time.sleep(wait_ms/1000.0)
            
def colorWipe3(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
   # while True:
       # for i in range(12):
       #while True:
    strip.setPixelColor(19, color)
    strip.setPixelColor(20, color)
    strip.setPixelColor(21, color)
    strip.setPixelColor(22, color)
    strip.setPixelColor(23, color)
    strip.setPixelColor(0, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

def left(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    #while True:
    #for i in range(12):
       #while True:
    strip.setPixelColor(0, color)
    strip.setPixelColor(1, color)
    strip.setPixelColor(2, color)
    strip.setPixelColor(3, color)
    strip.setPixelColor(4, color)
    strip.setPixelColor(5, color)
    strip.setPixelColor(6, color)
    strip.setPixelColor(7, color)
    strip.setPixelColor(8, color)
    strip.setPixelColor(9, color)
    strip.setPixelColor(10, color)
    strip.setPixelColor(11, color)
    strip.setPixelColor(12, color)
    strip.show()
    time.sleep(wait_ms/1000.0)
            
def right(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    #while True:
       # for i in range(12):
       #while True:
    strip.setPixelColor(12, color)
    strip.setPixelColor(13, color)
    strip.setPixelColor(14, color)
    strip.setPixelColor(15, color)
    strip.setPixelColor(16, color)
    strip.setPixelColor(17, color)
    strip.setPixelColor(18, color)
    strip.setPixelColor(19, color)
    strip.setPixelColor(20, color)
    strip.setPixelColor(21, color)
    strip.setPixelColor(22, color)
    strip.setPixelColor(23, color)
    strip.setPixelColor(24, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

def all(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    #while True:
    #for i in range(24):
       #while True:
    strip.setPixelColor(0, color)
    strip.setPixelColor(1, color)
    strip.setPixelColor(2, color)
    strip.setPixelColor(3, color)
    strip.setPixelColor(4, color)
    strip.setPixelColor(5, color)
    strip.setPixelColor(6, color)
    strip.setPixelColor(7, color)
    strip.setPixelColor(8, color)
    strip.setPixelColor(9, color)
    strip.setPixelColor(10, color)
    strip.setPixelColor(11, color)
    #strip.setPixelColor(12, color)
    strip.setPixelColor(12, color)
    strip.setPixelColor(13, color)
    strip.setPixelColor(14, color)
    strip.setPixelColor(15, color)
    strip.setPixelColor(16, color)
    strip.setPixelColor(17, color)
    strip.setPixelColor(18, color)
    strip.setPixelColor(19, color)
    strip.setPixelColor(20, color)
    strip.setPixelColor(21, color)
    strip.setPixelColor(22, color)
    strip.setPixelColor(23, color)
    strip.setPixelColor(24, color)
    #strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

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
        while x<10:
            
            print ('Color wipe animations.')
            x=int(input("Position waehlen : "))
            if x == 1:
                print("Bereich 1 gewaehlt")
                colorWipe(strip, Color(127, 127, 127))  # Blue wipe
                
            
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
               
                
            if x == 10:
                print("Kartoffel ")
                
            #colorWipe1(strip, Color(127, 127, 127))
            #colorWipe2(strip, Color(127, 127, 127))
            #colorWipe3(strip, Color(127, 127, 127))
            #left(strip, Color(127, 127, 127))
            #right(strip, Color(127, 127, 127))
           # colorWipe(strip, Color(0, 0, 255))  # Green wipe
      #      print ('Theater chase animations.')
       #     theaterChase(strip, Color(127, 127, 127))  # White theater chase
        #    theaterChase(strip, Color(127,   0,   0))  # Red theater chase
         #   theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
          #  print ('Rainbow animations.')
           # rainbow(strip)
            #rainbowCycle(strip)
            #theaterChaseRainbow(strip)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)

