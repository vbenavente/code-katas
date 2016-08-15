def series_sum(n):
    if n == 0:
        return "%.2f" % n
    elif n == 1:
        return "%.2f" % n
    else:
        denom = 1
        num1 = 0
        num2 = 0
        for i in range(1, n):
            denom = denom + 3
            num1 = 1/denom
            total = 1 + num1 + num2
            num2 = num1
        return "%.2f" % total
