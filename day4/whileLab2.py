#1부터 6사이 난수 2개를 추출
#추출된 2개의 숫자가 서로 다르면 값의 크기를 비교하여 대소관계 비교하여 출력
#추출된 숫자가 동일하면 '게임 끝'이라는 메세지 출력

import random

while True:
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)
    # print(pairNum1, pairNum2)

    if pairNum1 == pairNum2:
        print('게임 끝')
        break
    elif pairNum1 > pairNum2:
        print('pairNum1이 pairNum2보다 크다')
    else:
        print('pairNum1이 pairNum2보다 작다')
