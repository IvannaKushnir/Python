import csv

class Student:
	def __init__(self, name, surname, course, age, gender):
		self.name = name
		self.surname = surname
		self.course = course
		self.age = age
		self.gender = gender

students= []

f = open('file_1.csv', 'r')
reader = csv.reader(f)
for row in reader:
    student = Student(row[0].strip(), row[1].strip(), row[2].strip(), int(row[3].strip()), row[4].strip())
	students.append(student)
	print row
	
f.close()

for student in students:
	if student.age >30:
		print student.name + " " + student.surname
