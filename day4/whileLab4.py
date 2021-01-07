#사용자로부터 월에 해당하는 숫자를 입력받는다
#입력된 숫자가 1~12면: 각 월에 맞는 계절을 'x월은 xx'이렇게 출력
#입력된 숫자가 1~12아니면 : '1~12사이의 입력하세요'출력

while True:
    month = int(input('월을 입력하세요'))
    if 3<= month <= 5 :
        print(month,'월은 봄', sep='')
    elif 6<= month <= 8 :
        print(month,'월은 여름', sep='')
    elif 9<= month <=11:
        print(month, '월은 가을', sep='')
    elif month == 1 or month ==2 or month== 12:
        print(month,'월은 겨울', sep='')
    else :
        break
print('1~12숫자를 입력하세요')