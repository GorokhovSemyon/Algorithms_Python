def find_max1_max2(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return max1, max2


def find_max_last(seq):
    answer = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > answer:
            answer = seq[i]
    return answer
