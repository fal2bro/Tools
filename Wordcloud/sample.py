import mywordcloud

filename = r"C:\Users\HMI\source\repos\fal2bro\Tools\Wordcloud\test.txt"
with open(filename, 'r', encoding='Shift-jis') as file:
        mytext = file.read()
mywordcloud.CreateWordcloud(mytext)