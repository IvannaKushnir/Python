import csv

class Person:
	def __init__(self, name, surname, age, gender):
		self.name = name
		self.surname = surname
		self.age = age
		self.gender = gender	

class Student(Person):
	def __init__(self, row):
		Person.__init__(self, row[0].strip(), row[1].strip(), int(row[3].strip()), row[4].strip())
		self.course = row[2].strip()

	def __str__(self, row):
		return "Name: {}, Surname: {}, Age: {} years old, Gender: {}".format(self.name, self.surname, self.age, self.gender)

students= []

f = open('file_1.csv', 'r')
reader = csv.reader(f)
for row in reader:
	s = Student(row)
	students.append(s)
f.close()

for student in students:
	if student.age > 30:
		print student
