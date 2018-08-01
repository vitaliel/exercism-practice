def is_pangram(sentence):
  letters = {chr(x): 0 for x in range(97, 97 + 26) }

  for letter in sentence.lower():
    try:
      letters[letter] += 1
    except KeyError:
      pass

  for v in letters.values():
    if v == 0:
      return False

  return True
