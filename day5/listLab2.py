listnum = [10,5,7,21,4,8,18]

min_num = listnum[0]
for i in range(1, len(listnum)):
    num= listnum[i]
    if min_num > num:
        min_num = num
    # else:
    #     continue

print('최솟값 : %d' %(min_num))