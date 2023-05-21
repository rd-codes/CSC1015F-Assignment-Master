# A program that search for words of a specified length in a file, that are anagrams of each other.
# 10 June 2021

from anagramsearch import letter_count as l_c


def main():
    print("***** Anagram Finder *****")
    word_len = eval(input("Enter word length:\n"))
    print("Searching...")

    # Search for words in file
    file = open("EnglishWords.txt", 'r')
    allText = file.read()
    file.close()
    # Ensure that you consider words that come after 'START' only and read one word per line, after the word 'START'.
    allText = allText.split("START")
    words = allText[1].split("\n")
    words_list = []
    # Store a word in a list if it has the length specified by the user
    for a_word in words:
        if len(a_word) == word_len:
            words_list.append(a_word)
        else:
            pass
    file_name = input("Enter file name:\n")
    file_name = open(file_name, 'w')
    print("Writing results...")

    anagrams = []
    c_anagrams = []
    anagram_sets = []
    list_copy = words_list
    # Write words that are anagrams of each other in a set 
    for a_word in words_list:
        for a_copy in list_copy:
            if l_c(a_word) == l_c(a_copy) and a_copy not in c_anagrams:
                anagrams.append(a_copy)
                c_anagrams.append(a_copy)  # To check if words have been compared or not
            else:
                pass
        # Ensure that a set contains at least two words
        if len(anagrams) >= 2:
            anagram_sets.append(sorted(anagrams))
        else:
            pass
        # Overwrite the first list and check for a new one
        anagrams = []
    # Write the sets of anagrams in a file
    for a_set in sorted(anagram_sets):
        print(str(a_set), file=file_name)
    file_name.close()


if __name__ == "__main__":
    main()

