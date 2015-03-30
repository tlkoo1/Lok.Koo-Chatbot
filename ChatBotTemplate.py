#open text document stop-words.txt

file = open("stop-words.txt")
stopwords = file.readlines()

#function going through all stopwords
def removeStopwords(firstWord):
    for word in stopwords:
        next = word.strip()
        firstWord = firstWord.replace(" " + next + " ", " " )
    return firstWord
    
#while input matches stop words, no display
while True:
    input = raw_input("What is your name ? ")
    input = " " + input + " " 
    filtered = removeStopwords(input);
    filtered = filtered.replace(" name "," ")
    print("Answer: " + filtered.strip())

