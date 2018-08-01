PLANTS = {x[0]: x for x in "Radishes Clover Grass Violets".split()}
STUDENTS = "Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()

class Garden(object):
  def __init__(self, diagram, students = None):
    self.rows = diagram.split()

    if not students:
      self.students = STUDENTS
    else:
      self.students = sorted(students)

  def plants(self, student_name):
    idx = self.students.index(student_name) * 2
    return [PLANTS[row[idx + i]] for row in self.rows for i in [0, 1]]
