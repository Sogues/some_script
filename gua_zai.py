#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import re


def main(args):
    if len(args) != 2:
        print('AT LEAST TWO ARGS')
        sys.exit(-1)

    pattern = r'{}'.format(args[0])
    comp = re.compile(pattern)

    if os.path.isdir(args[-1]) == False:
        try:
            os.mkdir(args[-1])
        except Exception as ex:
            print(ex)
            print('MKDIR ERROR')
            sys.exit(-1)
    try:
        process = os.popen('df -l')
        output = process.read()
        ret = comp.findall(output)
        if ret:
            print('{} has mount already'.format(args[0]))
            raise Exception
    except Exception as ex:
        print(ex)
        sys.exit(-1)
    try:
        process = os.popen('fdisk -l')
        output = process.read()
        ret = comp.findall(output)
        if not ret:
            print('{} has not exit'.format(args[0]))
            raise Exception
    except Exception as ex:
        print(ex)
        sys.exit(-1)
    try:
	os.system('mkfs.ext4 /dev/vdb')
        os.system("echo '{} {} ext4 defaults 0 0' >> /etc/fstab".format(*args))
        os.system('mount -a')
    except Exception as ex:
        print(ex)
        sys.exit(-1)
    print('SUCCESS')





if __name__ == '__main__':
    main(sys.argv[1:])
