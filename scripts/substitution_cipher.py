import string
payload = "ZKR LQYHQWHG WKH FLSKHU WKDW LV XVHG LQ WKLV PHVVDJH?"

stringy = string.ascii_uppercase

letter_to_index = {stringy[i]:i for i in range(len(stringy))}

def substitution_skew(payload,skew_vector):
    output= []
    for letter in payload:
        if letter in ('?',' '):
            output.append(letter)
        else:
            skewed = (letter_to_index[letter] + skew_vector) % 26
            output.append(stringy[skewed])
    
    return ''.join(output)


for i in range(26):
    print(substitution_skew(payload,i))