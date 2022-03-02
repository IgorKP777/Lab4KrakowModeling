import math
from prettytable import PrettyTable as tablePr

table = tablePr()
table.field_names = ['m', 'p(отк)', 'Q', 'n', 'kn', 'tc', 'сум. вер.']
table.title = 'таблица результатов'


class MMN:

    def __init__(self):
        pass

    # модель MMN0
    def mmn0(self, lam, mu, n, alfa) -> None:
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
            ['0', round(pOtk, 3), round(q, 3), round(nPod, 3), round((nPod / n) * 100, 3), round(tC, 3),
             round(sum(pk), 3)])

    # модель MMNM
    def mmnm(self, lam, mu, n, m, alfa=1) -> None:
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
            ['2', round(pOtk, 3), round(q, 3), round(nPod, 3), round((nPod / n) * 100, 3), round(tc, 3),
             round(sum(pk), 3)])

    # модель MMN∞
    def mmn8(self, lam, mu, n, alfa) -> None:
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

    def tableResult(self) -> tablePr:
        return table
