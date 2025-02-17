class ButtonManager:
    def __init__(self, button_pins):
        self.button_pins = button_pins
        self.setup_buttons()

    def setup_buttons(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        for pin in self.button_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def check_buttons(self):
        import RPi.GPIO as GPIO
        for index, pin in enumerate(self.button_pins):
            if GPIO.input(pin) == GPIO.LOW:  # Button pressed
                return index
        return None  # No button pressed