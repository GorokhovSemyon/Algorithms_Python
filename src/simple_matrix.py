def input_of_2d_matrix(n, m):
    arr_2d = []
    for i in range(n):
        internal_arr = []
        for j in range(m):
            internal_arr.append(input())
        arr_2d.append(internal_arr)
    return arr_2d
