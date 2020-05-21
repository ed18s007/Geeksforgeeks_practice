def sort012(arr,n):
    # code here
    cnt_zero, cnt_one, cnt_two = 0, 0, 0
    for i in range(n):
        if arr[i] == 0:
            cnt_zero += 1
        elif arr[i] == 1:
            cnt_one += 1
        elif arr[i] == 2:
            cnt_two += 1
    j = 0
    # print(cnt_zero, cnt_one, cnt_two)
    while cnt_zero > 0:
        arr[j] = 0
        j += 1
        cnt_zero -= 1
    while cnt_one > 0:
        arr[j] = 1
        j += 1
        cnt_one -= 1
    while cnt_two > 0:
        arr[j] = 2
        j += 1
        cnt_two -= 1
    # print(cnt_zero, cnt_one, cnt_two)
    return arr

arr = [0,1,2,0,1,2,0]#,1,2,0,1,2,0,1,2,]
print(sort012(arr, len(arr)))

import random
arr = [random.randint(0, 2) for p in range(0, 100)]
print(arr)
print(sort012(arr, len(arr)))
