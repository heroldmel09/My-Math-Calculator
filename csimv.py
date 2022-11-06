import math


def main():
    p = list(map(int, input("Enter a principal value:").split()))
    riy = list(map(str, input("Enter a interest Rate value:").split()))
    time = list(map(str, input("Enter a Time value:").split()))

    t = timecon(time)
    r = interest_rate_year(riy)
    i = interest(p, r, t)
    mf = maturity_value(p, i)
    print(f"The interest is:{i}")
    print(f"The Maturity Value is:{mf}")


def timecon(t):
    newlist = []
    for val in t:
        if "/" in val:
            n1 = val.split(":")
            n2 = [item.split("/") for item in n1]
            n = [item for l in n2 for item in l]
            for para, val2 in enumerate(n, start=1):
                if para == 1:
                    v1 = int(val2)
                elif para == 2:
                    v2 = int(val2)
                elif para == 3:
                    v3 = int(val2)
            frac_to_d = v2 / v3
            newlist.append(v1 + frac_to_d)
        elif "m" in val:
            n = val.replace("m", "")
            new_n = int(n) / 12
            newlist.append(new_n)
        elif "/" not in val:
            newlist.append(int(val))
    return newlist


def interest_rate_year(x):
    newlist = []
    for val in x:
        if "/" in val:
            n1 = val.split(":")
            n2 = [item.split("/") for item in n1]
            n = [item for l in n2 for item in l]
            for para, val2 in enumerate(n, start=1):
                if para == 1:
                    v1 = int(val2)
                elif para == 2:
                    v2 = int(val2)
                elif para == 3:
                    v3 = int(val2)
            enu = (v3 * v1) + v2
            n = enu / (v3 * 100)
            newlist.append(n)

        elif "." in val:
            n = round(float(val) / 100, 2)
            newlist.append(n)
        else:
            n = int(val) / 100
            newlist.append(n)

    return newlist


def interest(p, r, t):
    newlist = []
    for p, r, t in zip(p, r, t):
        n = round(p * r * t, 2)
        newlist.append(int(n))
    return newlist


def maturity_value(p, i):
    newlist = []
    for p, i in zip(p, i):
        n = round(p + i, 2)
        newlist.append(int(n))
    return newlist


main()
