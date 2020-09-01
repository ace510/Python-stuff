import os, subprocess

up = False
nope = 0
nope_threshold = 0
expected = b"Connection timed out\r\n"

with open("C:\\valley_forge\\Python-stuff\\scripts\\.ssh.ignore", "r") as file:
    ping_command = file.readline(4096)


while up is False:
    command = subprocess.Popen(
        ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    (output, error) = command.communicate()
    # print(error)
    # print(error[-22:])

    if str(error[-22:]) != str(expected):
        up = True
        print("the output was different than expected \n expected")
        print(expected)
        print("got")
        print(error[-22:])
    else:
        nope += 1

    if nope > nope_threshold:
        nope = 0
        nope_threshold += 1
        print(f"failed ping attempts: {nope_threshold}")
