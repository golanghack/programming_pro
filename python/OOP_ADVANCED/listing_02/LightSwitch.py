#! /usr/bin/env python3 

class LightSwitch():
    """Class for lighting switcher."""

    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        self.switch_is_on = True
    
    def turn_of(self):
        self.switch_is_on = False

    def show_switcher(self):
        print(self.switch_is_on)



def main():
    light_switch = LightSwitch()

    light_switch.show_switcher()
    light_switch.turn_on()
    light_switch.show_switcher()
    light_switch.turn_of()
    light_switch.show_switcher()
    light_switch.turn_of()
    light_switch.show_switcher()

if __name__ == '__main__':
    main()
