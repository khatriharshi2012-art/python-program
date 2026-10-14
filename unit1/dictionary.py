#create a dictionary

student = {'name':'Rahul',
           'course':"MCA",
           'semester':3,
           'marks':85}

#1. print the dictionary items
print("dictionary:",student)

#2. Access items
print("Student Name:",student['name'])
print("Course:",student['course'])

#3. Use get()
print("Semester:",student.get('semester'))
print("Marks:",student.get('marks'))

#4. change values
student['marks']= 90
student['semester']= 4

print("dictionary after changing:",student)

#5. Use len()
print("Number of items:",len(student))