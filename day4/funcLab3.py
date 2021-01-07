def expr(a,b,c):
    if c == '+':
        ans = a + b
    elif c== '-':
        ans =  a - b
    elif c== '*':
        ans =  a * b
    elif c== '/':
        ans = a / b
    else :
        ans = None
    return ans

s = '연산 결과 : '

result = expr(6,3,'+')
if result!= None:
    print(s,result)
else:
    print('수행불가')

result = expr(6,3,'-')
if result!= None:
    print(s,result)
else:
    print('수행불가')

result = expr(3,3,'a')
if result!= None:
    print(s,result)
else:
    print('수행불가')