import os
up = False
nope = 0
nope_threshold = 1
ping_command ='curl old.reddit.com'
output = 'this program crashes my computer every time I use it, stay away'

while up is False:
    # output = os.popen(ping_command).read()[:100]
    print(output[100])