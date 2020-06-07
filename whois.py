#!/usr/bin/env python2
import socket
import sys

if len(sys.argv) <= 1:
    print('USE: {} target.com'.format(sys.argv[0]))
else:
    target_domain = sys.argv[1]
    whois_iana = 'whois.iana.org'


    def new_socket(whois):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((whois, 43))
        s.send(target_domain + '\r\n')
        response = s.recv(1024)
        s.close()

        return response


    whois_target = new_socket(whois_iana).split()[19]

    whois_response = new_socket(whois_target)

    print(whois_response)
