#가변형인자(인수)

def sumEven1(*p):
    ans=0
    for data in p:
        if data%2==0:
            ans+= data
        else:
            ans = 0
    if len(p)==0:
        ans=-1
    return ans

print(sumEven1(1,2,3,4))
print(sumEven1())
print(sumEven1(100))
print(sumEven1(3,5,7))

