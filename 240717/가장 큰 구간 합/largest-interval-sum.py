n,m = map(int,input().split())

lst = list(map(int,input().split()))
max_sum = 0
count = 1
for i in range(n-m+1):
    s_lst = lst[i:i+m]
    if max_sum == sum(s_lst):
        count = count+1
    elif max_sum<sum(s_lst):
        count = 1
        max_sum = sum(s_lst)

if max_sum == 0:
    print(0)

else :
    print(max_sum)
    print(count)