nums = list(map(int, input().split()))

num_set = set(nums)
longest = 0

for n in num_set:
    if n - 1 not in num_set:
        current = n
        count = 1

        while current + 1 in num_set:
            current += 1
            count += 1

        longest = max(longest, count)

print(longest)