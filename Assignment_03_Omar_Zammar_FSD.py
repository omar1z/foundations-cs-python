#FSD SIMULATING STUDENT DATA FRAME

data_frame = [
    {
        "Name": "Alice",
        "Age": 20,
        "Scores": (85, 92, 78)
    },
    {
        "Name": "Bob",
        "Age": 21,
        "Scores": (78, 89, 95)
    },
    {
        "Name": "Omar",
        "Age": 22,
        "Scores": (88, 74, 90)
    },
    {
        "Name": "Georgio",
        "Age": 23,
        "Scores": (77, 69, 82)
    },
    {
        "Name": "Fred",
        "Age": 23,
        "Scores": (93, 71, 100)
    }
]


def main():
    print("1.Get Average Score")
    print("2.Get Youngest Student")
    print("3.Get Highest Score")
    print("4.Add Student")
    print("5.Remove Student")
    print("6.Get Common Students")
    print("7.Find Students with consistent Improvement")
    print("8.EXIT")

    print()
    choice = int(input("Enter your choice please :) --> "))
    while choice > 8:
        choice = int(input("Enter a valid choice please :"))


while True:
    main()


















