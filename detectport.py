#!/usr/bin/env python
# coding=utf8

# version:1.0
# kali linux python 2.7.13
# author:TClion
# create:2019-03-30

import socket
import argparse

TIMEOUT = 5

parser = argparse.ArgumentParser()
parser.add_argument('-i', help='url or target ip string', type=str, default=None)
parser.add_argument('-p', help='port number', type=int, default=None)
args = parser.parse_args()


def detect_port(ip, port):
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        conn.settimeout(TIMEOUT)
        result = conn.connect_ex((ip, int(port)))
        if result == 0:
            print '%s %d open' % (ip, port)
        else:
            print '%s %d close' % (ip, port)
            conn.close()
    except:
        print '%s %d close' % (ip, port)


if __name__ == '__main__':
    args = parser.parse_args()
    try:
        detect_port(args.i, args.p)
    except:
        print('please read README.md')