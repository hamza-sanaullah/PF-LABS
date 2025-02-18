import random


def Encryption():

    sentence = input("Enter a sentence or word to encrypt it: ").lower().split()
    #STEP 1 REVERSRE THE WORD
    reverse_words = [word[::-1] for word in sentence]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    fixed_alphabet = 'bcdefghijklmnopqrstuvwxyza'  # Fixed letters for values
    #CREATING A DICTIONARY BY USING ZIP FUNCTION
    alphabet_dict = dict(zip(alphabet,fixed_alphabet))
    #REPLACING EACH LETTER OF THE STRING WITH A RANDOM ALPHABET
    encrypted_words = []
    for word in reverse_words:
        encrypted_word = ''
        for i in word:
            if i in alphabet_dict:
                encrypted_word += alphabet_dict[i]
        encrypted_words.append(encrypted_word)
    random_letters_dict = {}
    random_letters_dict2 = {}
    random_letters_before = ""
    #CREATING DICTIONARY FOR ADDING RANDOM ALPHABETS BEFORE AND AFTER
    for letter in alphabet:
        random_letter = "".join([random.choice(alphabet) for i in range(3)])
        random_letters_dict[letter] = random_letter
    for letter in alphabet:
        random_letter = "".join([random.choice(alphabet) for i in range(3)])
        random_letters_dict2[letter] = random_letter
    random_letters_after = ""
    encrypted_sentence = ""
    for word in encrypted_words:
        for j in word:
            if j in random_letters_dict:
                #RANDOM ALPHABETS BEFORE
                random_letters_before = random_letters_dict[j]

        for j in word:
            if j in random_letters_dict2:
                #RANDOM ALPHABETS AFTER
                random_letters_after = random_letters_dict2[j]

        encrypted_word = random_letters_before + word + random_letters_after + " "
        encrypted_sentence += encrypted_word

    encrypted_sentence = encrypted_sentence

    return encrypted_sentence


def Decryption(encrypted_sentence):
    fixed_alphabet = 'bcdefghijklmnopqrstuvwxyza'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #CREATING A DICTIONARY FOR DECRPYTION
    alphabet_dict = dict(zip(fixed_alphabet, alphabet))

    decrypted_words = []
    words = encrypted_sentence.split()
    for word in words:
        decrypted_word = ''
        #REMOVING RANDOM ALPHABETS BEFORE AND AFTER
        for letter in word[3:-3]:
            if letter in alphabet_dict:
                decrypted_word += alphabet_dict[letter]
                dec = decrypted_word[::-1]
        decrypted_words.append(dec)

    decrypted_sentence = ' '.join(decrypted_words)
    return decrypted_sentence
while True:
    want = int(input("What you want to do\nEnter 2 for encryption\nEnter 3 for decrption\nPress 0 for exit:"))

    if want==2:
        encrypted = Encryption()
        print(f"The encryted version of the given string is {encrypted}")
        # encrypted = print(Encryption())
    elif want==3:
        print(f"The decryted version of the encyrted version is {Decryption(encrypted)}")
    elif want==0:
        exit()





