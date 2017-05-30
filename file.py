import csv

class Person:
	def __init__(self, name, surname, age, gender):
		self.name = name
		self.surname = surname
		self.age = age
		self.gender = gender	

class Student(Person):
	def __init__(self, name, surname, course, age, gender):
		self.name = name
		self.surname = surname
		self.course = course
		self.age = age
		self.gender = gender


	def __init__(self, row):
		self.name = row[0].strip()
		self.surname = row[1].strip()
		self.course = row[2].strip()
		self.age = int(row[3].strip())
		self.gender = row[4].strip()		
		students.append(student)

students= []

f = open('file_1.csv', 'r')
reader = csv.reader(f)
for row in reader:
	print row
f.close()

for student in students:
	if student.age >30:
		print student.name + " " + student.surname

	def Search(name, surname):
		for i in students:
		    return "Hello, {} {}. Are you {} years old?".format(name, surname, age)