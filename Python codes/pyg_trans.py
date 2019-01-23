print("Welcome to The PYG Translator")
pyg = 'ay'


def pyg_translator():
    original = input('Enter a word: ')
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word + first + pyg
        new_word = new_word[1:len(new_word)]
        print("Your translated word is: " + new_word)
    else:
        print('Not a Valid Word!!')
        print('''Press 1 to Retry
Press 0 to exit''')
        temp_var = int(input("Enter your choice: "))
        if temp_var == 1:
            print("Restarting program....")
            pyg_translator()
        else:
            print("Exiting program....")
            exit()


pyg_translator()
