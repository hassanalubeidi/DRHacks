
filepath = 'eprints-articles.json'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
#ID_PARSE
       if "eprintid" in line.strip():
           line = line[15:-4]
           print("ID is {}".format(line.strip()))

#TITLE_PARSE
       if "title" in line.strip():
           line = line[14:-5]
           print("Title is {}".format(line.strip()))

#AUTHOR_PARSE
       if "authors" in line.strip():
           line = fp.readline()
           line = line[7:-5]
           print("AUTHOR is {}".format(line.strip()))

       line = fp.readline()
