import time
'''say we have a 12V source and 1/4 watt resistors
power dissipated by a component is watts = current^2 * Resistance

Voltage / resistance = current

'''

voltage = 12

for m_resistance in range(144000,5000000):
    resistance = m_resistance/1000

    current = voltage / resistance

    watts = pow(current,2) * resistance
    
    if watts < 0.25:
        time.sleep(1)
        print(f'a {resistance} Ohm resistor would dissipate {watts} watts')
        print(f'at a totall current of {current}')
    
