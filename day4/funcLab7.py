def differtwovalue(a,b):
    if a>=b:
        ans = a-b
    else:
        ans = b-a
    return ans

import random
for i in range(5):
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    result = differtwovalue(num1, num2)
    print('%d와 %d의 차는 %d입니다.' % (num1, num2, result))