# import sets_simple
# import special_tasks
# import finding_simple
# import finding_simple
# import finding_simple
# import special_tasks
# import simple_matrix
# import string_operations_simple
# import string_operations_simple
# import string_operations_simple
# import maxs_simple
# import different_sorts

if __name__ == '__main__':
    # array = []
    # array_str = []
    # dict_simple = {}
    # set_poisk = set()
    # set_poisk.add(input())

    # n = int(input())
    # m = int(input())

    # double_array = simple_matrix.input_of_2d_matrix(n, 2)

    # for j in range(n):
    #     array.append(int(input()))
    # print(array)

    # for k in range(n):
    #     array_str.append(input())
    # print(array_str)

    # for i in range(n):
    #     dict_simple[input()] = i

    # print(special_tasks.chess_rook_beat_counter(double_array))

    class MyList(list):
        def append(self, elem):
            if (type(elem) == type(1) or type(elem) == type(1.1)):
                self.extend([elem])

            


    test = MyList()
    print(type(1))
    print(type(1.1))
    test.append([1,2,3])
    print(test)
