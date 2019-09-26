import os
up = False
nope = 0
nope_threshold = 1
ping_command ='ping gaqverintapp01.gs.adinternal.com'

while up is False:
    output = os.popen(ping_command).read()
    if str(output[:22]) != 'Ping request could not':
        up = True
        print(output)
    else:
        nope += 1

    
    if nope >= nope_threshold:
        nope = 0
        nope_threshold += 1
        print(output)
    