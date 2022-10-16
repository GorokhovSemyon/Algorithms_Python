def find_chet(seq):
    answer = -1
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < answer):
            answer = seq[i]
            flag = True
    return answer


def findx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans


def two_numbs_nearest_to_x(numbers, x):
    prev_number = set()
    for now_number in numbers:
        if x - now_number in prev_number:
            return now_number, x - now_number
        prev_number.add(now_number)
    return 0, 0


def is_equal_with_digit_swap(frst_num, sec_num):
    def digit_cnt(number):
        dig_cnt = [0] * 10
        while number > 0:
            tmp = number % 10
            dig_cnt[tmp] += 1
            number //= 10
        return dig_cnt
    digits_frst = digit_cnt(frst_num)
    digits_sec = digit_cnt(sec_num)
    for now_digit in range(10):
        if digits_frst[now_digit] != digits_sec[now_digit]:
            return False
        return True
