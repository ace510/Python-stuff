# notes, and stuff, if you find stuff other places move it here

enter
\\sshfs.k\[name]@[homeip]!25569

as a netowrk location

22 columns
23 rows

this is my cool way of of formatting a timestamp

def time_stamp():
    the_now = time.localtime()
    stam_parts = (the_now.tm_mon, '/', the_now.tm_mday, ' ', 
    the_now.tm_hour, ':', the_now.tm_min, '~')

    return ''.join(stam_parts)