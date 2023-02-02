def on_button_pressed_a():
    global counter
    counter = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global counter, goal
    counter = 0
    goal = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global goal
    goal += 10
    basic.show_number(goal)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global counter
    counter += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

goal = 0
counter = 0
counter = 0
goal = 0

def on_forever():
    global counter
    basic.show_number(counter)
    if goal > 0:
        if counter == goal:
            basic.show_icon(IconNames.HEART)
            music.play_melody("C D E F G A B C5 ", 200)
            counter = 0
basic.forever(on_forever)
