with open("2015-inputs/day1.txt", "r") as f:
    data = f.read()

floor = 1
entered_basement = -1

for i, move in enumerate(data):
    if move == ")":
        floor -= 1
    else:
        floor += 1

    if entered_basement == -1 and floor < 0:
        entered_basement = i

print("Floor:", floor)
print("Entered basement:", entered_basement)
