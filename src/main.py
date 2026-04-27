from machine import Pin, ADC, PWM
import time

print("Teste")
print("Edge AI inspection simulator starting...")

# =========================
# Pin configuration
# =========================
BUTTON_PIN = 14
POT_PIN = 34

LED_GREEN_PIN = 25
LED_YELLOW_PIN = 26
LED_RED_PIN = 27

BUZZER_PIN = 33

DEBOUNCE_TIME = 300  # milliseconds
STATUS_INTERVAL = 1000  # milliseconds

# =========================
# Hardware setup
# =========================
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

pot = ADC(Pin(POT_PIN))
pot.atten(ADC.ATTN_11DB)

led_green = Pin(LED_GREEN_PIN, Pin.OUT)
led_yellow = Pin(LED_YELLOW_PIN, Pin.OUT)
led_red = Pin(LED_RED_PIN, Pin.OUT)

buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty(0)

# =========================
# System states
# =========================
STATE_IDLE = 0
STATE_READ = 1
STATE_PROCESS = 2
STATE_ACTUATE = 3

state = STATE_IDLE

last_press_time = 0
last_status_time = 0
current_class = 0
current_result = ""


def read_input():
    """Read analog value from potentiometer."""
    return pot.read()


def simulate_class(adc_value):
    """Map ADC range (0-4095) to class range (0-9)."""
    return int((adc_value / 4095) * 9)


def decide_state(cls):
    """Convert class into system decision."""
    if cls <= 3:
        return "APPROVED"
    elif cls <= 6:
        return "WARNING"
    else:
        return "REJECTED"


def update_outputs(result):
    """Update LEDs and buzzer based on system state."""
    led_green.off()
    led_yellow.off()
    led_red.off()
    buzzer.duty(0)

    if result == "APPROVED":
        led_green.on()
    elif result == "WARNING":
        led_yellow.on()
    elif result == "REJECTED":
        led_red.on()
        buzzer.freq(1000)
        buzzer.duty(512)


print("Teste - Edge AI inspection simulator started")

while True:
    now = time.ticks_ms()

    # Periodic log used by CI and serial monitoring
    if time.ticks_diff(now, last_status_time) > STATUS_INTERVAL:
        print("Teste - system running")
        last_status_time = now

    if state == STATE_IDLE:
        if not button.value() and time.ticks_diff(now, last_press_time) > DEBOUNCE_TIME:
            last_press_time = now
            state = STATE_READ

    elif state == STATE_READ:
        adc_value = read_input()
        current_class = simulate_class(adc_value)
        state = STATE_PROCESS

    elif state == STATE_PROCESS:
        current_result = decide_state(current_class)
        print("Class:", current_class, "| Result:", current_result)
        state = STATE_ACTUATE

    elif state == STATE_ACTUATE:
        update_outputs(current_result)
        state = STATE_IDLE
