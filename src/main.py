import RPi.GPIO as GPIO
import time
from config import BUTTON_PINS, DEBOUNCE_TIME, PWM_PIN
from audio import speak_phrase

def button_callback(channel):
    button_index = BUTTON_PINS.index(channel)
    print(f"Button {button_index + 1} (GPIO {channel}) pressed")
    speak_phrase(button_index)

def setup():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    for pin in BUTTON_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback, bouncetime=DEBOUNCE_TIME)

def main():
    setup()
    try:
        while True:
            time.sleep(1)
            print("Waiting for button press...")
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()