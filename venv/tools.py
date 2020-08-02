import subprocess as sp
from time import sleep

def clear_screen():
    sp.call('cls', shell=True)

def sleep(seconds):
    sleep(seconds)
