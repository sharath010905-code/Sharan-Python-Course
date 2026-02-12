v = int(input("Enter the number of vehicles (v): "))
w = int(input("Enter the number of wheels (w): "))
if w % 2 != 0 or w < 2 * v or w > 4 * v:
    print("INVALID INPUT")
else:
    fw = (w - (2 * v)) // 2
    tw = v - fw
    print(f"TW = {tw} FW = {fw}")