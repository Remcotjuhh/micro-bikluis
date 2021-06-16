def on_button_pressed_a():
    global ingetypt
    ingetypt = "" + ingetypt + "A"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if wachtwoord == ingetypt:
        basic.show_icon(IconNames.YES)
        pins.servo_write_pin(AnalogPin.P0, 0)
    else:
        basic.show_icon(IconNames.NO)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global ingetypt
    ingetypt = "" + ingetypt + "B"
input.on_button_pressed(Button.B, on_button_pressed_b)

ingetypt = ""
wachtwoord = ""
pins.servo_write_pin(AnalogPin.P0, 180)
wachtwoord = "ABA"
ingetypt = ""