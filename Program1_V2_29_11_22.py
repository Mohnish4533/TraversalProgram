"""
QUESTION:

CHANGES:
    - Class implementation
    - multiple commands at once

- User inputs starting point
- gives directions : 1. Up      2. Down     3. Right    4. Left     5. Show     6. END
- find the ending point

"""

class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move_up(self):
        self.y = self.y + 1

    def move_down(self):
        self.y = self.y - 1

    def move_left(self):
        self.x = self.x - 1

    def move_right(self):
        self.x = self.x + 1

    def show(self):
        print("\nCurrent Coordinate : ({}, {})".format(self.x, self.y))


# main program
start_x, start_y = input("Enter starting coordinate FORMAT: x,y : ").split(',')
start_x = int(start_x)
start_y = int(start_y)

draw = Direction(start_x, start_y)

stop_flag = False

while (stop_flag == False):
    # display various possible option
    print("OPTIONS: \n\t'U' - move up by 1 \n\t 'D' - move down by 1 \n\t 'R' - move right by 1 \n\t 'L' - move left by 1 \n\t 'S' - DISPLAY CURRENT POSITION \n\t 'E' - STOP COMMAND EXECUTION")

    # get sequence input
    sequence = input("Enter string of above commands (Stops at 'E'): ")

    for i in range (0, len(sequence)):
        if sequence[i] == 'U':
            draw.move_up()

        elif sequence[i] == 'D':
            draw.move_down()

        elif sequence[i] == 'L':
            draw.move_left()

        elif sequence[i] == 'R':
            draw.move_right()

        elif sequence[i] == 'S':
            draw.show()
        
        elif sequence[i] == 'E':
            stop_flag = True
            break
        
        else:
            print("\nINVALID INUT COMMAND PROVIDED. SKIPPING COMMAND")

print("\n\nEXITED COMMAND LOOP. DONE WITH PROGRAM")
