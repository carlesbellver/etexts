#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

jsonfile = "unicorns.json"

f = open(jsonfile, "r")
unicorns = json.loads(f.read())

ebooktext = ""
ebooktext = ebooktext+"% "+unicorns['book']['title']+"\n"
ebooktext = ebooktext+"% "+unicorns['book']['author']+"\n"
ebooktext = ebooktext+"% "+unicorns['book']['date']+"\n"
ebooktext = ebooktext+"\n"
ebooktext = ebooktext+"---\n"
ebooktext = ebooktext+"title:    "+unicorns['book']['title']+"\n"
ebooktext = ebooktext+"subtitle: "+unicorns['book']['subtitle']+"\n"
ebooktext = ebooktext+"author:   "+unicorns['book']['author']+"\n"
ebooktext = ebooktext+"date:     "+unicorns['book']['date']+"\n"
ebooktext = ebooktext+"rights:   "+unicorns['book']['rights']+"\n"
ebooktext = ebooktext+"lang:     "+unicorns['book']['lang']+"\n"
ebooktext = ebooktext+"description: |\n"
ebooktext = ebooktext+"  "+unicorns['book']['description']+"\n"
ebooktext = ebooktext+"\n"
ebooktext = ebooktext+"...\n"
ebooktext = ebooktext+"\n"

for chapter in unicorns['chapters']:
  title = chapter['title']
  if (chapter['italics']):
    title = "*"+title+"*"
  if (chapter['untitled']):
    title = title+' {.untitled}'
  ebooktext = ebooktext+"# "+title+"\n"
  ebooktext = ebooktext+"\n"
  if (chapter['emoji']):
    ebooktext = ebooktext+"<img class=\"emoji\" src=\"web/twemoji/"+chapter['emoji']+".svg\" />\n"
    ebooktext = ebooktext+"\n"
  ebooktext = ebooktext+chapter['text']+"\n"
  ebooktext = ebooktext+"\n"
ebookpath = "unicorns.md"
print ebookpath
f = open(ebookpath, "w")
f.write(ebooktext.encode("utf-8"))
f.close()