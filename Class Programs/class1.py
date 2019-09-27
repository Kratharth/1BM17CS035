class student:
	def __init__(self):
		self.i = None
		self.m = None
		self.a = None
	
	def set(self,student_id,marks,age):
		self.i = student_id
		self.m = marks
		self.a = age
	
	def get(self):
		print('Id is :' + str(self.i))
		print('Marks is : ' + str(self.m))
		print('Age is : '+ str(self.a))

	def validate_marks(self):
		return self.m >=0 and self.m <= 100

	def validate_age(self):
		return self.a > 20

	def checkqualification(self):
		if self.validate_marks() and self.validate_age():
			if self.m >= 65:
				return True
		return False

if __name__ == '__main__':
	num_students = int(input('enter the number of students'))
	students = []
	for i in range(num_students):
		students.append(student())
	
	for i in range(num_students):
		print('enter the details of the student' + str(i+1))
		student_id = int(input('enter the id'))
		marks = int(input('enter the marks'))
		age = int(input('enter the age'))
		students[i].set(student_id,marks,age)
	
	for i in range(num_students):
		if students[i].checkqualification():
			print('student ' + str(i+1) + ' is qualified')
			print('His/Her details are : ',end = ' ' )
			students[i].get()
		else:
			print('Student ' +str(i+1) + ' is not qualified')
					
