#creating list of students in 2 classrooms:

class_1 = ['Abhishek','Akshay','vishal','hemant']
class_2 = ['Rohit ','sagar','Prasad']

#combining both lists to create one common list of students:

new_class = class_1 + class_2
print(new_class)


#adding the name of a student who was missing :
new_class.append('Rahul')
print(new_class)

new_class.remove('Akshay')
print(new_class)



#Lets calculate the % score of 'Vishal':
#creating a dictionary of marks obtained by 'vishal' in respective subjects:
# and adding all Marks

# Creating a dictionary of courses

courses = {'Math': 68, 'English':70, 'History': 85, 'Geography': 70, 'Science': 60}

total = courses['Math'] + courses['English'] + courses['History'] + courses['Geography'] + courses['Science']
print(total)

# since all marks obtained are outof 100

percentage = (total / 500) * 100
print(percentage)


#Now to find the topper in mathematics, we create another dictionary of students with their respective maths score:
mathematics = {'Abhishek bhujbal':78, 'Hemant hadawale':95, 'rohit pawar':65, 'Rahul kadam':50, 'Pooja bhosale':70, 'sagar jadahv':66, 'Rahul joshi':75}

#compares the value & returns the key:
topper = max(mathematics, key = mathematics.get)
print(topper)

#to get the last name first:

first_name = topper.split()[0]
last_name = topper.split()[1]
full_name = last_name + ' ' + first_name
print(full_name)


#to highlight the name, printing in uppercase:

uppercase_name = full_name.upper()
print(uppercase_name)
