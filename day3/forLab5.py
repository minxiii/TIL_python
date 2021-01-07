#3의 배수, 5의배수는 제외
sum=0

# for i in range(1,51):
#     if i%3==0 :
#         if not i%5==0:
#             sum+=i

for i in range(1,51):
    if i%3==0 and i%5 !=0:
        sum+=i

print(sum)
