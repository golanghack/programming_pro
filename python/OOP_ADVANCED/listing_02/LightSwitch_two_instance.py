#! /usr/bin/env python3 

from LightSwitch import LightSwitch

light_switch_one = LightSwitch()
light_switch_two = LightSwitch()

def main():
    light_switch_one.show_switcher()
    light_switch_two.show_switcher()
    light_switch_one.turn_on()
    light_switch_two.turn_of()
    light_switch_one.show_switcher()
    light_switch_two.show_switcher()


if __name__ == '__main__':
    main()