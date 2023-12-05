import csv

number_of_choices = int(input("Number of choices given to students (Give a number): "))
counterdict = {} #dictionary to count number of students in each course
for i in range (number_of_choices):
    counterdict[i] = 0
    
word_to_number = {'1st Choice': 0, '2nd Choice' : 1, '3rd Choice': 2, '4th Choice' : 3, '5th Choice' : 4, '6th Choice' : 5}
assign_class_tonum = { '4B' : 0 , '4C' : 1, '4I' : 2, "4K" : 3, '4M' : 4, '4P' : 5, '4R' : 6}

stdl = [] #list of students

class student:
    #c1 is colum 1, c2 is column 2, etc
    def __init__(self, name, clas, c1, c2, c3, c4, c5, c6):
        self.name = name.upper()
        self.clas = clas
        self.choice = [c1, c2, c3, c4, c5, c6]
        self.course = int()

    def sort(self):
        for i in range (number_of_choices): #looping through in order of student's preferance
            for j in range(number_of_choices): #looping through the courses
                    if word_to_number[self.choice[j]] == i:
                        if counterdict[j] < 30:
                            self.course = j 
                            counterdict[j] += 1
                            return

duplicate = dict() 
with open ('data1.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    #saving as a dictionary first to remove all duplicate responses via checking email (Some students send in multiple responses with same email)
    for row in csv_reader:
        duplicate[row[1]] = row
        
objl = list(duplicate.values())
for row in objl:    
    stdl.append(student(row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

for students in stdl:
    students.sort()

write_list_bycourse = [] #sorting by student's course
for i in range (6):
    for students in stdl:
        if students.course == i:
            write_list_bycourse.append([students.name, students.course, students.clas])

#sorting by student's class
write_list_byclass = [] 
for i in range(7): 
    for students in stdl:
            if assign_class_tonum[students.clas] == i:
                write_list_byclass.append([students.name, students.course, students.clas])

#First output to sort by course
header = ['name' , 'course', 'class']
with open('bycourse.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(write_list_bycourse)

#Second output to sort by class:
header = ['name' , 'course', 'class']
with open('byclass.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(write_list_byclass)

print(len(stdl))




            
        

