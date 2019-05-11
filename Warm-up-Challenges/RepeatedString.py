def repeatedString(s, n):
    s_len = len(s)
    if n <= s_len:
        return s[:n].count('a')
    remainder = n % s_len
    quotient = n // s_len
    if remainder != 0:
        return ((s.count('a') * quotient) + s[:remainder].count('a'))
    else:
        return (s.count('a') * quotient)