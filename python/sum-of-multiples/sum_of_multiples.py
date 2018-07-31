def sum_of_multiples(limit, multiples):
  if len(multiples) == 0:
    return 0

  result = 0

  for n in range(limit):
    for m in multiples:
      if n % m == 0:
        result += n
        break

  return result
