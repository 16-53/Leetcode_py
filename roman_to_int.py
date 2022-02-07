def romantoint(s):
    d = {'CM': 900, 'M': 1000,  'CD': 400, 'D': 500,  'XC': 90, 'C': 100, 'XL': 40,
         'L': 50, 'IX': 9, 'X': 10, 'IV': 4, 'V': 5, 'I': 1}
    result = 0
    for i in d:
        while i in s:
            result += d[i]
            s = s.replace(i, '0', 1)
    return result
