#! /usr/bin/env python3 

class DimmerSwitch():
    
    def __init__(self):
        self.switch_is_on = False
        self.brightness = 0 

    def turn_on(self) -> bool:
        self.switch_is_on = True

    def turn_off(self) -> bool:
        self.switch_is_on = False

    def raise_level(self):
        if self.brightness < 10:
            self.brightness += 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness -= 1
        
    def show(self):
        print(f'Switch on -> {self.switch_is_on}')
        print(f'Brightness -> {self.brightness}')


def main():
    dimmer = DimmerSwitch()
    dimmer.turn_on()
    dimmer.raise_level()
    dimmer.raise_level()
    dimmer.raise_level()
    dimmer.raise_level()
    dimmer.show()

    dimmer.lower_level()
    dimmer.lower_level()
    dimmer.turn_off()
    dimmer.show()

    dimmer.turn_on()
    dimmer.raise_level()
    dimmer.raise_level()
    dimmer.raise_level()
    dimmer.show()


if __name__ == '__main__':
    main()

    