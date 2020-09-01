import machine, time

adc = machine.ADC(1)
pin = machine.Pin(2, machine.Pin.OUT)


def toggle(p):
    p.value(not p.value())


delay_last = adc.read()
delay_total = 0
delay_drift = 0
delay_offset = 0
while True:
    delay_current = adc.read()
    toggle(pin)
    delay_jitter = delay_current - delay_last + delay_offset
    delay_drift += delay_jitter
    delay_total += delay_jitter
    if delay_drift < -10:
        delay_drift = 0
        delay_offset += 1
    elif delay_drift > 100:
        delay_drift = 0
        delay_offset -= 1

    print(delay_total)
    time.sleep_ms(abs(delay_total))
    delay_current = delay_last

import network, time, esp

esp.osdebug(None)
# os debug none gets rid of the pesky wifi messages
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
pin = machine.Pin(2, machine.Pin.OUT)
wlan.active(True)
ap.active(False)


def toggle(p):
    p.value(not p.value())


tset = set()
tset_names = set()

while True:
    # wlan.active(True)
    pin.on()
    tupelo = wlan.scan()
    pin.off()

    for entity in tupelo:
        tset.add(entity)

        if entity[0] not in tset_names:
            tset_names.add(entity[0])

    if len(tset_names) > 3:
        print(tset_names)
    # wlan.active(False)
    # time.sleep_ms(60000)

from machine import Pin
from neopixel import NeoPixel
import time


@micropython.native
def lights():

    pin = Pin(4, Pin.OUT)
    np = NeoPixel(pin, 50)
    while True:
        for i in range(50):
            np[i] = (0, 0, 0)
            np.write()
            print(i)


from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 50)


def light_gen():

    r, g, b = (0, 0), (255, -1), (0, 1)

    while True:
        r += r_change
        g += g_change
        b += g_change

        for item in [r, g, b]:
            if item[0] == 0 or item[0] == 255:
                if item[1] == -1:
                    item = (item[0], 0)
                elif item[1] == 0:
                    item = (item[0], 1)
                elif item[1] == 1:
                    item = (item[0], -1)
                else:
                    raise HolUpException

        yield (r[0], g[0], b[0])


def lights2():

    while True:
        for i in range(50):
            np[i] = (0, 255, 0)
            np.write()
            time.sleep_ms(100)


def blinky():
    from machine import Pin
    import time

    led_pin = Pin(5, Pin.OUT, value=1)

    while True:
        time.sleep_ms(1000)
        led_pin.value(0)
        time.sleep_ms(1500)
        led_pin.value(1)


def dht():
    import dht
    import machine
    import time

    dht_pin = dht.DHT11(machine.Pin(4))

    while True:
        time.sleep(2)
        try:
            dht_pin.measure()
        except:
            pass
        print("temperature is " + str(dht_pin.temperature()))
        print("humidity is " + str(dht_pin.humidity()))
