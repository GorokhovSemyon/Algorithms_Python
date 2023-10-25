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
# --------------------------------------------------------------
# Декоратор расчёта времени выполнения функции
# import time
#     def time_decorator(func):
#         def wrapper(*args, **kwargs):
#             before = time.time()
#             value = func(*args, **kwargs)
#             print(round(time.time() - before))
#             return value
#
#         return wrapper
# --------------------------------------------------------------
# Декоратор логов
# import datetime
# from inspect import getcallargs
#
#
# def logging_decorator(__list):
#     def decorator(f):
#         def wrapper(*args, **kwargs):
#             time = datetime.datetime.now()
#             res = f(*args, **kwargs)
#             __list.append({"name": f.__name__,
#                            "arguments": getcallargs(f, *args, **kwargs),
#                            "call_time": time,
#                            "result": res})
#             return res
#
#         return wrapper
#
#     return decorator
#
#
# logger = []  # этот словарь будет хранить наш "лог"
#
#
# @logging_decorator(logger)  # в аргументы фабрики
# def test_simple(a, b=3):
#     return 127
#
#
# test_simple(21)
#
# print(logger)
# --------------------------------------------------------------
# Задание на сетевое взяимодействие
# import requests
# import json
# import pickle
#
# stat = []
# response = requests.get("https://jsonplaceholder.typicode.com/users")
# users = [*response.json()]
# for prsn in users:
#     stat.append({"id": prsn["id"], "username": prsn["username"], "email": prsn["email"], "posts": 0, "comments": 0})
# stat = sorted(stat, key = lambda x: x["id"])
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# posts = [*response.json()]
# for el in posts:
#     stat[int(el['userId'])-1]["posts"] += 1
# response = requests.get("https://jsonplaceholder.typicode.com/comments")
# cmnts = [*response.json()]
# for i in cmnts:
#     for j in stat:
#         if j["email"] == i["email"]:
#             j["comments"] += 1
# response = requests.post("https://webhook.site/ba77f608-3cce-40f5-b8f1-794217e3518e", #адрес тут переменный
#                          data=json.dumps({"statistics": stat}))
# with open("solution.pickle", 'wb') as f:
#     pickle.dump(response, f)