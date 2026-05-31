#typecasting is process coverting variable to datatype
name ="kanmani"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(gpa))

gpa= int(gpa)
print(gpa)
age= float(age)
print(age)
name=str(name)
print(name)

name= bool(name)
print(name)