#!/usr/bin/env python
# coding=utf8

# version:1.0
# kali linux python 2.7.13
# author:TClion
# create:2019-03-30

import socket
import argparse

TIMEOUT = 5

def detect_port(ip, port):
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        conn.settimeout(TIMEOUT)
        result = conn.connect_ex((ip, int(port)))
        if result == 0:
            print '%s port %d opened' % (ip, port)
        else:
            print '%s port %d closed' % (ip, port)
            conn.close()
    except:
        print '%s port %d closed' % (ip, port)

if __name__ == '__main__':
    detect_port('www.baidu.com', 53)