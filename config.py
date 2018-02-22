#!/usr/bin/env python
# encoding: utf-8


import os
import sys
import re

def main():
    echo_state =
    statement = [
            'apt-get install python3',
            'apt-get install python3-pip',
            'pip3 install virtualenv',
            'virtualenv -p python3 env',
            'source env/bin/activate'
            'pip3 install --upgrade pip'
            'pip3 install jupyter',
            'jupyter notebook --generate-config',
            'echo "c.NotebookApp.ip = \'0.0.0.0\'" >> .jupyter/jupyter_notebook_config.py',
            ]
    try:
        idx = 0
        for state in statement:
            os.system(state)
            idx += 1
    except Exception as ex:
        print(ex, 'FAIL, ERROR STATEMENT:')
        print(statement[idx])
        sys.exit(-1)
    print('success')


if __name__ == '__main__':
    main()
