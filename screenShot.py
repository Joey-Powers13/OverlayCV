from PIL import ImageGrab
import time

# Get a screenshot of the screen in order to use it in the overlay

def screenShot():
    time.sleep(5)
    image = ImageGrab.grab()
    image.save("/Users/powers/OverlayCV/screenshot.png")

screenShot()