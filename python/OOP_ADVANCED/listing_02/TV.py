#! /usr/bin/env python3 

class TV():
    """Implemention TV pult functionality."""

    def __init__(self):
        self.is_on = False
        self.is_muted = False
        self.channels = [2, 3, 4, 5, 10, 20, 40, 50, 60, 70, ]
        self.len_channels = len(self.channels)
        self.channel_index = 0 
        self.VOLUME_MIN = 0
        self.VOLUME_MAX = 10
        self.volume = self.VOLUME_MAX // 2 

    def power(self):
        self.is_on = not self.is_on

    def volume_up(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False
        if self.volume < self.VOLUME_MAX:
            self.volume += 1

    def volume_down(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False
        if self.volume > self.VOLUME_MIN:
            self.volume += 1

    def channel_up(self):
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

        self.is_muted = not self.is_muted
    
    def set_channel(self, new_channel):
        if new_channel in self.channels:
            self.channel_index = self.channels.index(new_channel)

    def show_info(self):
        print()
        print('TV STATUS -> ')
        if self.is_on:
            print('TV IS -> ON')
            print(f'CHANNEL IS -> {self.channels[self.channel_index]}')
            
            if self.is_muted:
                print(f'VOLUME -> {self.volume}(sound is muted)')
            else:
                print(f'VOLUME -> {self.volume}')
        else:
            print('TV -> is off')


def main():
    tv = TV()

    tv.power()
    tv.show_info()
    tv.channel_up()
    tv.channel_up()
    tv.volume_up()
    tv.volume_up()
    tv.show_info()

    tv.power()
    tv.show_info()
    tv.power()
    tv.show_info()

    tv.volume_down()
    tv.mute()
    tv.show_info()

    tv.set_channel(40)
    tv.mute()
    tv.show_info()


if __name__ == '__main__':
    main()


