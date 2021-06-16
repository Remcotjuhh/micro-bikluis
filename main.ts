input.onButtonPressed(Button.A, function () {
    ingetypt = "" + ingetypt + "A"
})
input.onButtonPressed(Button.AB, function () {
    if (wachtwoord == ingetypt) {
        basic.showIcon(IconNames.Yes)
        pins.servoWritePin(AnalogPin.P0, 0)
        pins.servoWritePin(AnalogPin.P1, 0)
    } else {
        basic.showIcon(IconNames.No)
    }
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    ingetypt = "" + ingetypt + "B"
})
let ingetypt = ""
let wachtwoord = ""
pins.servoWritePin(AnalogPin.P0, 180)
pins.servoWritePin(AnalogPin.P1, 180)
wachtwoord = "ABA"
ingetypt = ""
