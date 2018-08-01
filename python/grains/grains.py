RANGE_ERROR = ValueError("N should be in range 1..64")

def on_square(n):
  if n <= 0 or n > 64:
    raise RANGE_ERROR

  result = 1
  for _ in range(n - 1):
    result *= 2

  return result

def total_after(n):
  if n <= 0 or n > 64:
    raise RANGE_ERROR

  total = result = 1

  for _ in range(n - 1):
    result *= 2
    total += result

  return total
