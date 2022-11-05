import statistics


def main():
    x = list(map(str, input("Enter multiple values: ").split()))
    global m
    re = change(x)
    m = the_mean(re)
    mod = the_mode(re)
    median = the_median(re)
    range1 = the_range(re)
    stan = standard_den(re)
    print(f"The mean is: {m}")
    print(f"The median is: {median}")
    print(f"The mode is: {mod}")
    print(f"The range is: {range1}")
    print(f"The Standard deviation is: {stan}")


def change(n):
    m = "".join(n)
    if "." in m:
        x = list(map(float, n))
    else:
        x = list(map(int, n))
    return x


def the_mean(n):
    s = sum(n)
    mean = s / len(n)
    return mean


def the_mode(n):
    newlist = []
    duplist = {}
    for i in n:
        if i not in duplist:
            duplist[i] = 1
        else:
            duplist[i] += 1
    for key, values in duplist.items():
        if values > 1:
            newlist.append(key)

    if newlist == []:
        return None
    else:
        return newlist


def the_median(n_num):
    n = len(n_num)
    n_num.sort()

    if n % 2 == 0:
        median1 = n_num[n // 2]
        median2 = n_num[n // 2 - 1]
        median = round((median1 + median2) / 2, 2)
        return median
    else:
        median = n_num[n // 2]
        return median


def the_range(n):
    n.sort()
    return n[-1] - n[0]


def standard_den(n):
    return round((statistics.stdev(n, xbar=m)), 2)


main()
