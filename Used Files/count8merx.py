#! /usr/bin/python
import subprocess
import time
from multiprocessing import Pool


def revcomp(DNA):
    DNA2 = DNA.lower()
    DNA2 = DNA2.replace("g","C")
    DNA2 = DNA2.replace("c","G")
    DNA2 = DNA2.replace("a","T")
    DNA2 = DNA2.replace("t","A")
    DNA3 = DNA2[::-1]
    return DNA3

def count8mer(jobno):
  
  infile = "ABFsplit"+str(jobno)+".fa"
  listfile = "KmerList"+str(jobno)+".txt"
  outfile = "ABFKmerCount"+str(jobno)+".txt"
  tic = time.time()
  i = 1
  kmerlist = open(listfile,"r")
  output = open (outfile,"w")
  
  while (i<=32768): #should be 32768
    kmer = kmerlist.read(8)
    rc = revcomp(kmer)
    if (kmer == rc):  #pallendrome
      count = subprocess.check_output(["grep", "-c", kmer, infile])
      count = int(count)
      output.write(kmer + '\t' + rc + '\t' + str(count) + '\n')
    else:
      grepex = kmer + """\|""" + rc
      forward = subprocess.check_output(["grep", "-c", str(grepex), infile])
      forward = int(forward)
      output.write(kmer + '\t' + rc + '\t' + str(forward) + '\n')
    if (i%300==0):
     print "job ", jobno ," has counted ", i ,"of 32768 kmers"  
    i = i+1

  toc = time.time()
  taken = toc - tic
  kmerlist.close()
  output.close()
  print "job", jobno ,"time taken = ", str(taken)
  return 0
  
if __name__ == '__main__':

  pool = Pool(processes=4)	
  results = pool.map(count8mer, (1,2,3,4))