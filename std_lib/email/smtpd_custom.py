#! /usr/bin/env python3 

import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from -> ', peer)
        print('Message addressed -> ', mailfrom)
        print('Message addressed -> ', rcpttos)
        print('Message lenght -> ', len(data))

server = CustomSMTPServer(('localhost', 1025), None)
asyncore.loop()