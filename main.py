import math as math
import openpyxl as xl
from prettytable import PrettyTable as tablePr


table = tablePr()


def data(v):
    book = xl.open(filename='table.xlsx', read_only=True)
    sheet = book.active
    lambdaV = []
    mu = []
    n = []
    m = []
    for row in range(2, sheet.max_row):
        lambdaV.append(sheet[row][1].value)
        mu.append(sheet[row][2].value)
        n.append(sheet[row][3].value)
        m.append(sheet[row][4].value)
    return lambdaV[v], mu[v], n[v], m[v]


def mmn0(lam, mu, n, alfa):
    s = n + 1
    bk = [float(alfa)]
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
    table.add_row(
        ['∞', round(pOch, 3), round(q, 3), round(nPod, 3), round((nPod / n) * 100, 3), round(tc, 3), '---'])
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
    inputData = tablePr()
    inputData.field_names = ['вариант', 'lambda', 'mu', 'n', 'm']
    inputData.add_row(row=[variant, lam, mu, n, m])
    inputData.align = 'c'
    print('исходные данные для варианта')
    print(inputData)
    print()
    mmn0(lam, mu, n, m)
    mmnm(lam, mu, n, m)
    mmn8(lam, mu, n, m)
    # mmn0(2, 2, 2, 1)
    # mmnm(2, 2, 2, 1)
    # mmn8(2, 2, 2, 1)
    print('таблица результатов')
    print(table)
