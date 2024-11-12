import mywordcloud

filename = r"Wordcloud\test.txt"
with open(filename, 'r', encoding='Shift-jis') as file:
        mytext = file.read()
mywordcloud.CreateWordcloud(mytext)