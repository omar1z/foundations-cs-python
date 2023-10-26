#ASSIGNMENT3
def main():
    # user's name
    print("HELLO MY FRIEND :)")
    username = input("Please enter your name :")
    print("Welcome dear _", username, "_")

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

    menu_Nb = int(input("Enter your choice please :"))

    if menu_Nb == 1:
        addMatrices()
    elif menu_Nb == 2:
        print(checkRotation())

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


main()





























