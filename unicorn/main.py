from time import sleep
import machine
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN as DISPLAY
from stellar import StellarUnicorn
import jpegdec

# overclock to 200Mhz
machine.freq(200000000)

# some basic parameters (note: 1.0 bright is VERY bright)
MAX_BRIGHT = 0.6 
DISPLAY_SECS = 20
INTERVAL_SECS = 10

# could make this a directory to cycle through
# images already resized to 16x16 pixels for Stellar
files = [ "logo3.jpeg", "mascot3.jpeg" ]


stellar = StellarUnicorn()
graphics = PicoGraphics(DISPLAY)


def show_image(filename):
    j = jpegdec.JPEG(graphics)
    j.open_file(filename)
    j.decode(0,0,jpegdec.JPEG_SCALE_FULL)
    stellar.set_brightness(MAX_BRIGHT)
    stellar.update(graphics)

def fade_image():
    # poor man's quick fade routine
    for n in range (MAX_BRIGHT*10,-1,-1):
        stellar.set_brightness(n/10)
        stellar.update(graphics)
        sleep(2.7*(n/10))
        if n == 1:
            stellar.clear()


while True:
    for f in files:
        print(f"Show {f}")
        show_image(f)
        sleep(DISPLAY_SECS)
        fade_image()
        sleep(INTERVAL_SECS)
    