# A program to check if a wildcard pattern given matches a given word
# 03 June 2021

def match(pattern, word):
    # Base case
    if len(pattern) == 0 and len(word) == 0:
        return True
    if len(pattern) != len(word):
        return False
    # Check when the lengths are equal and there might be wild card "?"
    if len(pattern) == len(word) and (pattern[0] == "?" or pattern[0] == word[0]):
        return match(pattern[1:], word[1:])
    else:
        return False
