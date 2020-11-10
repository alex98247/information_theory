def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if not poly:
        poly.append(0)


def poly_divmod(num, den, F):
    #Create normalized copies of the args
    num = num[:]
    normalize(num)
    den = den[:]
    normalize(den)

    if len(num) >= len(den):
        #Shift den towards right so it's the same degree as num
        shiftlen = len(num) - len(den)
        den = [0] * shiftlen + den
    else:
        return [0], num

    quot = []
    divisor = den[-1]
    for i in range(shiftlen + 1):
        #Get the next coefficient of the quotient.
        mult = (F.mul([num[-1]], F.inv([divisor]))[:1] or [0])[0] #num[-1] / divisor
        quot = [mult] + quot

        #Subtract mult * den from num, but don't bother if mult == 0
        #Note that when i==0, mult!=0; so quot is automatically normalized.
        if mult != 0:
            d = [mult * u for u in den]
            d = list(map(lambda x: x%F.p**F.n, d))
            num = [(F.add([u], [-v])[:1] or [0])[0] for u, v in zip(num, d)]

        num.pop()
        den.pop(0)

    normalize(num)
    return quot, num
