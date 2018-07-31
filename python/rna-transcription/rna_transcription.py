# * `G` -> `C`
# * `C` -> `G`
# * `T` -> `A`
# * `A` -> `U`
def encode(dna_nucleotide):
  if dna_nucleotide == 'G':
    return 'C'
  elif dna_nucleotide == 'C':
    return 'G'
  elif dna_nucleotide == 'T':
    return 'A'
  elif dna_nucleotide == 'A':
    return 'U'
  else:
    raise Exception("Bad DNA nucleotide")

def to_rna(dna_strand):
  result = ''

  for x in range(0, len(dna_strand)):
    result += encode(dna_strand[x])

  return result
