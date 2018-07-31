def largest_product(series, size):
  d_len = len(series)

  if size == 0:
    return 1
  elif size < 0:
    raise ValueError('size should be positive integer')
  elif size > d_len:
    raise ValueError('size is bigger than series length')

  digits = [int(n) for n in series]

  if d_len == size:
    return multiply(digits)

  max_p = multiply(digits[0:size])
  i = 1

  while i <= d_len - size:
    cp = multiply(digits[i:i+size])
    if cp > max_p:
      max_p = cp
    i += 1

  return max_p

def multiply(lst):
  result = 1
  for n in lst:
    result *= n

  return result
