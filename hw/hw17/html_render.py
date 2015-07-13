#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, name="", content=""):
        self.name = name
        # self.content = content
        self.children = [content] if content else []

    def append(self, new_child):
            self.children.append(new_child)

    def render(self, file_out, ind="    "):
        self.indent = ind
        IND_LEVEL = "    "
        # append the html thingies, indent, and content and write file
        file_out.write("%s<%s>" % (self.indent, self.name))
        for child in self.children:
            if (type(child) == str):
                file_out.write("\n" + self.indent + IND_LEVEL + child)
            else:
                # Add new child node by recursively rendering
                child.render(file_out, self.indent + IND_LEVEL)
        file_out.write("\n%s</%s>" % (self.indent, self.name))


class Html(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="html", content="<!DOCTYPE html\n")

    def render(self, file_out, indent="    "):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, "")


class Body(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="body", content=content)


class P(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="p", content=content)
