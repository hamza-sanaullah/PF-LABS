"""from collections import Counter
para = input("Enter a paragraph").split()
punctuations = [",",";","''",":"]
p_words = []
for word in para:
    clean_word = ''
    for c in word:
        if c not in punctuations:
            clean_word += c
    p_words.append(clean_word)
print(p_words)

word_counts = Counter(p_words)
print(word_counts)
t_words = 0
for words in p_words:
    t_words+=1
print(f"The total  number of words in the para graph is {t_words} ")"""



#ANOTHER METHOD
para = input("Enter a paragraph").split()
punctuations = [",",";","''",":"]
p_words = []
for word in para:
    clean_word = ''
    for c in word:
        if c not in punctuations:
            clean_word += c
    p_words.append(clean_word)

print(p_words)
d = {}
for word in p_words:
    if word in d:
        d[word]+=1
    else:
        d[word] = 1
print(d)
print(f"The total  number of words in the para graph is {len(p_words)} ")












