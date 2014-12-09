#!/usr/bin/python
# -*- coding: utf-8 -*-

html = u"""
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
            <title>Xu cat - Dune </title>
            <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
            <link rel="stylesheet" type="text/css" href="dune.css">
    </head>
    <body>
        <div id="title"> <a class="anav" href="preface.html"> XỨ CÁT - DUNE :: Franklin Patrick Herbert </a></div>

        <div id="navigator">
            <a href="dune{0}.html" class="anav" > << Previous </a> |
            <a  href="dune{1}.html" class="anav"> Next >> </a>
        </div>

        <div id="container">
            {2}
        </div>
        <div id="navigator" style=" position: initial; float: right; ">
                    <a href="dune{0}.html" class="anav"> &lt;&lt; Previous </a> |
                    <a href="dune{1}.html" class="anav"> Next &gt;&gt; </a>
                </div>
    </body>
</html>
"""

from pyquery import PyQuery
content = u""
for i in range(556):
    parse = open("chapter %s.html" % i).read()
    parse = parse.decode("utf8")
    tag = PyQuery(parse)("#container")
    if tag.html() == None:
        tag = PyQuery(parse)("body")
    tag.remove("style")
    ml = tag.html()
    content = content + ml


count = 0
lst = []
tags = PyQuery(html.format(0, 0, content))("#container")
for child in tags.children():
    try:
        if "page-break" in child.attrib["class"]:
            f = open("dune%d.html" % count, "w")
            out = html.format(max([0, count -1]), min([44, count + 1]),  u"".join ( PyQuery(x).outer_html() for x in lst ) )
            f.write(out.encode("utf-8"))
            f.close()
            count = count + 1
            lst = []
    except:
        pass

    lst.append(child)
