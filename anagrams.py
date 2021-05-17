#Two words are anagrams if they contain all of the same letters, but in a
#differentorder. For example, “evil” and “live” are anagrams because each contains
#one ‘e’, one ‘i’, one ‘l’, and one ‘v’. Create a program that reads two strings from
#the user, determines whether or not they are anagrams.

fWord = str(input("Enter first word: "))
sWord = str(input("Enter second word: "))
f = sorted(fWord)
s = sorted(sWord)
if f == s:
    print("The words are anagrams")
else:
    print("The words are not anagrams")
