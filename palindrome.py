# A string is a palindrome if it is identical forward and backward. For example
# “anna”,“civic”,“level”and“hannah”are all examples of palindromic words.Write a
# program that reads a string from the user and uses a loop to determines whether or
# not it is a palindrome.

txt = str(input("Enter any word: "))
while txt == txt[::-1]:
    print("The word " + txt + " is palindrome")
    break
else:
    print("The word " + txt + " is not palindrome")
