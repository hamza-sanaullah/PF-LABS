#Write a program that takes a sentence from the user and calculate the number of vowels and consonants in the sentence
#TAKING INPUT
sentence = input("Enter your sentence:\n")
#CONVERTING UPPER CASE INTO LOWER CASE
sentence = sentence.lower()
vowel_count = 0
conson_count = 0
if " " in sentence:
    #replacing space with empty
    sentence = sentence.replace(" ","")
for char in sentence:
    if char in "aeiou":
        #checking vowel letters
        vowel_count+=1
    else:
         conson_count+=1
print(f"There are {vowel_count} vowel in the given sentence")
print(f"There are {conson_count} consonants in the given sentence")