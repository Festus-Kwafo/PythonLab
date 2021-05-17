#A string is a palindrome if it is identical forward and backward. For example
#“anna”,“civic”,“level”and“hannah”are all examples of palindromic words.Write a
#program that reads a string from the user and uses a loop to determines whether or
#not it is a palindrome.

text = str(input("Enter any word: "))
while text == text[::-1]:
    print("The word "+ text + " is palindrome")
    break
else: 
    print("The word "+ text + " is not palindrome")
