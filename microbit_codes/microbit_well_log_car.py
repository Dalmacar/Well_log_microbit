def get_value(pos: number):
    if pos >= 0 and pos < 20:
        return 10
    elif pos >= 20 and pos < 40:
        return 120
    elif pos >= 40 and pos <= 60:
        return 30
    else:
        return 0
def send_profile():
    global value
    value = get_value(x)
    radio.send_string("[" + ("" + str(x)) + "," + ("" + str(value)) + "]")
def stop_car():
    SmartCar.motor(Motorlist.M1, Direction1.FORWARD, 0)
    SmartCar.motor(Motorlist.M2, Direction1.FORWARD, 0)
last_move_time = 0
ir = 0
x = 0
value = 0
STEP_MS = 300
irRemote.connect_infrared(DigitalPin.P16)
radio.set_group(7)
send_profile()

def on_forever():
    global ir, x, last_move_time
    ir = irRemote.return_ir_button()
    if ir == irRemote.ir_button(IrButton.OK):
        stop_car()
    elif ir == irRemote.ir_button(IrButton.UP):
        SmartCar.motor(Motorlist.M1, Direction1.FORWARD, 100)
        SmartCar.motor(Motorlist.M2, Direction1.FORWARD, 106)
        if input.running_time() - last_move_time > STEP_MS:
            x += 1
            last_move_time = input.running_time()
            send_profile()
    elif ir == irRemote.ir_button(IrButton.DOWN):
        SmartCar.motor(Motorlist.M1, Direction1.BACKWARD, 100)
        SmartCar.motor(Motorlist.M2, Direction1.BACKWARD, 106)
        if input.running_time() - last_move_time > STEP_MS:
            x += -1
            if x < 0:
                x = 0
            last_move_time = input.running_time()
            send_profile()
    elif ir == irRemote.ir_button(IrButton.LEFT):
        SmartCar.motor(Motorlist.M1, Direction1.BACKWARD, 100)
        SmartCar.motor(Motorlist.M2, Direction1.FORWARD, 106)
    elif ir == irRemote.ir_button(IrButton.RIGHT):
        SmartCar.motor(Motorlist.M1, Direction1.FORWARD, 100)
        SmartCar.motor(Motorlist.M2, Direction1.BACKWARD, 106)
    else:
        stop_car()
basic.forever(on_forever)

