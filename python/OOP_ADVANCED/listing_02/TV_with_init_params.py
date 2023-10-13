#! /usr/bin/env python3 

class TV():

    def __init__(self, brand: str, location: str) -> None:
        self.brand = brand
        self.location = location
        self.is_on = False
        self.is_mute = False
        self.channels = [1, 2, 3, 4, 5]
        self.len_channels = len(self.channels)
        self.channel_index = 0 
        self.VOLUME_MIN = 0 
        self.VOLUME_MAX = 10 
        self.volume = self.VOLUME_MAX // 2 

    def power(self) -> None:
        self.is_on = not self.is_on 

    def volume_up(self) -> None:
        if not self.is_on:
            return
        if self.is_mute:
            self.is_mute = False
        if self.volume < self.VOLUME_MAX:
            self.volume += 1

    def volume_down(self) -> None:
        if not self.is_on:
            return 
        if self.is_mute:
            self.is_mute = False
        if self.volume > self.VOLUME_MIN:
            self.volume -= 1

    def channel_up(self) -> None:
        if not self.is_on:
            return
        self.channel_index += 1
        if self.channel_index == self.len_channels:
            self.channel_index = 0 

    def channel_down(self):
        if not self.is_on:
            return 
        self.channel_index -= 1
        if self.channel_index < 0:
            self.channel_index = self.len_channels - 1

    def mute(self):
        if not self.is_on:
            return 
        self.is_mute = not self.is_mute
    
    def set_channel(self, new_channel: int) -> None:
        if new_channel not in self.channels:
            return
        self.channel_index = self.channels.index(new_channel)

    def show_info(self):
        print()
        print(f'Status of TV -> {self.brand}')
        print(f'Location -> {self.location}')
        if self.is_on:
            print('TV is on')
            print(f'Channel is -> {self.channels[self.channel_index]}')
            if self.is_mute:
                print(f'Volume is -> {self.volume}(sound is muted)')
            else:
                print(f'Volume is -> {self.volume}')
        else:
            print('TV is -> Off')


def main():
    tv_one = TV('Sony', 'Living room')
    tv_two = TV('Samsung', 'Bedroom')
    
    tv_one.power()
    tv_one.volume_up()
    tv_one.volume_up()

    tv_two.power()
    tv_two.volume_up()
    tv_two.set_channel(3)
    tv_two.mute()

    tv_one.show_info()
    tv_two.show_info()


if __name__ == '__main__':
    main()