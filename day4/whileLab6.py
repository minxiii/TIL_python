#절대값 : abs()
result=1
while True:
    num = int(input('숫자를 입력하세요'))
    if num == 0:
        print('종료')
        break
    elif -10> num or num >10:
        continue
    elif num < 0 :
        print('입력값(부호변경): %d' % abs(num))
        for i in range(1,abs(num)+1):
            result= result * i
        print(result)
    else:
        print('입력값: %d' % num)
        for i in range(1, num + 1):
            result = result * i
        print(result)

