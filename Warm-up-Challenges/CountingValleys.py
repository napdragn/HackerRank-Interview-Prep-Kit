def countingValleys(n, s):
    if n == 1:
        return 0
    valley_count = 0
    sum = 1 if s[0] == 'U' else -1
    for i in range(1, n):
        if sum == 0 and s[i - 1] == 'U':
            valley_count += 1
        if s[i] == 'U':
            sum += 1
        elif s[i] == 'D':
            sum -= 1
    return (valley_count + 1) if sum == 0 and s[n - 1] == 'U' else valley_count
