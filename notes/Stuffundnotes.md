# notes, and stuff, if you find stuff other places move it here

enter
\\sshfs.k\[name]@[home ip]!25569

as a netowrk location

22 columns
23 rows

this is my cool way of of formatting a timestamp

def time_stamp():
    the_now = time.localtime()
    stam_parts = (the_now.tm_mon, '/', the_now.tm_mday, ' ',
    the_now.tm_hour, ':', the_now.tm_min, '~')
    return ''.join(stam_parts)

list_comprehension = [i * 10 if i % 4 == 0 else i for i in range(1,num+1) ]
prints i, unless i is divisible by four

Ctrl + G: shows info in Nano

import logging

logging.basicConfig(
    level=logging.DEBUG)

DESK POWER STIP ALLOCATION
1. XBOX
2. Work Comp
3. Desk Ethernet Switch
4. USB charger hub (switch, tablet)    
