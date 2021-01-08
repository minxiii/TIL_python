listnum = [10,5,7,21,4,8,18]

max_num = listnum[0]
min_num = listnum[0]

for i in range(1, len(listnum)):
    num= listnum[i]
    if max_num < num:
        max_num = num
    elif min_num > num:
        min_num = num

print('최솟값 : %d, 최댓값 : %d' %(max_num,min_num))