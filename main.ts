input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    counter = 0
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    counter = 0
    goal = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    goal += 10
    basic.showNumber(goal)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    counter += 1
})
let goal = 0
let counter = 0
counter = 0
goal = 0
basic.forever(function on_forever() {
    
    basic.showNumber(counter)
    if (goal > 0) {
        if (counter == goal) {
            basic.showIcon(IconNames.Heart)
            music.playMelody("C D E F G A B C5 ", 200)
            counter = 0
        }
        
    }
    
})
