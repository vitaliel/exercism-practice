def sum_of_multiples(limit, multiples):
  numbers = set()

  for m in multiples:
    for i in range(m, limit, m):
      numbers.add(i)

  return sum(numbers)
