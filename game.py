import os

map1 = ["-------------\n-           -\n-           -\n-           -\n-           -\n-          x-\n-------------", [[25, 39, 53], [15, 29, 43, 57, 71]]]
map2 = ["2------------\n-           -\n-           -\n-           -\n-           -\n-           -\n-------------", [[25, 39, 53, 67, 81], [15, 29, 43, 57, 71]]]


class singleton:
    def __init__(self, current):
        self.current = current
    
    def setMap(self, new):
        self.current = new

    def setField(self, f):
        self.current[0] = f

    def getMap(self):
        return self.current
    
    def getField(self):
        return self.current[0]
    
    def getBlock(self):
        return self.current[1]

current_map = singleton(map1)

def movement(move, field_string, block_list):
    
    
    listRep = list(field_string)
    
    # Player field start is: 15, end: 81, reihe: 14
    print(field_string)
    # move upwards
    if move == "w":
        field_return = move_write(field_string, listRep, -14)

    # move downwards
    if move == "s":
        field_return = move_write(field_string, listRep, 14)

    # move right
    if move == "d":
        if field_string.find("x") in block_list[0]:
            field_return = move_write(field_string, listRep, 0)
        elif field_string.find("x") in [67, 81]:
            current_map.setMap(map2)
            new_string = current_map.getField()
            newRep = list(new_string)
            newRep[field_string.find("x")-10] = "x"
            field_return = move_write(new_string, newRep, 0)
            
        else:
           field_return = move_write(field_string, listRep, 1)

    # move left
    if move == "a":
        if field_string.find("x") in block_list[1]:
            field_return = move_write(field_string, listRep, 0)
        else:
            field_return = move_write(field_string, listRep, -1)

    
    current_map.setField(field_return)


def move_write(string, listi, number):
    # Clear the terminal screen based on the OS
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')

    # Rewrite the position
    if string.find("x") == -1:
        s = list(string)
        s[-1] = "-"
        string = "".join(s)
        position = string.find("x")
        listi[position] = " "
        listi[position + number] = "x"
        field = "".join(listi)
        print(string)
        return string
    else: 
        position = string.find("x")
        listi[position] = " "
        listi[position + number] = "x"
        field = "".join(listi)
        print(field)
        return field
    

x = False
while x == False:
    player = input()
    mappy = current_map.getMap()
    movement(player, mappy[0], mappy[1])

    # Print field position
    stringstring = current_map.getMap()
    #print(stringstring[0].find("x"))

    #if player == "d" and current_map[0].find("x") == 53:
        #current_map = map2.copy()
        #move_write(field_string, listRep, -10)


    

