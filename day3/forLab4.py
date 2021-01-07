evenNUM, oddNum =0,0

for i in range(1, 101):
    if i%2==0:
        evenNUM +=i
    else:
        oddNum +=i

print('1부터 100까지의 숫자들 중에서')
print('짝수의 합은 %d이고' %evenNUM)
print('홀수의 합은 %d이다' %oddNum)