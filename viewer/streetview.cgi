#!/usr/bin/env python

import cgi
from mako.template import Template

form = cgi.FieldStorage()
lng = form["lng"].value
lat = form["lat"].value

print("Content-type: text/html\n")

mytemplate = Template(filename='streetview.mak.html')
print(mytemplate.render(latitude=lat,longitude=lng))
