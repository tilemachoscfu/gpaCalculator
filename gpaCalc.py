class Course:
  def __init__(self, grade, credits, name = "N/A"):
    self.grade   = score[grade]
    self.letter  = grade
    self.credits = credits
    self.name    = name

score = {
  'A' : 4.000,
  'A-': 3.667,
  'B+': 3.333,
  'B' : 3.000,
  'B-': 2.667,
  'C+': 2.333,
  'C' : 2.000,
  'C-': 1.667,
  'D+': 1.333,
  'D' : 1.000,
  'D-': 0.667,
  'F' : 0.000
}

spring2018 = [
  Course('A', 4, "Operating Systems"),
  Course('B', 4, "Algorithms"),
  Course('A-', 4, "GIS"),
  Course('A-', 4, "Finite Mathematics")
]

def gpa(semester):
  total_score = 0
  total_credits = 0

  for course in semester:
    score = course.grade * course.credits
    total_score += score
    total_credits += course.credits

  gpa = total_score / total_credits
  return gpa

print (gpa(spring2018))
