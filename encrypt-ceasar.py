alphabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
alphabet1 = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

def stepOne(input, key):
    # 1. change word to digits
    # variables
    letter_to_digit = []
    space_in_word = []
    x = 0

    length_of_variable = len(input)
    while x <= length_of_variable-1:
        single_letter = input[x]
        if single_letter == " ":
            space_in_word.append(x)
            pass
        else:
            single_digit_in_letters = alphabet[single_letter]
            letter_to_digit.append(single_digit_in_letters)
        x += 1
    # print(f"number of spaces: {space_in_word}")
    # print(f"values of plain text: {letter_to_digit}")
    stepTwo(letter_to_digit, key, space_in_word)

def stepTwo(letter_to_digit, key, space_in_word):
    # 2. append key to the values of plain text
    # variables
    ciphered_digit = []
    y = 0
    length_of_digit = len(letter_to_digit)
    
    while y <= length_of_digit - 1:
        sigle_digit_in_digits = letter_to_digit[y]
        sigle_digit_in_digits += key
        if sigle_digit_in_digits > 25:
            sigle_digit_in_digits -= 26
        ciphered_digit.append(sigle_digit_in_digits)
        y += 1
    # print(f"values of ciphered text: {ciphered_digit}")
    stepThree(ciphered_digit, space_in_word)

def stepThree(ciphered_digit, space_in_word):
    # 3. change values of ciphered text to letters and concatenate
    # variables
    index_of_spaces = []
    word = ''
    w = 1
    z = 0

    # increment the values of space_in_word
    if len(space_in_word) > 0:
        index_of_spaces.append(space_in_word[0])
    if len(space_in_word) > 1:
        # print(len(space_in_word))
        while w <= len(space_in_word) - 1:
            number_to_add = space_in_word[w]
            index_of_spaces.append(number_to_add - w)
            w += 1
    # print(f"number of spaces: {index_of_spaces}")
    ciphered_digit_length = len(ciphered_digit)
    while z <= ciphered_digit_length - 1:
        if z in index_of_spaces:
            word += " "
            ciphered_digit_word = ciphered_digit[z]
            word += alphabet1[ciphered_digit_word]
            ciphered_digit_length + 1
        else:
            ciphered_digit_word = ciphered_digit[z]
            word += alphabet1[ciphered_digit_word]
        z += 1

    print("Caesar ciphered Text: "+word.upper())

def main():
    try:
        print("-----------------------------------------------------------")
        print('CAESAR ENCRYPTOR. ENTER ANY STRING OF CHARACTERS TO ENCRYPT')
        print("-----------------------------------------------proudly Tz🖤")
        word_to_encrypt = input("Enter word to encrypt: ")
        key = input("Enter number of steps: ")
        if word_to_encrypt == "":
            print("word to encrypt cannot be empty!")
        elif key == "":
            print("steps cannot be empty!")
        else:
            stepOne(word_to_encrypt.lower(),int(key))
    except KeyboardInterrupt:
        print("\n\nbye 👋👋")

main()