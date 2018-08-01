def is_armstrong(number):
  digits = [int(d) for d in str(number)]
  power = len(digits)

  result = 0
  for d in digits:
    result += d ** power
    if result > number:
      return False

  return result == number
