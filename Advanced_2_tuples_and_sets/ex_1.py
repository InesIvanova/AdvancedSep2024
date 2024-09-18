nums = tuple([float(el) for el in input().split()])
occ = {}

for num in nums:
    occ[num] = nums.count(num)

for key, value in occ.items():
    print(f"{key:.1f} - {value} times")