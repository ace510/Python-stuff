import string

valid = ["-",".","_","~",":","/","?","#","[","]","@","!","$","&","'","(",")",
"*","+",",",";","%","="]
valid_string = ''.join(valid)
search_space = valid_string + string.ascii_lowercase + string.digits




if __name__ == "__main__":

    print('this code is bad and should not be ran directly')

# 0123456789-._~:/?#[]@!$&'()*+,;%=