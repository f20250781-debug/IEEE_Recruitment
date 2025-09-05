# Palindrome
paragraph = str(input("Enter required text: ")) # Takes a user input text
# Splits the string into individual words at the whitespace after removing punctuations
words = paragraph.replace(",", "").replace("!", "").replace(".", "").replace("?", "").replace("(", "").replace(")", "").replace('"',"" ).replace("'", '').split()
palindrome = [] # Creates an empty list to add palindrome words found
for word in words:
    word = word.lower() # Converts all words to lowercase to prevent errors
    if word == word[::-1]: # Compares each word with its reverse
        palindrome.append(word) # Adds word to the list
if len(palindrome)>0:
    print("Palindrome List = ", palindrome)
else:
    print("0")