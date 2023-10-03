import random
arr = [random.randint(1,5) for _ in range(10)]
print(arr)
arr.append(arr[0])
sum_ = []
for  idx, bush in enumerate(arr):
    if idx < (len(arr) - 1):
        print(idx,len(arr))
        sum_.append(arr[idx-1] + arr[idx] + arr[idx+1])

print(sum_, max(sum_), arr)