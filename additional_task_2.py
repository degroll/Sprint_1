def digit_root(num):
    if type(num) != int or num <= 0 or num > 10 ** 7:
        return None
    res = 0
    for n in str(num):
        res += int(n)
    if len(str(res)) > 1:
        return digit_root(res)
    return res


print(digit_root(123))