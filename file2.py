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

students = {}
try: 
	f = open('file_1.csv', 'r')
	reader = csv.reader(f)
	for row in reader:
		s = Student(row)
		students[s.name + " " + s.surname] = s
	f.close()

except IOError:
	print "File not found"

else:
	for k, v in students.interitems():
		if v.age > 30:
			print v

	print "1st search function"
	def Search(name, surname):
		for k, v in students.interitems():
			print student[s.name + " " + s.surname]

	a = Search ("Harry", "Grey")
	print a

	print "2nd search function"
	def SecondSearch(age):
		return student[s.name + " " + s.surname]

	a = SecondSearch (int(18))

	for m in a:
		print m

finally:
	print "End"


