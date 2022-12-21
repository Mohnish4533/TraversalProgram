"""
QUESTION:

- User inputs starting point
- gives directions : 1. Up      2. Down     3. Right    4. Left     5. Stop
- find the ending point

"""

# functions used in code

def move_up():
    global y
    y = y + 1

def move_down():
    global y
    y = y - 1

def move_left():
    global x
    x = x - 1

def move_right():
    global x
    x = x + 1


# main program 
x, y = input("Enter starting coordinate FORMAT: x,y : ").split(',')
x = int(x)
y = int(y)
option = 0
while option != 5:
    option = int(input("OPTIONS: \n 1. Up \n 2. Down \n 3. Right \n 4. Left \n 5. STOP \n : "))
    if option == 1:
        move_up()
    elif option == 2:
        move_down()
    elif option == 3:
        move_right()
    elif option == 4:
        move_left()
    elif option == 5:
        print("Final position = ({}, {})".format(x, y))
    else:
        print("INVALID INPUT\n")

print("THANK YOU")
