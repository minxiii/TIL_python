import random
grade = random.randint(1, 6)

if grade == 1 or 2 or 3:
    print(grade,'학년은 저학년입니다')
elif grade == 4 or 5 or 6:
    print(grade,'학년은 고학년입니다')
