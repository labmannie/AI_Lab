# Simple Grid World similar to Wumpus World

size = 4
x, y = 0, 0
direction = "RIGHT"

gold = (3, 3)
wumpus = (2, 1)
pit = (1, 3)

has_gold = False
wumpus_alive = True
arrow = True

def show():
    for j in range(size - 1, -1, -1):
        row = ""
        for i in range(size):
            if (i, j) == (x, y):
                row += " A "
            elif (i, j) == gold:
                row += " G "
            elif (i, j) == wumpus and wumpus_alive:
                row += " W "
            elif (i, j) == pit:
                row += " P "
            else:
                row += " . "
        print(row)

def percept():
    p = []

    if (x, y) == gold and not has_gold:
        p.append("Glitter")

    if abs(x - pit[0]) + abs(y - pit[1]) == 1:
        p.append("Breeze")

    if wumpus_alive and abs(x - wumpus[0]) + abs(y - wumpus[1]) == 1:
        p.append("Stench")

    if not p:
        p.append("Nothing")

    return p

def move():
    global x, y
    if direction == "RIGHT" and x < size - 1:
        x += 1
    elif direction == "LEFT" and x > 0:
        x -= 1
    elif direction == "UP" and y < size - 1:
        y += 1
    elif direction == "DOWN" and y > 0:
        y -= 1
    else:
        print("Bump!")

def left():
    global direction
    order = ["RIGHT", "UP", "LEFT", "DOWN"]
    direction = order[(order.index(direction) + 1) % 4]

def right():
    global direction
    order = ["RIGHT", "DOWN", "LEFT", "UP"]
    direction = order[(order.index(direction) + 1) % 4]

def shoot():
    global arrow, wumpus_alive
    if not arrow:
        print("No arrow left")
        return

    arrow = False
    if direction == "RIGHT" and y == wumpus[1] and x < wumpus[0]:
        wumpus_alive = False
        print("Wumpus killed!")
    elif direction == "LEFT" and y == wumpus[1] and x > wumpus[0]:
        wumpus_alive = False
        print("Wumpus killed!")
    elif direction == "UP" and x == wumpus[0] and y < wumpus[1]:
        wumpus_alive = False
        print("Wumpus killed!")
    elif direction == "DOWN" and x == wumpus[0] and y > wumpus[1]:
        wumpus_alive = False
        print("Wumpus killed!")
    else:
        print("Missed!")

print("Simple Grid World")
print("Commands: move, left, right, grab, shoot, climb, exit")

while True:
    print("\nPosition:", (x, y), "Direction:", direction)
    print("Percepts:", percept())
    show()

    if (x, y) == pit:
        print("Fell into pit. Game Over.")
        break

    if wumpus_alive and (x, y) == wumpus:
        print("Eaten by Wumpus. Game Over.")
        break

    cmd = input("Enter action: ").lower()

    if cmd == "move":
        move()
    elif cmd == "left":
        left()
    elif cmd == "right":
        right()
    elif cmd == "grab":
        if (x, y) == gold:
            has_gold = True
            print("Gold grabbed!")
        else:
            print("No gold here.")
    elif cmd == "shoot":
        shoot()
    elif cmd == "climb":
        if (x, y) == (0, 0):
            if has_gold:
                print("You escaped with gold. Win!")
            else:
                print("You escaped.")
            break
        else:
            print("Climb only at start cell.")
    elif cmd == "exit":
        break
    else:
        print("Invalid action.")
