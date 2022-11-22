from math import gcd


def add_frac(frac1, frac2):  # frac1 + frac2
    if frac1[1] == 0 or frac2[1] == 0:
        raise ValueError("The denominator cannot be zero.")
    d = frac1[1] * frac2[1]
    n = frac1[0] * frac2[1] + frac2[0] * frac1[1]

    nwd = gcd(n, d)
    n_reduced = int(n / nwd)
    d_reduced = int(d / nwd)
    if d_reduced < 0:
        d_reduced = abs(d_reduced)
        n_reduced = 0 - n_reduced
    return [n_reduced, d_reduced]


def sub_frac(frac1, frac2):  # frac1 - frac2
    if frac1[1] == 0 or frac2[1] == 0:
        raise ValueError("The denominator cannot be zero.")
    d = frac1[1] * frac2[1]
    n = frac1[0] * frac2[1] - frac2[0] * frac1[1]

    nwd = gcd(n, d)
    n_reduced = int(n / nwd)
    d_reduced = int(d / nwd)
    if d_reduced < 0:
        d_reduced = abs(d_reduced)
        n_reduced = 0 - n_reduced
    return [n_reduced, d_reduced]


def mul_frac(frac1, frac2):  # frac1 * frac2
    if frac1[1] == 0 or frac2[1] == 0:
        raise ValueError("The denominator cannot be zero.")
    n = frac1[0] * frac2[0]
    d = frac1[1] * frac2[1]
    nwd = gcd(n, d)
    n = int(n / nwd)
    d = int(d / nwd)
    if d < 0:
        d = abs(d)
        n = 0 - n
    return [n, d]


def div_frac(frac1, frac2):  # frac1 / frac2
    if frac1[1] == 0 or frac2[1] == 0:
        raise ValueError("The denominator cannot be zero.")
    frac2[0], frac2[1] = frac2[1], frac2[0]
    n = frac1[0] * frac2[0]
    d = frac1[1] * frac2[1]
    nwd = gcd(n, d)
    n = int(n / nwd)
    d = int(d / nwd)
    if d < 0:
        d = abs(d)
        n = 0 - n
    return [n, d]


def is_positive(frac):  # bool, czy dodatni
    if frac[1] == 0:
        raise ValueError("The denominator cannot be zero.")
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac):  # bool, typu [0, x]
    if frac[1] == 0:
        raise ValueError("The denominator cannot be zero.")
    return frac[0] == 0


def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    if frac1[1] == 0 or frac2[1] == 0:
        raise ValueError("The denominator cannot be zero.")

    n1, n2 = frac1[0] * frac2[1], frac2[0] * frac1[1]
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        return 0


def frac2float(frac):  # konwersja do float
    if frac[1] == 0:
        raise ValueError("The denominator cannot be zero.")
    return float(frac[0] / frac[1])
