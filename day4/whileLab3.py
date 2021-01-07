#참고 : print(ood('A')), print(chr(65))
import random
count = 0

while True:
    num = random.randint(0,30)
    if num ==0 or 27<=num <=30:
        break
    else:
        count+=1
        print(chr(num+64), '(%d)' %num)

print('수행횟수는 %d번 입니다' %count)