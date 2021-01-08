listnum = [10,5,7,21,4,8,18]

max_num = listnum[0]
for i in range(1, len(listnum)):
    num= listnum[i]
    if max_num < num:
        max_num = num
    # else:
    #     continue

print('최댓값 : %d' %(max_num))