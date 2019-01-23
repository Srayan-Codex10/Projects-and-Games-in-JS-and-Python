sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
  dna_data = ""
  with open(dna_file,"r") as f :
    for line in f :
      dna_data += line
    if f.closed != True:
      f.close()
  return dna_data

def dna_codons(dna):
  codons = []
  for i in range(0,len(dna),3):
    if (i+3) < len(dna):
      codons.append(dna[i:i+3])
  return codons

def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample :
      matches += 1
  return matches

def is_criminal(dna_sample,count):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3 :
    print(" %d matches, Continue Investigation on Suspect %d... " % (num_matches,count))
  else:
    print("Suspect %d Innocent..." % (count))

is_criminal("suspect1.txt",1)
is_criminal("suspect2.txt",2)
is_criminal("suspect3.txt",3)

    
