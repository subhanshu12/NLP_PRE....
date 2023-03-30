text_file = open ("MyData.txt" , 'r')
text = text_file.read()

## cleaning the unwanted notation, punctuation marks 
text = text.lower()

words = text.split()

words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]
## finding unique

unique = [] ## unique words ko isme store krenge 

for word in words:
    if word not in unique:
        unique.append( word)

## sort krenge hum

unique.sort()
sentence = " “Someone on TV has only to say, ‘Alexa,’ and she lights up. She’s always ready for action, the perfect woman, never says, ‘Not tonight, dear.’” "
print(sentence.split(','))
print(unique)

# open() function to get a reference to the file object.
# file.read() method to read contents of the file.
# str.lower() method to convert text to lower case.
# str.split() method to split the text into words separated by white space characters like single space, new line, tab, etc.
# str.strip() method to strip the punctuation marks from the edges of words.
# str.replace() method to replace 's with nothing, at the end of words.
# for loop to iterate for each word in the words list.
# in – membership operator to check if the word is present in unique.
# list.append() method to append the word to unique list.
# list.sort() method to sort unique words in lexicographic ascending order.