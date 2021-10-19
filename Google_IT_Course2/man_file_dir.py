# accepts files and return the filesize
# !/usr/bin/env python3
import os
import os.path
import re

"""
def create_python_script(filename):
    comments = "This course is all about using Python to interact with the operating system\n" \
               "Thus, managing files and directories on your operating system."
    with open(filename, 'w') as file:
        file.write(comments)

        filesize = len(filename)

    return filesize


print(create_python_script('file.txt'))
"""


def rearrange_name(name):
    results = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if results is None:
        return name
    return "{} {}".format(results[2], results[1])


result = rearrange_name("Busah, Irene")
print(result)
