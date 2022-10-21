phrase = "Don't panic!"

plist = list(phrase) 
print(phrase.upper())

#challange : Don't panic -> on top

for i in range(4):
    plist.pop()
plist.pop(0)

plist.pop()

plist.remove("'")

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)