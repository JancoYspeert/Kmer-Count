#! usr/bin/python

def combinefiles():
  
  infile1 = open('ABFKmerCount1.txt','r')
  infile2 = open('ABFKmerCount2.txt','r')
  infile3 = open('ABFKmerCount3.txt','r')
  infile4 = open('ABFKmerCount4.txt','r')
  
  outfile = open('Count8mers.txt', 'w')
  
  i = 1
  
  while (i<=32768):
    A = infile1.readline()
    B = infile2.readline()
    C = infile3.readline()
    D = infile4.readline()
    
    ListA = A.strip().split('\t')
    ListB = B.strip().split('\t')
    ListC = C.strip().split('\t')
    ListD = D.strip().split('\t')
    
    Kmer = ListA[0]
    Revcomp = ListA[1]
    
    Total = int(ListA[2]) + int(ListB[2]) +int(ListC[2])+int(ListD[2])
    
    outfile.write(Kmer + '\t' + Revcomp + '\t' + str(Total) +'\n')
    
    print "done ", i ," of 32768 lines"
    i = i+1
  
  infile1.close()
  infile2.close()
  infile3.close()
  infile4.close()
  outfile.close()
  
  return 0 