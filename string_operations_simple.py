def short_words(words):
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)
    ans = []
    for word in words:
        if len(word) == min_len:
            ans.append(word)
    return ' '.join(ans)


def rle(string):
    def add_repeat(string_cnt, cnt):
        if cnt > 1:
            return string_cnt + str(cnt)
        return string_cnt
    lastsym = string[0]
    lastpos = 0
    answer = []
    for i in range(len(string)):
        if string[i] != lastsym:
            answer.append(add_repeat(lastsym, i - lastpos))
            lastpos = i
            lastsym = string[i]
    answer.append(add_repeat(string[lastpos], len(string) - lastpos))
    return ''.join(answer)


def word_without_one_letter(dictionary, text):
    dict_words = set(dictionary)
    for word in dictionary:
        for letter_pos in range(len(word)):
            dict_words.add(word[:letter_pos] + word[letter_pos+1:])
    print(dict_words)
    ans = []
    for word in text:
        ans.append(word in dict_words)
    return ans

def gistogram_of_char(str):
    dict_for_letters = {}
    max_symbol_rate = 0
    for symbol in str:
        if symbol not in dict_for_letters:
            dict_for_letters[symbol] = 0
        dict_for_letters[symbol] += 1
        max_symbol_rate = max(max_symbol_rate, dict_for_letters[symbol])
    dict_for_letters_sort = sorted(dict_for_letters.keys())
    for i in range(max_symbol_rate, 0, -1):
        for symbol in dict_for_letters_sort:
            if dict_for_letters[symbol] >= i:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(dict_for_letters_sort))
