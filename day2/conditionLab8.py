import random
oper_num = random.randint(1, 10)

if oper_num == 1 or 6:
    sum =300 + 50
elif oper_num == 2 or 7:
    sum = 300 - 50
elif oper_num == 3 or 8:
    sum = 300 * 50
elif oper_num == 4 or 9:
    sum = 300 / 50
else:
    sum = 300 % 50

print('결과값 : ', sum)