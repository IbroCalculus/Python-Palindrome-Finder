from string import punctuation
print('Enter the text whose polindrome you would like to find:')
sentence = input()
splitSentence = sentence.split(' ') # Splits the sentence by words
npal = 0                        # To count and store the number of palindromes
pal = []                        # To store the palindromes as a list


#This is to split all punctuation signs i.e !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# E.g 'wow, i am amazed,'   
for word in splitSentence:                          # Loops through the word
    nword = ''          # To store the individual words after looping through
    for string in word:                      # Loops through a word's strings
        if string in punctuation:
            pass
        else: nword += string

        
    pword = ''          # To store the individual words after looping in reverse
    for j in reversed(nword):
        if j in punctuation:
            pass
        else: pword += j
    if pword == nword: # Comparing the word and its reversed version
        if len(nword) == 1: # E.g 'I' may be seen as a polindrone
            pass
        else:
            npal += 1
            pal.append(nword)
            print(nword,'is a palindrone')
    else: print(nword, 'is not a palindrone')
print('\n'*5)
print('The number of palindrones are: {}'.format(npal))
def palDisplay():   # Function to display the list of palindrones
    for i in pal:
        print(i)
print('The palindronic words/numbers present are:')
palDisplay()
