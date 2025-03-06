# Here is the importation script with mongoimport executed in the terminal
#C:\Users\sedjr>mongoimport --db Students --collection collection_student --file student.json --jsonArray
#C:\Users\sedjr>mongoimport --db Students --collection collection_course --file course.json --jsonArray
#C:\Users\sedjr>mongoimport --db Students --collection collection_professor --file professor.json --jsonArray

import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://romulusakonakpo:210602@cluster0.jb9ihtp.mongodb.net/")
db = client.Students
collection_student = db['student']
collection_professor = db['professor']
collection_course = db['course']

data_student = list(collection_student.find())
data_professor = list(collection_professor.find())
data_course = list(collection_course.find())

#for document in data_student:
    #print(document)

# 1. Find Master’s students:
master_students = list(collection_student.find({"stu_current_level": "Master"}))
print(f"The master's students are : {master_students}")

# 2. Find the student with ID 55:
student = collection_student.find_one({"id_student": "55"})
print(f"The student with ID 55 is : {student}")

# 3. Search for a student by first name
search = {'stu_first_name': 'Blanc'}
result = collection_student.find_one(search)
print(f"The desired student is: {result}")

# 4. Insert a new student
new_student = {
    'id_student' : 63, 
    'stu_name': 'Chifu', 
    'stu_first_name': 'Adrian' , 
    'stu_date_birth': '1987-01-01', 
    'stu_adress_resid': "12 Rue Protis, 13007 Marseille", 
    'stu_univ_mail': 'adrian.chifu@etu.univ-amu.fr',
    'stu_phone_num' : '05 45 85 75 96', 
    'stu_gender': 'M', 
    'stu_nationality': 'France', 
    'stu_current_level': 'Post doctorat',
    }
result = collection_student.insert_one(new_student)
print(f"The new student inserted is : {result}")

# 5. Determine the name and age of students born after 2000
after_2000_filter = {"stu_date_birth": {"$gte": "2000-01-01"}}  

filtered_students = collection_student.find(after_2000_filter)

def calculate_age(birth_date_str):
    from datetime import date

    birth_date = date.fromisoformat(birth_date_str)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
for student in filtered_students:
    name = f"{student['stu_name']} {student['stu_first_name']}"
    birth_date = student["stu_date_birth"]
    age = calculate_age(birth_date)  
    print(f"Name: {name}, Age: {age}")


