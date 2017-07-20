#! usr/bin/python

def splitfile(infile):

  
  fle = open(str(infile), "r")
  outfile1 = open("ABFsplit1.fa", "w")
  outfile2 = open("ABFsplit2.fa", "w")
  outfile3 = open("ABFsplit3.fa", "w")
  outfile4 = open("ABFsplit4.fa", "w")
  
  counter = 1
  
  while (counter <= 320497):
    line = fle.readline()
    outfile1.write(line)
    counter = counter + 1
    print counter, "of 1281988"
  
  while (counter <= 640994):
    line = fle.readline()
    outfile2.write(line)
    counter = counter + 1
    print counter, "of 1281988"
  
  while (counter <= 961491):
    line = fle.readline()
    outfile3.write(line)
    counter = counter + 1
    print counter, "of 1281988"

  while (counter <= 1281988):
    line = fle.readline()
    outfile4.write(line)
    counter = counter + 1
    print counter, "of 1281988"
  
  outfile1.close()
  outfile2.close()
  outfile3.close()
  outfile4.close()
  
  return 0