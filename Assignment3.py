#ASSIGNMENT3
# user's name
print("HELLO MY FRIEND :)")
username = input("Please enter your name :")
print("Welcome dear _", username, "_")


def main():
    #MENU
    print()
    print("1.Add Matrices")
    print("2.Check Rotation")
    print("3.Invert Dictionary")
    print("4.Convert Matrix to Dictionary")
    print("5.Check Palindrome")
    print("6.Search for an Element & Merge Sort")
    print("7.EXIT")
    print()

    menu_nb = int(input("Enter your choice please :"))
    while menu_nb > 7:
        menu_nb = int(input("Enter a valid choice please :"))

    if menu_nb == 1:
        addMatrices()
    elif menu_nb == 2:
        print(checkRotation())
    elif menu_nb == 3:
        print(invertDictionary())
    elif menu_nb == 4:
        print(matrixToDic())
    elif menu_nb == 5:
        s = input("Enter a string to check it if it's palindrome :")
        print(checkPalindrome(s, 0, -1))
    elif menu_nb == 6:
        element_list = [3,6,1,9,4,0,2,7,2]
        elem = int(input("Check if the number you are thinking about is in this list :) :"))
        print(searchAm(element_list, elem))
    elif menu_nb == 7:
        exit()

def addMatrices():
    i,j = 0,0
    m1 = []
    m2 = []
    rows = int(input("Enter number of rows :"))
    cols = int(input("Enter number of columns :"))
    for i in range(rows):
        print("row", i+1)
        a = []
        for j in range(cols):
            a.append(eval(input("Enter one element of the row of matrix1:")))
        m1.append(a)
    for i in range(rows):
        print("row", i+1)
        b = []
        for j in range(cols):
            b.append(eval(input("Enter one element of the row of matrix2:")))
        m2.append(b)
    print()
    print(m1, "+", m2, "= ", end="")
    m3 = []
    for i in range(rows):
        c = []
        for j in range(cols):
            c.append(m1[i][j] + m2[i][j])
        m3.append(c)
    print(m3)


def checkRotation():
    m1 = []
    m2 = []
    rows1 = int(input("Enter number of rows:"))
    cols1 = int(input("Enter number of columns:"))

    # Input for the first matrix
    for i in range(rows1):
        print("Row", i + 1)
        a = []
        for j in range(cols1):
            a.append(eval(input("Enter one element of the row of matrix1:")))
        m1.append(a)

    # Create the second matrix with swapped rows and columns
    rows2 = cols1
    cols2 = rows1
    for i in range(rows2):
        print("Row", i + 1)
        b = []
        for j in range(cols2):
            b.append(eval(input("Enter one element of the row of matrix2:")))
        m2.append(b)

    print(m1, " =? ", m2)
    c = 0
    for i in range(rows1):
        for j in range(cols1):
            if m1[i][j] == m2[j][i]:
                c += 1

    if c == rows1 * cols1:
        return "MATRIX X IS A ROTATION OF MATRIX Y!"
    else:
        return "MATRIX X IS NOT A ROTATION OF MATRIX Y!"



def invertDictionary():
    list1 = []
    d_key = int(input("Enter a key or -1 to stop: "))
    d = {}

    while d_key != -1:
        while d_key in list1:
            print("***Key already exists***")
            d_key = int(input("Enter a key or -1 to stop: "))
        dic_value = input("Enter values to fill the dictionary: ")
        list1.append(d_key)
        d[d_key] = dic_value
        d_key = int(input("Enter a key or -1 to stop: "))

    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key

    return inverted_dict


def matrixToDic():
    rows = int(input("Enter how many user you want to enter their data :"))
    m = []
    id_list = []
    for i in range(rows):
        a = []
        print("for user", i+1)
        f_name = input("Enter first name for user :")
        l_name = input("Enter last name for user :")
        idd = int(input("Enter ID for user :"))
        while idd in id_list:
            idd = int(input("***Enter a different ID for user*** :"))
        id_list.append(idd)
        job_t = input("Enter job title for user :")
        company = input("Enter the company of the user :")
        a.append(f_name)
        a.append(l_name)
        a.append(idd)
        a.append(job_t)
        a.append(company)
        m.append(a)
    print()
    print("Input :")
    print(m)
    dictionary = {}
    f = ""
    for i in range(rows):
        user_details = []
        for j in range(5):
            if j != 2:
                user_details.append([m[i][j]])
            else:
                f = m[i][2]
        dictionary[f] = user_details
    print("Output :")
    return dictionary


def checkPalindrome(s, c, e):
    # s is the string
    # c is the starting point that is at index 0
    # e is -1 the last index
    # incrementing c and decrementing e
    mid = len(s)//2
    if s == "":
        print("You didn't enter a string")
    else:
        if s[c] == s[e] and c != mid:
            return checkPalindrome(s,c+1,e-1)
        elif c == mid:
            return "This string is a palindrome"
        else:
            return "This string is not palindrome"


def searchAm(lst, element):
    j = 0
    for i in range(len(lst)):
        if element == lst[i]:
            print(element, "was found in index :", i)
    print("list before sorting :",lst)
    print("The list sorted :")
    for i in range(len(lst)):
        mini = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[mini]:
                mini = j
        lst[i], lst[mini] = lst[mini], lst[i]
    return lst


while True:
    main()





























