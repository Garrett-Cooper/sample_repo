name = "garrett cooper"
#caps first letter word
print (name.title())
#converts all letters to lower case
print (name.lower())
#converts all letters to upper case
print (name.upper())

#adding a newline in a string \n
message = "Languages:\nPython\nC\nJavaScript"
print (message)
#combining a tab \t and newline \n
message = "Languages:\n\tPython\n\tC\n\tJavaScript"
print (message)

#using right strip rstrip() , left strip lstrip(), and strip strip() methods
word = 'hello '
rstrip_word = word.rstrip()
print (word)
print (word + 'has ' + str(len(word)) + ' characters')
print (rstrip_word)
print (word + 'has ' + str(len(rstrip_word)) + ' characters')

word = ' hello '
all_strip_word = word.strip()
print (word)
print (word + 'has ' + str(len(word)) + ' characters')
print (all_strip_word)
print (word + 'has ' + str(len(all_strip_word)) + ' characters')
