import sys
import shelve
import pyperclip


'''make clipboard that can store many things

    mcb.pyw save [item]: saves clipboard to item
    
    mcb.pyw [item] retrieves clipboard
    
    mcb list: lists all stored items
    
    eat pant
    
    
    '''
shelf = shelve.open('shelf')

if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list((shelf.keys()))))
elif sys.argv[1].lower() == 'save':
    shelf[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1] in shelf:
    pyperclip.copy(shelf[sys.argv[1]])

shelf.close()