#실습1
#1부터 추출된 숫자값까지의 각 숫자들의 제곱값을 행단위로 출력한다
import random
num = random.randint(5,10)
#print('num :', num)

for i in range(1,num+1):
    print(i, '->', i**2)
    while i == num:
        break