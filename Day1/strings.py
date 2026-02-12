#s=input("Enter a string:")
#if s[0].isupper():
#    print("Uppercase")
#else:
#    print("Lowercase")

#s=input("Enter a string:")
#word_len=len(s.split())
#char_len=len(s)
#print("the count of words is:",word_len)
#print("The count of characters is:",char_len)

#text = input("Enter a sentence: ")
#print(text.capitalize())     #Capitalizes the first letter of the sentence
#print(text.title())          #Capitalizes the first letter of each word in the sentence

#text=input("Enter a string:")
#print("Reversed string:", text[::-1])    #Reverses the string

    #count the number of vowels in a string
#text=input("Enter a string:")
#count=(text.count('a')+text.count('e')+text.count('i')+text.count('o')+text.count('u')+text.count('A')+text.count('E')+text.count('I')+text.count('O')+text.count('U'))
#print("The count of the vowels in the string is:",count)       

#text = input("Enter a string: ")
#for i in "aeiouAEIOU":
#    text = text.replace(i, "")
#print("String after removing vowels:", text)  #removing vowels from the string


    #check if the string is palindrome or not
text = input("Enter a string: ").lower()  #Converting the string to lowercase
rev = ""
for ch in text:
    rev = ch + rev
if text == rev:
    print("Palindrome")
else:
    print("Not a palindrome")