#!/usr/bin/env python3

import time
import datetime
import shutil
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
import RPi.GPIO as GPIO
from picamera2 import Picamera2
import logging

PHOTO_DIR = Path("/home/pi/photos")
PHOTO_DIR.mkdir(parents=True, exist_ok=True)

BUTTON_PIN = 17
BAT_LOW_PIN = 26

RST_PIN = 24
DC_PIN = 25
CS_PIN = 8
BUSY_PIN = 23
SPI_CLK = 11
SPI_DIN = 10

DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 300
DISK_SPACE_THRESHOLD = 100 * 1024 * 1024

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    handlers=[logging.FileHandler("/home/pi/camera.log"), logging.StreamHandler()]
)
logger = logging.getLogger("papercam")

try:
    from waveshare_epd import epd4in2
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear()
    logger.info("E‑ink display initialized")
except Exception as e:
    logger.error(f"E‑ink init failed: {e}")
    epd = None

camera = Picamera2()
camera.configure(camera.create_still_configuration(main={"size": (4056, 3040)}, display=None))
camera.start()
time.sleep(2)
logger.info("Camera initialized")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BAT_LOW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
logger.info("GPIO setup complete")

def is_battery_low():
    return GPIO.input(BAT_LOW_PIN) == GPIO.LOW

def check_sd_space():
    _, _, free = shutil.disk_usage(str(PHOTO_DIR))
    return free > DISK_SPACE_THRESHOLD

def capture_photo():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = PHOTO_DIR / f"photo_{ts}.jpg"
    logger.info(f"Capturing {path.name}...")
    camera.capture_file(str(path))
    return path

def show_bitmap(img):
    if epd:
        epd.display(epd.getbuffer(img))

def display_message(text):
    if not epd:
        return
    
    img = Image.new('1', (DISPLAY_WIDTH, DISPLAY_HEIGHT), 255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    draw.text(((DISPLAY_WIDTH - w)//2, (DISPLAY_HEIGHT - h)//2), text, font=font, fill=0)
    show_bitmap(img)

def flash_once(img, delay=0.5):
    show_bitmap(img)
    time.sleep(delay)
    inv = ImageOps.invert(img.convert("L")).convert("1")
    show_bitmap(inv)
    time.sleep(delay)
    show_bitmap(img)

def display_sd_full():
    logger.warning("SD nearly full – displaying warning")
    display_message("SD CARD FULL")

def display_low_battery():
    logger.warning("Battery low – displaying warning")
    display_message("LOW BATTERY")

def display_ready():
    display_message("Ready")


if epd:
    display_ready()


def display_processing():
    if epd:
        display_message("PROCESSING...")

def process_and_display(photo_path):
    if not epd:
        return
    
    img = None
    bw = None
    try:
        display_processing()
        
        img = Image.open(photo_path).convert('L')
        img = ImageOps.fit(img, (DISPLAY_WIDTH, DISPLAY_HEIGHT), Image.Resampling.LANCZOS)
        bw = img.convert('1')
        show_bitmap(bw)
        logger.info("Displayed captured image")
    except Exception as e:
        logger.error(f"Display error: {e}")
    finally:
        for obj in (bw, img):
            try:
                obj and obj.close()
            except Exception:
                pass

def cleanup():
    GPIO.cleanup()
    try:
        camera.close()
    except Exception:
        pass
    if epd:
        try:
            epd.sleep()
        except Exception:
            pass
    logger.info("Shutdown complete")

def main():
    logger.info("PaperCam ready – waiting for button press")
    battery_warned = False
    last_battery_check = 0
    
    try:
        while True:
            current_time = time.time()
            
            if current_time - last_battery_check > 5:
                if is_battery_low():
                    if not battery_warned:
                        display_low_battery()
                        battery_warned = True
                        logger.warning("Battery low - photos may not save properly")
                else:
                    if battery_warned:
                        logger.info("Battery level recovered")
                    battery_warned = False
                last_battery_check = current_time

            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                time.sleep(0.1)
                if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                    if battery_warned:
                        logger.warning("Taking photo with low battery")
                    
                    if not check_sd_space():
                        display_sd_full()
                    else:
                        photo = capture_photo()
                        process_and_display(photo)
                    
                    while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                        time.sleep(0.1)
            
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt – shutting down")
    except Exception as e:
        logger.exception(f"Unhandled exception: {e}")
    finally:
        cleanup()

if __name__ == "__main__":
    main()