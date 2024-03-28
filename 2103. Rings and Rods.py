def countPoints(rings):
    rods = {}
    for i in range(0, len(rings), 2):
        color, rod = rings[i], rings[i + 1]
        rods.setdefault(rod, set()).add(color)

    count = 0
    for rod, colors in rods.items():
        if len(colors) == 3:
            count += 1
    return count

rings1 = "B0B6G0R6R0R6G9"
print(countPoints(rings1))

rings2 = "G4"
print(countPoints(rings2))