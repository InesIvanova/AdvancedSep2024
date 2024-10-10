from collections import deque

packages = [int(el) for el in input().split()]
couriers = deque([int(el) for el in input().split()])

total_delivered_weight = 0

while packages and couriers:
    current_package = packages[-1]
    current_courier = couriers[0]

    if current_courier >= current_package:
        capacity = current_courier - current_package * 2
        couriers.popleft()
        if capacity > 0:
            couriers.append(capacity)
        total_delivered_weight += packages.pop()
    else:
        packages[-1] -= couriers.popleft()
        total_delivered_weight += current_courier

print(f"Total weight: {total_delivered_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join([str(el) for el in packages])}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join([str(el) for el in couriers])} but there are no more packages to deliver.")