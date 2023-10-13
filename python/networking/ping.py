#! /usr/bin/env python3

"""Use ping command with python"""

import subprocess

def ping_ip(ip_address: str) -> bool:
    """Ping for ip -> i_address;
    if ip supported -> True
    else -> False
    """ 

    replica = subprocess.run(['ping', '-c', '3', 'n', ip_address],
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            encoding='utf-8')
    if replica.returncode != 0:
        return True
    else:
        return False

print(ping_ip(''))