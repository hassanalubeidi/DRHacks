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

           with open("tmp.txt", "a") as myfile:
               myfile.write("!"+ line.strip() + "\n")

#TITLE_PARSE
       if "title" in line.strip():
           line = line[14:-5]

           with open("tmp.txt", "a") as myfile:
               myfile.write("@"+ line.strip() + "\n")

#TYPE_PARSE
#       if "'"'type'"':" in line.strip():
       if "\"type\"" in line.strip():
#           (["'])(?:(?=(\\?))\2.)*?\1
           line = line[13:-5]
           with open("tmp.txt", "a") as myfile:
               myfile.write("#"+ line.strip() + "\n")

#jsonURI_PARSE
       if "json_uri" in line.strip():
           line = line[17:-3]

           with open("tmp.txt", "a") as myfile:
               myfile.write("\n" + "$"+ line.strip() + "\n")

#Get filesize
           d = urllib.urlopen(line)
           data = json.loads(d.read())
           fs = str(data['documents'][0]['files'][0]['filesize'])

           with open("tmp.txt", "a") as myfile:
               myfile.write("%"+ fs  + "\n \n")

#AUTHOR_PARSE
       if "authors" in line.strip():
           line = fp.readline()
           line = line[7:-5]

           with open("tmp.txt", "a") as myfile:
               myfile.write("^"+ line.strip())

       line = fp.readline()
