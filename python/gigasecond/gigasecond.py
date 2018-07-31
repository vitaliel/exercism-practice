from datetime import timedelta

GIGASECOND = 10 ** 9

def add_gigasecond(birth_date):
  return birth_date + timedelta(seconds=GIGASECOND)
