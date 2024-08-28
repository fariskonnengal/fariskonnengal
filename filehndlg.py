sent=input("enter the sentence")
#write to a file named sentence.txt
f=open("sentence.txt","w")
f.write(sent)
f.close()

#read content of sentence.txt
f=open("sentence.txt","r")
content=f.read()
f.close()
print(content)

#count number of words in content
words=content.split()
print(len(words))


