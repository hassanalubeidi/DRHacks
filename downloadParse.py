#!/usr/bin/env python

import urllib, json
import os
import sys

filepath = 'eprints-articles.json'

open("tmp.txt", "w").close()

with open(filepath) as fp:
   line = fp.readline()
 #! - id, @ - Title, # - Type, $ - URI, % - Size, ^ - Author
   while line:
#ID_PARSE
       if "eprintid" in line.strip():
           line = line[15:-4]
           print("ID is {}".format(line.strip()))
           with open("tmp.txt", "a") as myfile:
               myfile.write("!"+ line.strip() + "\n")

#TITLE_PARSE
       if "title" in line.strip():
           line = line[14:-5]
           print("Title is {}".format(line.strip()))
           with open("tmp.txt", "a") as myfile:
               myfile.write("@"+ line.strip() + "\n")

#TYPE_PARSE
#       if "'"'type'"':" in line.strip():
       if "\"type\"" in line.strip():
#           (["'])(?:(?=(\\?))\2.)*?\1
           line = line[13:-5]
           print("Type is {}".format(line.strip()))
           with open("tmp.txt", "a") as myfile:
               myfile.write("#"+ line.strip() + "\n")

#jsonURI_PARSE
       if "json_uri" in line.strip():
           line = line[17:-3]
           print("URI is {}".format(line.strip()))
           with open("tmp.txt", "a") as myfile:
               myfile.write("$"+ line.strip() + "\n")

#Get filesize
           d = urllib.urlopen(line)
           data = json.loads(d.read())
           fs = str(data['documents'][0]['files'][0]['filesize'])
           print "File Size is: "  + fs
           with open("tmp.txt", "a") as myfile:
               myfile.write("%"+ fs  + "\n \n")

#AUTHOR_PARSE
       if "authors" in line.strip():
           line = fp.readline()
           line = line[7:-5]
           print("AUTHOR is {}".format(line.strip()))
           with open("tmp.txt", "a") as myfile:
               myfile.write("^"+ line.strip())

       line = fp.readline()
