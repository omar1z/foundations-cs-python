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
            "Major": "Business",
            "GPA": 3.9
        }
    ]
student_data1 = [
        {
            "ID": 1,
            "Name": "Anas",
            "Age": 30,
            "Major": "Bio Science",
            "GPA": 2.7
        },
        {
            "ID": 2,
            "Name": "Omar",
            "Age": 22,
            "Major": "Business",
            "GPA": 4
        },
        {
            "ID": 3,
            "Name": "jad",
            "Age": 18,
            "Major": "Computer Science",
            "GPA": 2
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
        addSt(student_data, name, age, major, gpa)
    elif choice == 5:
        print(findCommon(student_data, student_data1))
    else:
        exit()

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
    dictionary = {"ID": len(st_data)+1, "name": name, "age": age, "Major": major, "GPA": gpa}
    return st_data.append(dictionary)


def findCommon(st1, st2):
    d1 = []
    d2 = []
    for i in st1:
        d1.append(i["Major"])
    for j in st2:
        for k in d1:
            if k == j["Major"]:
                d2.append(j["Major"])
    return d2


while True:
    main()
