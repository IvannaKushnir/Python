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

	def __str__(self):
		return "Name: {}, Surname: {}, Age: {} years old, Gender: {}, Course: {}".format(self.name, self.surname, self.age, self.gender, self.course)

students = []
try: 
	f = open('file_1.csv', 'r')
	reader = csv.reader(f)
	for row in reader:
		s = Student(row)
		students.append(s)
	f.close()

except IOError:
	print "File not found"

else:
	for student in students:
		if student.age > 30:
			print student

	print "1st search function"
	def Search(name, surname):
		for i in students:
			if i.name == name and i.surname == surname:
				return i

	a = Search ("Harry", "Grey")
	print a

	print "2nd search function"
	def SecondSearch(age):
		for k in students:
			if k.age == age:
				yield k

	a = SecondSearch (int(18))

	for m in a:
		print m

	print "3rd search function"
	print students[1]

finally:
	print "End"


