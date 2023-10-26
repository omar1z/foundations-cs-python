#ASSIGNMENT3
#user's name
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

    menuNb = int(input("Enter your choice please :"))

    if menuNb == 1:
        addMatrices()

def addMatrices():
    k,i,j,x,y = 0,0,0,0,0
    m1 = []
    m2 = []
    rows = int(input("Enter number of rows :"))
    cols = int(input("Enter number of columns :"))
    for i in range(rows):
        a = []
        for j in range(cols):
            a.append(eval(input("Enter elements of the row of matrix1:")))
        m1.append(a)
    for i in range(rows):
        b = []
        for j in range(cols):
            b.append(eval(input("Enter elements of the row of matrix2:")))
        m2.append(b)

    print(m1, "+", m2, "=")


main()





























