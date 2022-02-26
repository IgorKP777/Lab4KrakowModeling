import math
from prettytable import PrettyTable

table = PrettyTable()


def data(v):
    lambdaV = [4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 4.8, 5.0, 2.6, 5.3, 4.1, 2.2, 2.4, 2.5, 5.2,
               2.4, 5.1, 2.3]
    mu = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1]
    n = [3 for _ in range(24)]
    m = [2 for _ in range(24)]
    return lambdaV[v], mu[v], n[v], m[v]


def mmn0(lam, mu, n, m):
    s = n + 1
    bk = [m]
    for i in range(1, s):
        bk.append(m / i * bk[i - 1])
    p0 = 1 / sum(bk)
    pk = [p0]
    for i in range(1, s):
        pk.append(bk[i] * p0)
    pOtk = (m ** n) / math.factorial(n) * p0
    q = lam * (1 - pOtk)
    nPod = m * (1 - pOtk)
    tC = nPod / lam
    # print('-----Случай M/M/n/0-----')
    # print('p(отк) = ', round(pOtk, 3), sep='')
    # print('Q = ', round(q, 3), sep='')
    # print('n(с чертой) = ', round(nPod, 3), sep='')
    # print('kn = ', round((nPod / n) * 100, 3), sep='')
    # print('tc = ', round(tC, 3), sep='')
    table.add_row(['0', '', '', '', '', '', ''])
    # print('Сумма вероятностей ', round(sum(pk), 3), sep='')
    print()


def mmn8(lam, mu, n, m):
    sum = 0
    for i in range(1, n + 1):
        sum += (m ** i) / math.factorial(i)
    p0 = (1 + sum + (m ** (n + 1) / math.factorial(n) * (n - m))) ** -1
    pk = [p0]
    for i in range(1, n + 1):
        pk.append(((m ** i) / math.factorial(i)) * p0)
    sum = 0
    for i in range(n):
        sum += pk[i]
    nPod = m
    pOch = 1 - sum
    mPod = (m * pOch) / (n + 1 - m)
    NPod = mPod + nPod
    q = lam
    tOch = mPod / lam
    tc = NPod / lam
    # print('-----Случай M/M/n/8-----')
    # print('p(отк) =', '???')
    # print('Q =', round(q, 3))
    # print('nPod =', round(nPod, 3))
    # print('kn = ', round((nPod / n) * 100, 3), sep='')
    # print('tc =', round(tc, 3))
    # print('pOch =', round(pOch, 3))
    # print('mPod =', round(mPod, 3))
    # print('NPod =', round(NPod, 3))
    # print('tOch =', round(tOch, 3))
    table.add_row(['бес', '', '', '', '', '', '--'])
    print()


def mmnm(lam, mu, n, m):
    s = n + m + 1
    bk = [m]
    for k in range(1, s):
        bk.append(m / k * bk[k - 1])
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += (m ** i) / math.factorial(i)
    sum2 = 0
    for i in range(1, m + 1):
        sum2 += (m / n) ** i
    p0 = (1 + sum1 + (m ** n / math.factorial(n)) * sum2) ** -1
    pk = [p0]
    for i in range(1, s):
        pk.append(bk[i] * p0)
    # print(pk)
    pOtk = ((m ** n) / math.factorial(n)) * ((m / n) ** m) * p0
    q = lam * (1 - pOtk)
    nPod = m * (1 - pOtk)
    mPod = 0
    for s in range(1, m + 1):
        mPod += s * (((m ** n) / math.factorial(n)) * ((m / n) ** s) * p0)
    NPod = nPod + mPod
    tOch = mPod / lam
    tc = NPod / lam
    # print('-----Случай M/M/n/m-----')
    # print('p(отк) =', round(pOtk, 3))
    # print('Q =', round(q, 3))
    # print('nPod =', round(nPod, 3))
    # print('kn = ', round((nPod / n) * 100, 3), sep='')
    # print('tc =', round(tc, 3))
    table.add_row(['2', '', '', '', '', '', ''])
    # print('Сумма вероятностей ', round(sum(pk), 3), sep='')
    pass


if __name__ == '__main__':
    table.field_names = ['m', 'p(отк)', 'Q', 'n', 'kn', 'tc', 'сум вер']
    try:
        variant = int(input('введите вариант '))
        # variant = 7
        print()

        if not 1 <= variant <= 24:
            print('введите номер варианта от 1 до 24')
            exit(0)

        lam, mu, n, m = data(variant - 1)
        inputData = PrettyTable()
        inputData.field_names = ['вариант', 'lambda', 'mu', 'n', 'm']
        inputData.add_row([str(variant), str(lam), str(mu), str(n), str(m)])
        print(inputData)
        # print('вариант', variant)
        # print('lambda = ', lam, sep='')
        # print('mu = ', mu, sep='')
        # print('n = ', n, sep='')
        # print('m = ', m, sep='')
        # print()
        mmn0(2, 2, 2, 1)
        mmnm(2, 2, 2, 1)
        mmn8(2, 2, 2, 1)
        print(table)
    except ValueError:
        print('введите число')

    # table = PrettyTable()
    # table.field_names = ['m', 'p(отк)', 'Q', 'n', 'kn', 'tc']
    # table.add_row(['0', '', '', '', '', ''])
    # table.add_row(['2', '', '', '', '', ''])
    # table.add_row(['бес', '', '', '', '', ''])
    # table.align = 'c'
    # print(table)
    pass
