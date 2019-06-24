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
    delay_jitter = (delay_current - delay_last + delay_offset)
    delay_drift += delay_jitter
    delay_total += delay_jitter
    if delay_drift < -10:
        delay_drift = 0
        delay_offset += 1
    elif delay_drift  > 100:
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
