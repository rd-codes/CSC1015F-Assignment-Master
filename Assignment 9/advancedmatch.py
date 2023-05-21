# A program to implement a two characters wildcard
# 03 June 2021


def match(pattern, word, ):
    # Base case
    if len(pattern) == 0 and len(word) == 0:
        return True
    if len(pattern) > 1 and pattern[0] == '*' and len(word) == 0:
        return False
    # Check if the pattern contains "*" and first character in pattern doesn't match with the first character in word/first charater in pattern is not "?"
    if (len(pattern) <= 1 or pattern[0] != '?') and (len(pattern) == 0 or len(word) == 0 or pattern[0] != word[0]):
        # Check when the first character in pattern is "*"
        if len(pattern) != 0 and pattern[0] == '*':
            return match(pattern[1:], word) or match(pattern, word[1:])
        return False
    # Check if the pattern  contains '?', or first character in pattern match with the first character in word/first charater in pattern is "?"
    return match(pattern[1:], word[1:])