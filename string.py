sent = str(input("enter the sentence"))

#convert to uppercase
uppercs=sent.upper()
print(uppercs)

#convert to lowercase
lowercs=sent.lower()
print(lowercs)

#count and print number of words in the sentence
words = sent.split()
print(len(words))

#replace a word from the sentence
word_to_replace = input("enter the word to replace")
replacement_word = input("enter replacement word")
newword=sent.replace(word_to_replace,replacement_word)
print(newword)


#split sentence by comma
words=sent.split(",")
print(words)



