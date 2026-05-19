students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"

}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


for student in students:
    print(student)


for student in students:
    print(student, students[student])

for student in students:
    print(student, students[student], sep=", ")


#what if there was more information on the students
classmates = [

    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russell Terrier"},
    {"name" : "draco", "house" : "Slytherin", "patronus" : None}
]

for classmate in classmates:
    print(classmate["name"], classmate["house"], classmate["patronus"], sep=", ")