import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO PIN CONNECTIONS
_VISIBLE_LED = 18
_IR_LED = 4

# take control over system LEDs. Power and OK LEDs
GPIO.setup(_VISIBLE_LED, GPIO.OUT)
GPIO.setup(_IR_LED, GPIO.OUT)

def turn_on_visible_led():
    GPIO.output(_VISIBLE_LED, GPIO.HIGH)


def turn_off_visible_led():
    GPIO.output(_VISIBLE_LED, GPIO.LOW)


def turn_on_ir_led():
    GPIO.output(_IR_LED, GPIO.HIGH)


def turn_off_ir_led():
    GPIO.output(_IR_LED, GPIO.LOW)
