#!/usr/bin/python3
"""This module contains the append_after function to insert a line
after each line containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string."""
    # اقرأ كل الأسطر
    with open(filename, "r") as f:
        lines = f.readlines()

    # افتح الملف للكتابة وابدأ إعادة كتابة كل شيء مع الإضافة
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
