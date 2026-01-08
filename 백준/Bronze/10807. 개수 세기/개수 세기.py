n = int(input())
nums = list(map(int, input().split()))
v = int(input())
my_count = 0

for i in nums:
    if i == v:
        my_count += 1
print(my_count)