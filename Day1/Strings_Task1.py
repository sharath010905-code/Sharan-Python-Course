s = input("Enter a string: ")

print("Word count:", len(s.split()))
print("Character count:", len(s))

print("Capitalized:", s.title())
print("Reversed:", s[::-1])
print("Without duplicates:", "".join(dict.fromkeys(s)))

vowels = "aeiouAEIOU"
vowel_count = 0
no_vowels = ""

for ch in s:
    if ch in vowels:
        vowel_count += 1
    else:
        no_vowels += ch

print("Vowel count:", vowel_count)
print("Without vowels:", no_vowels)

t = s.replace(" ", "").lower()
print("Palindrome" if t == t[::-1] else "Not Palindrome")

for ch in s:
    print(ch, ":", s.count(ch))

print("Sorted string:", "".join(sorted(s)))