#! usr/bin/python
from linecache import getline

def revcomp(DNA):
    DNA2 = DNA.lower()
    DNA2 = DNA2.replace("g","C")
    DNA2 = DNA2.replace("c","G")
    DNA2 = DNA2.replace("a","T")
    DNA2 = DNA2.replace("t","A")
    DNA3 = DNA2[::-1]
    return DNA3


def getLineNo(Kmer):
  countDic = {"A" :0, "C" : 1, "G" : 2, "T" : 3}
  length = len(Kmer)
          
  if (Kmer[0] == "G"):
    lineNo = 32769   
    for i in range(1,length-1):
      lineNo = lineNo + (countDic.get(Kmer[i])*(2**(2*(length-i-1)-1)))
    if (Kmer[7] == "C"): 
      lineNo = lineNo + 1
    return lineNo

  elif (Kmer[0] == "T"):
    lineNo = 40961
    for i in range(1,length-1):
      lineNo = lineNo + (countDic.get(Kmer[i])*(4**(length-i-2))) 
    return lineNo

  else:  
    lineNo=1
    for i in range(length):
      lineNo = lineNo + (countDic.get(Kmer[i])*(4**(length-i-1)))
    return lineNo



def countGapped(Kmer, dots):
  total = 0
  bases = ["A","C","G","T"]
  firstDot = Kmer.index(".") 
  
  if (dots > 1):
    for i in bases:
      Kmer2 = Kmer[:(firstDot)] + i + Kmer[(firstDot+1):]
      total = total + countGapped(Kmer2, dots-1)
    return total

  if (dots == 1):
    for i in bases:
      Kmer2 = Kmer[:firstDot] + i + Kmer[firstDot+1:]
      total = total + KmerCount(Kmer2)
    return total  
  
  
  
def KmerCount(Kmer):
  
  if (len(Kmer) != 8):
    print  "Please input a Kmer of length 8"
  
  dots = 0
  for i in range(len(Kmer)):
    if (Kmer[i] == "."):
      dots = dots + 1 #(could probably just use str.count that would also possible, in another part of my whole solution,
			# solve the problem of finding multiple instances of a Kmer in the same line)
  if (dots > 0):
    total = countGapped(Kmer, dots)
    return total
  else:
    rc = revcomp(Kmer)
    rcSmaller = 0 
  
    if (rc < Kmer):
      rcSmaller = 1
      lineNo = getLineNo(rc)
  
    else:
      lineNo = getLineNo(Kmer)
  
    line = getline('Count8mers.txt', lineNo)
    print line  
    LineList = line.strip().split('\t')
  
    return int(LineList[2])