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