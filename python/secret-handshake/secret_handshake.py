code_map = {
  1: "wink",
  2: "double blink",
  4: "close your eyes",
  8: "jump"
}

def handshake(code):
  result = []

  for bit, action in code_map.items():
    if code & bit == bit:
      result.append(action)

  if code & 0x10 == 0x10:
    return result[::-1]
  else:
    return result

def secret_code(actions):
  inv_map = {v: k for k, v in code_map.items()}
  codes = [inv_map[action] for action in actions]

  if len(codes) > 1 and codes[0] > codes[-1]:
    codes.append(0x10)

  return sum(codes)
