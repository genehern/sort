# Purpose of project
1. 1. The project can be used to allocate students from each class into a selected course based on their choice (rankings).
   2. Their choices are collated via google forms, which in turns gives us a google sheets
   3.  Allocations is based on first come first serve basis as each course can only accomodate up to 30 students.
   4.  This programme is extremely practical. It can also be used in other scenarios such as allocating students to their desried Co-Curiicular Activites

# Programming logic
2. 1. Create an object "student", which containts important information such as his name, class, and selected choices.
   2. It also contains built in function to allocate that particular student to his/her desired course based on availability.
   3. Some students sent in multiple responses via the google forms to update their responses
   4. Thus, a dictionary called "duplicate" is called. This will ensure that our object list (list of responses) only contains the latest responses. This is done via inputing their email addresses as "keys" in the dict, as repeated responses will be sent via the same email address.
   5. List of students (stdl) is created by taking in values from object list (objl)
   6. 2 csv files will be created. Students will be grouped by their allocated courses in 1 file, while in the other file, they will be grouped by their original classes
   7. In the terminal, the number of students will be printed. This can be used to check if the programme is working.

# How to use the programme
3. 1. Download the google sheets as a csv file
   2. Name the csv file as "data.csv"
   3. Follow the commands in the terminal.
   4. In line 3, update the number of choices given to the students
   5. In line 8, update the key in the dictionary to the same wordings in the google sheets (how the students express their choices)
   6. In line 9, update the key in the dictionary to the same wordings in the google sheets (how the students express their class)
   7. In lines 15 and 18, update the number of choices given to students
   8. In line 40 make sure that the values taken in correspond to the csv. If not, update the order.
   9. Run the programme!


      
  
  
