from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice('/dev/input/event0')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY and event.value == 1:
        try:
            keyevent = categorize(event)
            if 'BTN_TRIGGER_HAPPY1' in keyevent.keycode: #'BTN_TRIGGER_HAPPY', 'BTN_TRIGGER_HAPPY1'
                print ("Playstation button")
                
            if keyevent.keycode == "BTN_TOP2":
                print ("Top D-Pad button")
            if keyevent.keycode == "BTN_BASE":
                print ("Bottom D-Pad button")
            if keyevent.keycode == "(BTN_BASE2":
                print ("Left D-Pad button")
            if keyevent.keycode == "(BTN_PINKIE":
                print ("Right D-Pad button")
                
            if keyevent.keycode == "BTN_BASE5":
                print ("Left top shoulder button")
            if keyevent.keycode == "BTN_BASE6":
                print ("Right top shoulder button")
            if keyevent.keycode == "BTN_BASE3":
                print ("Left bottom shoulder button")
            if keyevent.keycode == "BTN_BASE4":
                print ("Right bottom shoulder button")

            if "BTN_TRIGGER" in keyevent.keycode: #'BTN_JOYSTICK', 'BTN_TRIGGER'
                print ("SELECT button")                
            if keyevent.keycode == "BTN_TOP":
                print ("START button")

            if keyevent.keycode == "BTN_DEAD":
                print ("SQUARE button")

                
            print (keyevent) # comment to remove key messages

        except:
            print ("Problem key pressed...")
        

