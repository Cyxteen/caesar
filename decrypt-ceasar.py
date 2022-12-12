alphabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
alphabet1 = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
letter_to_digit = []

def word_to_digit(encrypted_word, b):
    new_reduced_digit = []
    space_in_word = []
    word = ''
    key = 0
    x = 0
    a = 1
    while a < b + 1:
        length_of_variable = len(encrypted_word)
        while x <= length_of_variable - 1:
            single_letter = encrypted_word[x]
            if single_letter == " ":
                space_in_word.append(x)
                pass
            else:
                single_digit_in_letters = alphabet[single_letter]
                letter_to_digit.append(single_digit_in_letters)
            x += 1
        
        # print(space_in_word)
        length_of_digits = len(letter_to_digit)
        w = 0

        while w <= length_of_digits - 1:
            single_digit = letter_to_digit[w] - a
            new_reduced_digit.append(single_digit)
            w += 1

        new_word(new_reduced_digit, a, space_in_word)
        new_reduced_digit = []
        a += 1

def new_word(new_reduced_digit, a, space_in_word):
    new_reduced_word = ''
    index_of_spaces = []
    w = 1
    y = 0
    if len(space_in_word) > 0:
        index_of_spaces.append(space_in_word[0])
    if len(space_in_word) > 1:
        # print(len(space_in_word))
        while w <= len(space_in_word) - 1:
            number_to_add = space_in_word[w]
            index_of_spaces.append(number_to_add - w)
            w += 1
    # print(index_of_spaces)
    length_reduced_digits = len(new_reduced_digit)
    while y <= length_reduced_digits - 1:
        if y in index_of_spaces:
            new_reduced_word += " "
            digit_word = new_reduced_digit[y]
            if digit_word < 0:
                digit_word = 26 + digit_word
            new_reduced_word += alphabet1[digit_word]
        else:
            digit_word = new_reduced_digit[y]
            if digit_word < 0:
                digit_word = 26 + digit_word
                if digit_word < 0:
                    digit_word = 26 + digit_word
                    

            new_reduced_word += alphabet1[digit_word]
        y += 1
    print(f"The cracked word with key: {a} is: {new_reduced_word.upper()}\n")
    new_reduced_word = ""

def main():
    try:
        print("-----------------------------------------------------------")
        print('CAESAR DECRYPTOR. ENTER ANY STRING OF CHARACTERS TO DECRYPT')
        print("-----------------------------------------------proudly Tz🖤")
        word_encrypted = input("Enter cipher text to decrypt: ")
        iterable = int(input("Enter number of times to iterate(max = 32): "))
        if word_encrypted == "":
            print("word to decrypt cannot be empty!")
            main()
        elif iterable == "":
            print("number to iterate cannot be empty cannot be empty!")
            main()
        elif iterable > 32:
            print("iterable cannot be greater than 32")
            main()
        else:
            # b - number of steps to iterate if step is 1
            word_to_digit(word_encrypted.lower(), iterable)
    except KeyboardInterrupt:
        print("\n\nbye 👋👋")

main()