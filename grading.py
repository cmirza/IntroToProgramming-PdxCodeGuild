#Takes a percentage and figures out corresponding letter grade

input_grade = input("What percentage did you get:")
grade = int(input_grade)

if grade > 100:
    print("I don't think so...\n")
elif grade >= 90:
    print("You got an A!\n")
elif grade >= 80:
    print("You got an B!\n")
elif grade >= 70:
    print("You got an C!\n")
elif grade >= 60:
    print("You got an D!\n")
elif grade >= 0:
    print("You got an F!\n")
elif grade < 0:
    print("I don't think so...\n")
