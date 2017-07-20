#! usr/bin/python
  
def stripfile(filename,outfile):
  """ Strips the DNaseClustered.fa file of most unnessary - for this project - information. Since we are only interested
  in how often a k-mer come up, the Chromosomal placement is unimportant. Similarly, one N is enough to act as a break 
  character... we don't need rows of N's for this project! """
  
  fle = open(str(filename), "r")
  outfile = open(str(outfile), "w")
  gen = ""
  counter = 1
  Nmarker = 0
  line = fle.readline()
  
  while (line != ""):
    print "Stripfile has read ", counter, "lines of 2563976"
    if (line[0] == ">"):
      counter = counter + 1
      line = fle.readline()
      continue
    else:
      for i in range(len(line)):
	if (Nmarker == 0):
	  if (line[i] != "N"):
	    gen = gen + line[i]
	    #Nmarker = 0
	    continue
	  if (line[i] == "N"):
	    gen = gen + line[i]
	    Nmarker = 1
	    continue
	else:   # (Nmarker == 1):
	  if (line[i] == "N"):
	    continue
	  else:
	    gen = gen + line[i]
	    Nmarker = 0

     
	outfile.write(gen)
	gen = ""

      counter = counter + 1
      line = fle.readline()
      
  return 0



