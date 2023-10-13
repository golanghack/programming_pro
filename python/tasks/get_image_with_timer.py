#! /usr/bin/env python3 

import time 

def get_image_url():

    pass

def result(func):
    url = func()
    if url == None:
        while True:
            result(func)
            time.sleep(10)
    return url 


def main():
    result(get_image_url)


if __name__ == '__main__':
    main()
