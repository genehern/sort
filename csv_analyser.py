import csv

stdl = [] #list of students
duplicate = dict() 
counterdict = {1 : 0 , 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0} #the key represents the column number
word_to_number = {'1st Choice': 1, '2nd Choice' : 2, '3rd Choice': 3, '4th Choice' : 4, '5th Choice' : 5, '6th Choice' : 6}

class student:
    #c1 is colum 1, c2 is column 2, etc
    def __init__(self, name, clas, c1, c2, c3, c4, c5, c6):
        self.name = name.upper()
        self.clas = clas
        self.choice = [c1, c2, c3, c4, c5, c6]
        self.course = int()

    def sort(self):
        for i in range (1,6):
            for j in range (1,6):
                if word_to_number[self.choice[j]] == i:
                    self.course = i #i = which column number
                    counterdict[i] += 1


with open ('data1.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    #saving as a dictionary first to remove all duplicate responses via checking email.
    for row in csv_reader:
        duplicate[row[1]] = row
        
objl = list(duplicate.values())
for row in objl:    
    stdl.append(student(row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

write_list = []
for students in stdl:
    students.sort()
#write_list.append([students.name, students.clas, students.course]) 

for i in range (1,6):
    for students in stdl:
        if students.course == i:
            write_list.append([students.name, students.course, students.clas])


header = ['name' , 'course', 'class']
with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(write_list)




            
        

