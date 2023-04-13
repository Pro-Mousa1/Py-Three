from database import User,Student,Teacher
# Try to save the users in the table

try:
    User.create(name="Mousa", email="mousamuigai13@gmail.com", password="123")
except:
    print("Please use a different email")

# Display all users saved in the database on the table called Users
users = User.select()
# Write a loop to display all the users
for user in users:
    print(user.name, user.email, user.password)

# Try to save the students in the table

try:
    Student.create(name="Mousa", adm_no="ADM3", course="Python")
except:
    print("Enter correct data")

students = Student.select()
# Write a loop to display all the users
for student in students:
    print(student.name, student.adm_no, student.course)


# Try to save the teachers in the table

try:
    Teacher.create(name="Mrs.Angel", tsc_no="1718513", subject ="Medicine",
                   school="Hacettepe")
except:
    print("Enter a different tsc_no")


teachers = Teacher.select()

for teacher in teachers:
    print(teacher.name, teacher.tsc_no, teacher.subject, teacher.school)

