# FSW (Simulating Student API Endpoints)
student_data = [
        {
            "ID": 1,
            "Name": "Alice",
            "Age": 20,
            "Major": "Computer Science",
            "GPA": 3.7
        },
        {
            "ID": 2,
            "Name": "Bob",
            "Age": 21,
            "Major": "Engineering",
            "GPA": 3.9
        }
    ]
def main():


    print("1. Get Student by ID")
    print("2. Get All Students")
    print("3. Get Students by Major")
    print("4. Add Student")
    print("5. Find Common Majors")
    print("6. Delete Student")
    print("7. Calculate Average GPA")
    print("8. Get Top Performers")
    print("9. EXIT")

    print()
    choice = int(input("Enter your choice please : "))
    while choice > 9:
        choice = int(input("Enter a valid choice please :"))

    if choice == 1:
        gbi = eval(input("Enter student ID to get all his Info :"))
        print(getById(student_data,gbi))
    elif choice == 2:
        print(getAstud(student_data))
    elif choice == 3:
        gbm = input("Enter a major to get all students of it :")
        print(getByMaj(student_data,gbm))
    elif choice == 4:
        name = input("Enter student name :")
        age = input("Enter student age :")
        major = input("Enter student major :")
        gpa = input("Enter student gpa :")
        student_data.append(addSt(student_data, name, age, major, gpa))
        

def getById(st_data, st_id):
    for i in st_data:
        if i["ID"] == st_id:
            return i


def getAstud(st_data):
    for i in st_data:
        print(i)
    return ":)"


def getByMaj(st_data, st_maj):
    for i in st_data:
        if i["Major"] == st_maj:
            print(i["Name"])
    return ":)"


def addSt(st_data, name, age, major, gpa):
    dictionary = {"ID": len(st_data)+1, "name": name, "age": age, "major": major, "GPA": gpa}
    return dictionary

while True:
    main()
