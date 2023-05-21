# A program to check whether or not a string is a palindrome using recursive function
# 02 June 2021

def isPalindrome(string):
    # Base case
    if  len(string) <= 1 :
        return True
    # Check if a pattern match with a word by comparing each current characters
    if string[0] == string[len(string)-1]:
        return isPalindrome(string[1:len(string) - 1])
    else:
        return False
   
    
def main():
    words = input("Enter a string:\n")
    if isPalindrome(words):
        print("Palindrome!")
    else:
        print("Not a palindrome!")
    

if __name__ == "__main__":
    main()
    