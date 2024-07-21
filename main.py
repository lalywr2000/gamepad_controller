from gamepad_controller import ShanWanGamepad

if __name__ == '__main__':
    shanwan_gamepad = ShanWanGamepad()

    while True:
        gamepad_input = shanwan_gamepad.read_data()

        LH = gamepad_input.analog_stick_left.x          # Left joystick Horizontal direction
        LV = gamepad_input.analog_stick_left.y          # Left joystick Vertical direction
        RH = gamepad_input.analog_stick_right.y * -1.0  # Right joystick Horizontal direction

        # Remove noise value
        LH = 0.0 if -0.1 < LH < 0.1 else LH
        LV = 0.0 if -0.1 < LV < 0.1 else LV
        RH = 0.0 if -0.1 < RH < 0.1 else RH

        # Left joystick: parallel movement to 8 directions
        # Right joystick: rotation in place
        # [left joystick has priority to control]

        if LH == 0 and LV > 0:
            print("direction 1")
        elif LH > 0 and LV > 0:
            print("direction 2")
        elif LH > 0 and LV == 0:
            print("direction 3")
        elif LH > 0 and LV < 0:
            print("direction 4")
        elif LH == 0 and LV < 0:
            print("direction 5")
        elif LH < 0 and LV < 0:
            print("direction 6")
        elif LH < 0 and LV == 0:
            print("direction 7")
        elif LH < 0 and LV > 0:
            print("direction 8")
        else:
            if RH > 0:
                print("clockwise rotation")
            elif RH < 0:
                print("counter-clockwise rotation")
