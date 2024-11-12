import mywordcloud

filename = ".\test.txt"
with open(filename, 'r', encoding='Shift-jis') as file:
        mytext = file.read()
mywordcloud.CreateWordcloud(mytext)