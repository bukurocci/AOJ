m,n = list(map(int, input().split()))
p = (10 ** 9) + 7

def mpow(x, exp, mod):
    if(exp == 1):
        return m % mod

    if(exp % 2 == 1):
        return (x * mpow(x, exp - 1, mod)) % mod

    x = mpow(x, exp / 2, mod)

    return (x * x) % mod

print(mpow(m, n, p))