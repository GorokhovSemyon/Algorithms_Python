# Словарь заполняется с входящего потока, разделители - пробелы, тип "ключ" - True
# print(dict.fromkeys(input().split(), True))
# --------------------------------------------------------------
# Заполнение словаря значениями unicod посимвольно
# def str_to_unicode(string):
    #     res = []
    #     for letter in string:
    #         res.append(str(ord(letter)))
    #     return int("".join(res))

    # inp = input().split()
    # d = {}
    # for key in inp:
    #     if key not in d:
    #         d[key] = str_to_unicode(key)
    # print(d)
# --------------------------------------------------------------
# Каждому символу в словаре его юникодовский эквивалент
# inp = input().split()
#     d = dict.fromkeys(inp, 0)
#     for key in d:
#         d[key] = ord(key)
#     print(d)
# --------------------------------------------------------------
# Поиск наиболее встречающихся 3 слов в тексте
# text = input()
#     lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')']  # и т.д.
#     lst = []
#
#     for word in text.lower().split():
#         if not word in lst_no:
#             _word = word
#             if word[-1] in lst_no:
#                 _word = _word[:-1]
#             if word[0] in lst_no:
#                 _word = _word[1:]
#             lst.append(_word)
#
#     _dict = dict()
#     for word in lst:
#         _dict[word] = _dict.get(word, 0) + 1
#
#     _list = []
#     for key, value in _dict.items():
#         _list.append((value, key))
#         _list.sort(reverse=True)
#
#     for freq, word in _list[0:3]:
#         print(f'{word}: {freq}', sep='')
#
#     _dict = {(i, lst.count(i)) for i in lst}
#     _list = []
#
#     for word, kol in _dict:
#         _list.append((kol, word))
#         _list.sort(reverse=True)
# --------------------------------------------------------------
# Классическая задача с собеса (что выведет?)
# a = [[]] * 3
#     print(a)
#
#     a[2].append(3)
#     print(a)