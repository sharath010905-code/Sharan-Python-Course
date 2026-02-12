d = {"a": 1, "b": 2, "c": 3}
swapped = {}

for key, value in d.items():
    swapped[value] = key

print(swapped)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {}

for key, value in d1.items():
    merged[key] = value

for key, value in d2.items():
    merged[key] = value

print(merged)