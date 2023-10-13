#! /usr/bin/env python3 

import smtplib

serv = smtplib.SMTP('mail')
serv.set_debuglevel(True)

try:
    result = serv.verify('golanghack')
    not_result = serv.verify('nowhere')
finally:
    serv.quit()

print('golang -> ', result)
print('not -> ', not_result)