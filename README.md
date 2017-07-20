## Kmercounter, Used and program files

This program was used to count the number of instancs of each Kmer of a specified length in the standard example of the human genome. A kmer is a string of length K, consisting of DNA bases "A","C", "T" and "G" and wildcards "\*". The original file was 420 Mbs large, and contained extraneous data for my purposes. Through various manipulations, included in the "used files" directory, I managed to strip the file to 280 megs. Unfortunately, these This file was then split into four segments, to enable parallel processing. Each segment returned a count file, and these were combined, to create the text file Count8mers.txt in Program files. The file Count8mers.py uses simple mathematics to look up the correct line of the input Kmer and return its count in the dna, and some basic recursion to calculate counts.

Skills used: Data Cleanig and processing, parallel processing.
