#!/usr/bin/env python
# encoding: utf-8

import getpass
import sys
import os

def main():
    try:
	os.system('rm -rf ~/.pip')
    except Exception as ex:
        pass
    finally:
        os.system('cd ~')
        os.mkdir('.pip')

    state = 'echo "[global]" >> ~/.pip/pip.conf &&\
            echo "trusted-host=mirrors.aliyun.com" >> ~/.pip/pip.conf &&\
            echo "index-url=https://mirrors.aliyun.com/pypi/simple/" >> ~/.pip/pip.conf &&\
            apt-get install zip tar &&\
	        pip3 install --upgrade pip &&\
            pip3 install virtualenv &&\
            virtualenv -p python3 env &&\
            . env/bin/activate &&\
            pip install jupyter &&\
            pip install tensorflow-gpu==1.3.0 &&\
            jupyter notebook --generate-config &&\
            echo "c.NotebookApp.ip = \'0.0.0.0\'" >> ~/.jupyter/jupyter_notebook_config.py && \
            echo "c.NotebookApp.open_browser = False" >> ~/.jupyter/jupyter_notebook_config.py'
    os.system(state)

if __name__ == '__main__':
    user = getpass.getuser()
    if user != 'root':
        print('current user {}, please use root'.format(user))
        sys.exit(-1)
    main()
