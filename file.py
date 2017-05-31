import csv

class Person:
	def __init__(self, name, surname, age, gender):
		self.name = name
		self.surname = surname
		self.age = age
		self.gender = gender	

class Student(Person):
	Person.__init__(self, name, surname, age, gender)
	self.course = course

	def __init__(self, row):
		Student.__init__(self, row[0].strip(), row[1].strip(), row[2].strip(), int(row[3].strip()), row[4].strip())

	def __str__(self):
		return "Name: {}, Surname: {}, Age: {} years old, Gender: {}".format(self.name, self.surname, self.age, self.gender)
		Students.append(s)


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
			if name == name and surname == surname:
				return i