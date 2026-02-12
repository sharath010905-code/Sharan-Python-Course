rainfall=float(input("Enter rainfall amount in mm:"))
if rainfall < 1:
    print("No Rain")
elif rainfall < 5:
    print("Light Rain")
elif rainfall < 10:
    print("Moderate Rain")
else:
    print("Heavy Rain")