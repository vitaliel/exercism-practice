def distance(strand_a, strand_b):
  len_a = len(strand_a)
  if len_a != len(strand_b):
    raise ValueError("DNA strands length should be the same")

  count = 0
  for i in range(len_a):
    if strand_a[i] != strand_b[i]:
      count += 1

  return count
