def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
    
while not at_goal() :
    if front_is_clear():
        move()
    elif not right_is_clear():
        if not wall_in_front():
            move()
        else:
            turn_left()
    elif right_is_clear():
        turn_right()
        move()