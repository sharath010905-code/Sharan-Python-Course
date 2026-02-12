d={"name":"Ram","age":22}
s = input("Enter a string: ")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key, value in freq.items():
    print(key, "-", value)