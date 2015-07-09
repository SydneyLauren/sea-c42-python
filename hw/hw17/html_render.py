#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, name="", content=""):
        self.name = name
        self.content = content

    def append(self, new_child):
        self.content += new_child

    def render(self, file_out, ind=""):
        frontstr = "<" + self.name + ">\n"
        endstr = "\n<" + self.name + "/>\n"
        file_out.write(frontstr + self.content + endstr)
