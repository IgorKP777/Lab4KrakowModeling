import math
from prettytable import PrettyTable

table = PrettyTable()


def data(v):
    lambdaV = [4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 4.8, 5.0, 2.6, 5.3, 4.1, 2.2, 2.4, 2.5, 5.2,
               2.4, 5.1, 2.3]
    mu = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1]
    n = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    m = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    return lambdaV[v], mu[v], n[v], m[v]


def mmn0(lam, mu, n, alfa):
    s = n + 1
    bk = [alfa]
    for i in range(1, s):
        bk.append(alfa / i * bk[i - 1])
    p0 = 1 / sum(bk)
    pk = [p0]
    for i in range(1, s):
        pk.append(bk[i] * p0)
    pOtk = (alfa ** n) / math.factorial(n) * p0
    q = lam * (1 - pOtk)
    nPod = alfa * (1 - pOtk)
    tC = nPod / lam
    table.add_row(
        ['0', round(pOtk, 3), round(q, 3), round(nPod, 3), round((nPod / n) * 100, 3), round(tC, 3), round(sum(pk), 3)])


# def mmn8(lam, mu, n, alfa):
#     sum1 = 0
#     for i in range(1, n):
#         sum1 += (alfa ** i) / math.factorial(i)
#     p0 = (1 + sum1 + ((alfa ** (n + 1)) / (math.factorial(n) * (n - alfa)))) ** -1
#     pk = [p0]
#     for i in range(1, n + 1):
#         pk.append(((alfa ** i) / (math.factorial(i) * n ** (i - n))) * p0)
#
#     print(pk)
#     sum2 = 0
#     for i in range(n - 1):
#         sum2 += pk[i]
#     pOch = 1 - sum2
#
#     nPod = alfa
#
#     mPod = (alfa * pOch) / (n + 1 - alfa)
#     NPod = mPod + nPod
#     q = lam
#     tOch = mPod / lam
#     tc = NPod / lam
#     table.add_row(['бес', round(pOch, 3), round(q, 3), round(nPod, 3), round((nPod / n) * 100, 3), round(tc, 3), '---'])

def mmn8(lam, mu, n, alfa):
    sum1 = 0
    for k in range(1, n + 1):
        sum1 += ((alfa ** k) / math.factorial(k))
    p0 = (1 + sum1 + ((alfa ** (n + 1)) / (math.factorial(n) * (n - 1)))) ** -1
    pk = [p0]
    for k in range(1, n + 1):
        pk.append(((alfa ** k) / math.factorial(k)) * p0)
    nPod = alfa
    pOch = 1 - sum(pk) + pk[-1]
    mPod = (alfa * pOch) / (n / alfa)
    NPod = nPod + mPod
    q = lam
    tOch = mPod / lam
    tc = NPod / lam
    table.add_row(['\'бес\'', round(pOch, 3), round(q, 3), round(nPod, 3), round((nPod / n) * 100, 3), round(tc, 3), '---'])
    pass


def mmnm(lam, mu, n, m, alfa=1):
    s = n + m + 1
    bk = [float(alfa)]
    for k in range(1, n):
        bk.append(alfa / k * bk[k - 1])
    for k in range(n, s):
        bk.append(alfa / n * bk[k - 1])
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += (m ** i) / math.factorial(i)
    sum2 = 0
    for i in range(1, m + 1):
        sum2 += (m / n) ** i
    p0 = (1 + sum1 + (m ** n / math.factorial(n)) * sum2) ** -1
    pk = [p0]
    for k in range(1, len(bk)):
        pk.append(bk[k] * p0)
    # bk = [alfa]
    # for k in range(1, s):
    #     bk.append(alfa / k * bk[k - 1])
    # sum1 = 0
    # for i in range(1, n + 1):
    #     sum1 += (m ** i) / math.factorial(i)
    # sum2 = 0
    # for i in range(1, m + 1):
    #     sum2 += (m / n) ** i
    # p0 = (1 + sum1 + (m ** n / math.factorial(n)) * sum2) ** -1
    # pk = [p0]
    # for i in range(1, s):
    #     pk.append(bk[i] * p0)
    # # print(pk)
    #
    pOtk = ((m ** n) / math.factorial(n)) * ((m / n) ** m) * p0
    q = lam * (1 - pOtk)
    nPod = m * (1 - pOtk)
    mPod = 0
    for s in range(1, m + 1):
        mPod += s * (((m ** n) / math.factorial(n)) * ((m / n) ** s) * p0)
    NPod = nPod + mPod
    tOch = mPod / lam
    tc = NPod / lam
    table.add_row(
        ['2', round(pOtk, 3), round(q, 3), round(nPod, 3), round((nPod / n) * 100, 3), round(tc, 3), round(sum(pk), 3)])
    pass


if __name__ == '__main__':

    table.field_names = ['m', 'p(отк)', 'Q', 'n', 'kn', 'tc', 'сум. вер.']

    variant = int()
    try:
        # variant = int(input('введите вариант '))
        variant = 7
        print('ваш вариант', variant)
        print()
    except ValueError:
        print('введите число')
        exit(-1)

    if not 1 <= variant <= 24:
        print('введите номер варианта от 1 до 24')
        exit(-2)

    lam, mu, n, m = data(variant - 1)
    inputData = PrettyTable()
    inputData.field_names = ['вариант', 'lambda', 'mu', 'n', 'm']
    inputData.add_row([variant, lam, mu, n, m])
    inputData.align = 'c'
    print('исходные данные для варианта')
    print(inputData)
    print()
    # mmn0(lam, mu, n, m)
    # mmnm(lam, mu, n, m)
    # mmn8(lam, mu, n, m)
    mmn0(2, 2, 2, 1)
    mmnm(2, 2, 2, 1)
    mmn8(2, 2, 2, 1)
    print('таблица результатов')
    print(table)
