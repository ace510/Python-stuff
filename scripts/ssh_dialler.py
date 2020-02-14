import os
up = False
nope = 0
nope_threshold = 1
ping_command ='ssh 50.43.42.179 -p '

for i in range(23,65535):
    ssh_command = ping_command + str(i)
    print(ssh_command)
    output = os.popen(ssh_command).read()
    if str(output[:22]) != 'Ping request could not':
        up = True
        print(output)
    else:
        nope += 1

    
    if nope >= nope_threshold:
        nope = 0
        nope_threshold += 1
        print(output)
    