class Allergies(object):
  def __init__(self, score):
    user_allergies = []
    new_score = score & 0xff;

    allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate',
                 'pollen', 'cats']
    idx = 0
    while new_score > 0:
      if new_score & 1 == 1:
        user_allergies.append(allergies[idx])
      idx += 1
      new_score = new_score >> 1

    self.user_allergies = user_allergies

  # item string allergy
  def is_allergic_to(self, item):
    return item in self.user_allergies

  @property
  def lst(self):
    return self.user_allergies
