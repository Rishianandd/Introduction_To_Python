grade = float(input("Grade: /20 "))
if grade < 0 or grade > 20:
    print("Invalid Grade")
elif grade >= 16:
    print("Very good")
elif grade >= 14:
    print("Fairly good")
elif grade >= 12:
    print("Good")
elif grade >= 8:
    print("Pass")
else:
    print("Fail")