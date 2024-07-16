lst = [0]*(101)
lst[1] = 1
lst[2] = 1
lst[3] = 1
lst[4] = 2
lst[5] = 2
for i in range(6,101):
    lst[i] = lst[i-2]+lst[i-3]

n = int(input())
print(lst[n])