import string

copy_pasta = "aurora"
output=[]

for letter in copy_pasta:
    monch = 'ERROR'
    if letter not in string.ascii_letters:
        monch = ''
    else:
        monch = f':regional_indicator_{letter.lower()}: '

    output.append(monch)

output_str = ''.join(output)

print(output_str[:2000])