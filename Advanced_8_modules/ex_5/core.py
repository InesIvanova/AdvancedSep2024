def create_sequence(n):
    first_num = 0
    second_num = 1

    seq = [first_num, second_num]

    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq


def locate_index_of_number(seq, number_to_locate):
    return seq.index(number_to_locate)