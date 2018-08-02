PLANTS = {x[0]: x for x in "Radishes Clover Grass Violets".split()}
STUDENTS = "Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()

class Garden(object):
  def __init__(self, diagram, students = None):
    self.rows = diagram.split()
    self.students = STUDENTS

    if students:
      self.students = sorted(students)

  def plants(self, student_name):
    index = self.students.index(student_name) * 2
    return [PLANTS[row[index + i]] for row in self.rows for i in [0, 1]]
