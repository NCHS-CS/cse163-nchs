""" 
This activity is going to help you understand how to use the __file__ variable to get the path of the current file.
To start off first test this code out. It prints out a few lines from our LICENSE file.

Run: `python classwork/file-path/file-path.py`
This should print out lines 10 to 15 of the LICENSE file.
Now try changing your current directory and see if it still works.
Run: `cd classwork/file-path`
Now try running the file again
Run: `python file-path.py`
Note: the print of __file__ didn't change! This is because __file__ is the path to the current file, not the current working directory.
Figure out how to fix the code so that it works no matter what your current working directory is. 
You will need to use the __file__ variable to get the path of the current file and then use that to get the path of the LICENSE file.
"""

from pathlib import Path

print("__file__ is:", __file__)
with open("LICENSE") as f:
    print('\n'.join(f.readlines()[10:15]))

