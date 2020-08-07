import os
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

nope = 0
nope_threshold = 1
bad_strings = ('Request timed out',' Temporary failure','could not find host')
# ping_command ='ping gaqverintapp01.gs.adinternal.com'
ping_command = 'ping www.google.com'
while True:
    up = True
    print('pinging')
    output = os.popen(ping_command).read()
    print(output)
    for b_str in bad_strings:
        if b_str in output:
            print(f'found: {b_str}')
            up = False

    if up == True:
        print('site seems to be up')
        print(output)
        break
=======
=======
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
=======
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
=======
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
=======
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
    