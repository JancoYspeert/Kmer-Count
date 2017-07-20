#! usr/bin/python

def make8merfiles():
  bases = ["A","C","G","T"]
  list1 = [A+B+C+D+E+F+G+H for A in ["A","C"] for B in bases for C in bases for D in bases for E in bases for F in bases for G in bases for H in bases]
  outfile = open("KmerList.txt", "w")
  counter = 0 
  for i in list1:
    outfile.write(i)
    counter = counter +1
    print counter
  print "Finished file"
    
