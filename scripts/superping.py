import os
up = False
nope = 0
nope_threshold = 1
# ping_command ='ping gaqverintapp01.gs.adinternal.com'
ping_command = 'ping trueye.dyndns.org'
while up is False:
    output = os.popen(ping_command).read()
    print(output)
    if 'Request timed out' not in output:
        up = True
        print(output)
    else:
        nope += 1
    