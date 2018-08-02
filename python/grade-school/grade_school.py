class School(object):
  def __init__(self):
    self.students = {}

  def add_student(self, name, grade):
    self.students[name] = grade

  # Sort by grade, then by name
  def roster(self):
    keys = sorted([(v, k) for k, v in self.students.items()])
    return [x[1] for x in keys]

  def grade(self, grade_number):
    return sorted([name for name, k in self.students.items() if k == grade_number])
