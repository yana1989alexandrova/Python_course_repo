import random
arr = [random.randint(1,15) for _ in range(10)]
arr2 = [random.randint(1,15) for _ in range(10)]
print(arr,arr2)
res_arr = []
for num in arr:
    if num in arr2:
        res_arr.append(num)
res_arr.sort()
result = set(res_arr)
print(result)