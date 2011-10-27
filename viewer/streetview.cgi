#!/usr/bin/env python

import cgi
from mako.template import Template

form = cgi.FieldStorage()
lng = form.getvalue("lng", 0)
lat = form.getvalue("lat", 0)

print("Content-type: text/html\n\n")

mytemplate = Template(filename='streetview.mak.html')
print(mytemplate.render(latitude=lat,longitude=lng))
