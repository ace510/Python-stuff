import os
import time

nope = 0
nope_threshold = 1
bad_strings = ("Request timed out", " Temporary failure", "could not find host")
# ping_command ='ping gaqverintapp01.gs.adinternal.com'
# ping_command = "ping www.google.com"
ping_command = 'ping owner-pc'
while True:
    up = True
    print("pinging")
    output = os.popen(ping_command).read()
    print(output)
    for b_str in bad_strings:
        if b_str in output:
            print(f"found: {b_str}")
            up = False
            time.sleep(1)

    if up == True:
        print("site seems to be up")
        print(output)
        break

# up = False
# nope = 0
# nope_threshold = 1
# # ping_command ='ping gaqverintapp01.gs.adinternal.com'
# ping_command = "ping trueye.dyndns.org"
# while up is False:
#     output = os.popen(ping_command).read()
#     print(output)
#     if "Request timed out" not in output:
#         up = True
#         print(output)
#     else:
#         nope += 1
