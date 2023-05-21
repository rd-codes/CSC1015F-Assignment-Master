# A program that search for anagrams of a given word in a file, and prints out the results in alphabetical order.
# 08 June 2021

# A function to take a word and count the frequency of each letter in the word.
def letter_count(word):
    letterFreq = {}
    for letter in word.strip():
        if letter not in letterFreq:
            letterFreq[letter] = 1
        else:
            letterFreq[letter] += 1
    return letterFreq


def main():
    print("***** Anagram Finder *****")
    # Handle an exception if one is found
    try:
        file = open("EnglishWords.txt", 'r')
        allText = file.read()
        file.close()
        # Ensure that you consider words that come after 'START' only, and read one word per line
        allText = allText.split("START")
        words = allText[1].split("\n")
        word = input("Enter a word:\n").lower()
        anagrams = []
        # Store a word in a list of anagrams if it is an anagram.
        for a_word in words:

            # Ensure that a word entered by user is not in our anagrams list; a word is not an anagram of itself.
            if letter_count(a_word) == letter_count(word) and (a_word != word):
                anagrams.append(a_word)
            else:
                pass

                # Check if the word given by the user has any anagrams in file.
        if len(anagrams) == 0:
            print("Sorry, anagrams of", "'{}'".format(word), "could not be found.")
        else:
            print(sorted(anagrams))

    except FileNotFoundError:
        print("Sorry, could not find file 'EnglishWords.txt'.")


if __name__ == "__main__":
    main()
