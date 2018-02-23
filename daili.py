#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import getpass

def prepare():
    os.system('git clone https://github.com/haad/proxychains')
    state = 'cd ./proxychains &&\
        ./configure &&\
        make && make install &&\
        cp ./src/proxychains.conf /etc/proxychains.conf &&\
        cd .. && rm -rf proxychains'
    os.system(state)
    print('vim /etc/proxychains.conf')
    print('socks5 	127.0.0.1 1080')

def start():
    os.system('sslocal -c shadowsocks.json -d start')

def stop():
    os.system('sslocal -c shadowsocks.json -d start')

def restart():
    os.system('sslocal -c shadowsocks.json -d start')

def main(args):
    if len(args) == 0:
        prepare()
    elif args[0] == 'start':
        start()
    elif args[0] == 'stop':
        stop()
    elif args[0] == 'restart':
        restart()
    else:
        print('args error')



if __name__ == '__main__':
    user = getpass.getuser()
    if user != 'root':
        print('current user {}, please use root'.format(user))
        sys.exit(-1)
    if len(sys.argv) > 2:
        print('args eror')
        sys.exit(-1)
    main(sys.argv[1:])
