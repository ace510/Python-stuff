import requests
import string
import itertools
import confidential


valid = ["-",".","_","~",":","/","?","#","[","]","@","!","$","&","'","(",")",
"*","+",",",";","%","="]
valid_string = ''.join(valid)
search_space = valid_string + string.ascii_lowercase + string.digits
output_set = set()
# save_my_sanity = 0
# all valid URL characters, namely UPPER/lower letters and the chosen symbols
# feel free to replace with a ready made constant, or update the characters


if __name__ == "__main__":
    for i in range(1,128):
        for postamble in itertools.combinations_with_replacement(search_space, i):
            # the postamble will start with a, b, c, d and work out to longer, 128
            # 128 is chosen as a sane upper bound
            #print(postamble)
            test_url = confidential.preamble + ''.join(postamble)
            trial_request = requests.get(test_url)
            # this is where the request is made, could be parallelized?
            if trial_request.status_code not in (404,400,403,504):
                # this is a list of 'bad' status codes
                # so far 404 is generic URL not found
                # 400 is something that should trigger an internal app but doesn't
                # 403 is  file denied access
                # 504 is a weird bug, maybe rate limiting?
                output_set.add(test_url)
                print(test_url)
                print(trial_request.status_code)
                # discovering new and exciting Status_codes
            # elif save_my_sanity >= 10:
            #     print(save_my_sanity)
            #     save_my_sanity = 0
            # else:
            #     save_my_sanity += 1
    # this snippit will write the set out to file, just in case I leave my computer
    # on until the heat death of the universe
    with open('results.md','w') as file:
        for item in output_set:
            file.write(item)
