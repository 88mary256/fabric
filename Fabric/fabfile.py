from fabric.api import run

def hello():
    print("Hello world!")

def host_type():
    run('uname -s')
