def boarding_passengers(ship_capacity, *passenger_list):

    program_data = {}
    total_to_board = sum([passenger_group_info[0] for passenger_group_info in passenger_list])

    for passenger_group_info in passenger_list:
        count, group_name = passenger_group_info

        if ship_capacity == 0:
            break

        if count <= ship_capacity:
            if group_name not in program_data:
                program_data[group_name] = 0
            program_data[group_name] += count
            ship_capacity -= count

    total_onboarded = 0
    sorted_data = sorted(program_data.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = "Boarding details by benefit plan:\n"
    for group_name, count in sorted_data:
        result += f"## {group_name}: {count} guests\n"
        total_onboarded += count

    unboarded_guests = total_to_board - total_onboarded

    if unboarded_guests <= 0:
        result += f"All passengers are successfully boarded!"

    if ship_capacity == 0 and unboarded_guests > 0:
        result += f"Boarding unsuccessful. Cruise ship at full capacity."


    if ship_capacity != 0 and unboarded_guests > 0:
        result += f"Partial boarding completed. Available capacity: {ship_capacity}."

    return result

