def flood_function(hight):
    maxpos = 0
    for i in range(len(hight)):
        if hight[i] > hight[maxpos]:
            maxpos = i
    answer = 0
    nowmax = 0
    for i in range(maxpos):
        if hight[i] > nowmax:
            nowmax = hight[i]
        answer += nowmax - hight[i]
    nowmax = 0
    for i in range(len(hight) - 1, maxpos, -1):
        if hight[i] > nowmax:
            nowmax = hight[i]
        answer += nowmax - hight[i]
    return answer


def chess_rook_beat_counter(cords):
    def add_new_rook(rowsorcols, key):
        if key not in rowsorcols:
            rowsorcols[key] = 0
        rowsorcols[key] += 1
    def number_of_pairs(rowsorcols):
        pairs = 0
        for key in rowsorcols:
            pairs += rowsorcols[key] - 1
        return pairs
    rooksinrow = {}
    rooksincol = {}
    for rows, cols in cords:
        add_new_rook(rooksinrow, rows)
        add_new_rook(rooksincol, cols)
    return number_of_pairs(rooksincol) + number_of_pairs(rooksinrow)
