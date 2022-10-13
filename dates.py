def code_of_month(month_number):
    if month_number == 1 or month_number == 10:
        return 1
    elif month_number == 5:
        return 2
    elif month_number == 8:
        return 3
    elif month_number == 2 or month_number == 3 or month_number == 11:
        return 4
    elif month_number == 6:
        return 5
    elif month_number == 12 or month_number == 9:
        return 6
    elif month_number == 7 or 4:
        return 0
    else:
        return None


def code_of_year(year_number):
    if (year_number / 100 == 19):
        result = (0 + (year_number % 100) + int((year_number % 100) / 4))
    else:
        result = (6 + (year_number % 100) + int((year_number % 100) / 4))
    return result % 7


def day_of_week(day, month_code, year_code):
    result = (day + month_code + year_code - 1) % 7
    if result == 0:
        result = 7
    return result


def output(data, result):
    tmp = data[0] - result + 1
    str_res = str(tmp) + "-"
    if (data[1] < 10):
        str_res += "0"
        str_res += str(data[1])
        str_res += "-"
    else:
        str_res += str(data[1])
        str_res += "-"
    str_res += str(data[2])
    return str_res


data = input().split('-')
data_str = data
for i in range(3):
    data[i] = int(data[i])
result = day_of_week(data[0], code_of_month(data[1]), code_of_year(data[2]))
print(output(data, result))