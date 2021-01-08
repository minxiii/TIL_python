import random
listnum = []

#난수10개 추출해서 추출된 순서대로 저장
for i in range(10):
    listnum.append(random.randint(1,50))
print(listnum)

#모든값 출력
for i in listnum:
    print(i)

#10보다 작은값 100으로 변경
for i in range(10): #for i in listnum하면 변경처리 안된다
    if listnum[i] <10:
        listnum[i] =100
print(listnum)
print('-'*20)

print(listnum[0])
print(listnum[-1])
print(listnum[1:6]) #2~6번째까지
print(listnum[::-1])
print(listnum[:])
del listnum[4] #5번째 삭제
print(listnum[:])
listnum[1:3] = [] #2~3번째 삭제
print(listnum[:])