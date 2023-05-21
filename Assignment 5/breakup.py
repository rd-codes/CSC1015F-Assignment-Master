# A program that convert an input sentence into a comma-separated list of lowercase words with a full-stop at the end.
# 16 April 2021

sentence = input("Enter a sentence:\n")
print("The word list:",end=" ")

for posLetter in range(len(sentence)):
# Check for one complete word in a sentence
    if not(sentence[posLetter]==" "):           
        print(sentence[posLetter].lower(),end="")
    else:                                        
        print(", ",end="")          
print(".")
