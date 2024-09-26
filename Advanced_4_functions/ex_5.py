def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power-1)

# print(recursive_power(2, 4))

for el in [1, 2, 3]:
    print(el)


nums = [1, 2, 3]

index = 0
while True:
    if len(nums) >= index:
        break
    print(nums[index])
    index +=1