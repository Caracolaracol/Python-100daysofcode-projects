
row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]

map =  [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical-1][horizontal - 1] = "X"


""" if horizontal == 1 :
    if vertical == 1 :
        map[0][0] = "x"
    elif vertical == 2 :
        map[1][0] = "x"
    elif vertical == 3 :
        map[2][0] = "x"
elif horizontal == 2 :
    if vertical == 1 :
        map[0][1] = "x"
    elif vertical == 2 :
        map[1][2] = "x"
    elif vertical == 3 :
        map[2][3] = "x"
elif horizontal == 3 :
    if vertical == 1 :
        map[0][3] = "x"
    elif vertical == 2 :
        map[1][3] = "x"
    elif vertical == 3 :
        map[2][3] = "x" """

print(f"{row1}\n{row2}\n{row3}")