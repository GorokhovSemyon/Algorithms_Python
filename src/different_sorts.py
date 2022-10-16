def sort_count(sequence):
    minimum_val = min(sequence)
    maximum_val = max(sequence)
    k = maximum_val - minimum_val + 1
    array_counter = [0] * k
    for now in sequence:
        array_counter[now - minimum_val] += 1
    now_position = 0
    for value in range(0, k):
        for i in range(array_counter[value]):
            sequence[now_position] = value + minimum_val
            now_position += 1
    return sequence
