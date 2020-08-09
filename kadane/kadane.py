def kadane(arr):
    if all(i<=0 for i in arr):
        return max(arr)
    Max = 0
    cur_max = 0
    for i in arr:
        cur_max += i
        if cur_max<0:
            cur_max = 0
        if Max<cur_max:
            Max = cur_max
    return Max

print(kadane([-2, -3, 5, 6, -1, -2, 100, 1, 2, -3, -4, 1]))
print(kadane([-2, -3, -1, 0]))
print(kadane([-2, -3, -1]))
print(kadane([2, 3, 1, 1, 4, 2]))
