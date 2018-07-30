class Allergies(object):
  def __init__(self, score):
    list = []
    new_score = score & 0xff;

    allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate',
                 'pollen', 'cats']
    idx = 0
    while new_score > 0:
      if new_score & 1 == 1:
        list.append(allergies[idx])
      idx += 1
      new_score = new_score >> 1

    self.list = list

  # item string allergy
  def is_allergic_to(self, item):
    return item in self.list

  @property
  def lst(self):
    return self.list
