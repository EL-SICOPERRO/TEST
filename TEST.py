import lgpio
import time

# --- PIN ASSIGNMENT ---
STEP = 18
DIR  = 4
ENA  = 22

# --- STEP SPEED ---
DELAY = 0.002   # 2 ms HIGH + 2 ms LOW = 250 steps/s (safe speed)

# Open RP1 GPIO chip
h = lgpio.gpiochip_open(0)

# Set pins as outputs
lgpio.gpio_claim_output(h, STEP)
lgpio.gpio_claim_output(h, DIR)
lgpio.gpio_claim_output(h, ENA)

# Enable driver
lgpio.gpio_write(h, ENA, 1)     # ENA HIGH = driver ON

# Set direction
lgpio.gpio_write(h, DIR, 0)     # 0 = CW, 1 = CCW

print("Motor spinning... Press Ctrl+C to stop.")

try:
    while True:
        lgpio.gpio_write(h, STEP, 1)
        time.sleep(DELAY)
        lgpio.gpio_write(h, STEP, 0)
        time.sleep(DELAY)

except KeyboardInterrupt:
    pass

# Disable driver
lgpio.gpio_write(h, ENA, 0)

# Cleanup
lgpio.gpiochip_close(h)
print("Stopped.")
