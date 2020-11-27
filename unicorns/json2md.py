#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

jsonfile = "unicorns.json"

f = open(jsonfile, "r")
unicorns = json.loads(f.read())

ebooktext = ""
ebooktext = ebooktext+"% "+unicorns['metadata']['title']+"\n"
ebooktext = ebooktext+"% "+unicorns['metadata']['author']+"\n"
ebooktext = ebooktext+"% "+unicorns['metadata']['date']+"\n"
ebooktext = ebooktext+"\n"
ebooktext = ebooktext+"---\n"
ebooktext = ebooktext+"title:    "+unicorns['metadata']['title']+"\n"
ebooktext = ebooktext+"subtitle: "+unicorns['metadata']['subtitle']+"\n"
ebooktext = ebooktext+"author:   "+unicorns['metadata']['author']+"\n"
ebooktext = ebooktext+"date:     "+unicorns['metadata']['date']+"\n"
ebooktext = ebooktext+"rights:   "+unicorns['metadata']['rights']+"\n"
ebooktext = ebooktext+"lang:     "+unicorns['metadata']['lang']+"\n"
ebooktext = ebooktext+"description: |\n"
ebooktext = ebooktext+"  "+unicorns['metadata']['description']+"\n"
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
    ebooktext = ebooktext+"<img class=\"emoji\" src=\"web/twemoji/"+chapter['emoji']+".svg\">\n"
    ebooktext = ebooktext+"\n"
  ebooktext = ebooktext+chapter['text']+"\n"
  ebooktext = ebooktext+"\n"
ebookpath = "unicorns.md"
print ebookpath
f = open(ebookpath, "w")
f.write(ebooktext.encode("utf-8"))
f.close()