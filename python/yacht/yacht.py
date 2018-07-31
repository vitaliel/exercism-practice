# Score categories
# Change the values as you see fit
YACHT = "Yacht"
ONES = "Ones"
TWOS = "Twos"
THREES = "Threes"
FOURS = "Fours"
FIVES = "Fives"
SIXES = "Sixes"
FULL_HOUSE = "FullHouse"
FOUR_OF_A_KIND = "FourOfAKind"
LITTLE_STRAIGHT = "LittleStraight"
BIG_STRAIGHT = "BigStraight"
CHOICE = "Choice"

def score(dice, category):
  if category == YACHT:
    expected = [dice[0] for i in range(0, len(dice))]

    if dice == expected:
      return 50
    else:
      return 0
  elif category == ONES:
    return search(dice, 1)
  elif category == TWOS:
    return search(dice, 2)
  elif category == THREES:
    return search(dice, 3)
  elif category == FOURS:
    return search(dice, 4)
  elif category == FIVES:
    return search(dice, 5)
  elif category == SIXES:
    return search(dice, 6)
  elif category == CHOICE:
    return sum(dice)
  elif category == FOUR_OF_A_KIND:
    d = index_values(dice)
    for key in range(1, 7):
      if d[key] >= 4:
        return key * 4
  elif category == FULL_HOUSE:
    if four_of_a_kind(dice) > 0 or is_two_of_a_kind(dice):
      return 0
    return sum(dice)
  elif category == LITTLE_STRAIGHT and sorted(dice) == [1, 2, 3, 4, 5]:
    return 30
  elif category == BIG_STRAIGHT and sorted(dice) == [2, 3, 4, 5, 6]:
    return 30

  return 0

def search(dice, value):
  result = 0

  for i in dice:
    if i == value:
      result += 1

  return result * value

def index_values(dice):
  d = {x: 0 for x in range(1, 7) }
  for v in dice:
    d[v] += 1

  return d

def sum(dice):
  result = 0

  for i in dice:
    result += i

  return result

def four_of_a_kind(dice):
  d = index_values(dice)
  for key in range(1, 7):
    if d[key] >= 4:
      return key * 4
  return 0

def is_two_of_a_kind(dice):
  d = index_values(dice)
  count = 0

  for key in range(1, 7):
    if d[key] == 2:
      count += 1

  return count == 2
