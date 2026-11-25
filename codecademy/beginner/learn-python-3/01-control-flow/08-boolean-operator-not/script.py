statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not 120 <= credits:
    print("You do not have enough credits to graduate.")

if not 2.0 <= gpa:
    print("Your GPA is not high enough to graduate.")

if not 120 <= credits and not 2.0 <= gpa:
    print("You do not meet either requirement to graduate!")
