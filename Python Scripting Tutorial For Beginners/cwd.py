import os

def current_directory():
    print(os.getcwd())

current_directory()
# /home/maruf/Documents/python/Python Scripting Tutorial For Beginners

def file_abs_path():
    print(os.path.abspath(__file__))
def file_real_path():
    print(os.path.realpath(__file__))

file_abs_path()
file_real_path()
# /home/maruf/Documents/python/Python Scripting Tutorial For Beginners/cwd.py
# /home/maruf/Documents/python/Python Scripting Tutorial For Beginners/cwd.py