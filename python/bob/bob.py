def hey(phrase):
  text = phrase.strip()
  is_yelling = text == text.upper() and text != text.lower()

  if text == '':
    return 'Fine. Be that way!'
  elif text[-1] == '?':
    if is_yelling:
      return 'Calm down, I know what I\'m doing!'
    else:
      return 'Sure.'
  elif is_yelling:
    return 'Whoa, chill out!'
  else:
    return 'Whatever.'
