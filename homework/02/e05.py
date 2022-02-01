user_grade = -1

while user_grade < 0 or user_grade > 5:
    user_grade = int(input("What is your grade? 0-5: "))

match user_grade:
    
    case 0:
        print("Fail")
    case 1 | 2:
        print("Weak")
    case 3 | 4:
        print("Good")
    case 5:
        print("Excellent")