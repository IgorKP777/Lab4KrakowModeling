import math
from prettytable import PrettyTable as tablePr

table = tablePr()
table.title = 'таблица результатов'
table.field_names = ['m', 'p(отк)', 'Q', 'n', 'kn', 'tc', 'сум. вер.']
table.align = 'c'
table.float_format = '.3'
table.encoding = 'utf-8'


class MMN:

    # модель MMN0
    def mmn0(self, lam, mu, n, m) -> None:
        alfa = lam / mu
        summa = float()
        for k in range(1, n + 1):
            a = (alfa ** k) / math.factorial(k)
            summa += a
        p0 = (1 + summa) ** -1
        p = [p0]
        for k in range(1, n + 1):
            p.append((alfa ** k) / math.factorial(k) * p0)
        p_otk = p[n]
        q = lam * (1 - p_otk)
        n_pod = alfa * (1 - p_otk)
        t_c = n_pod / lam
        table.add_row(['0', p_otk, q, n_pod, (n_pod / n) * 100, t_c, sum(p)])

    # модель MMNM
    def mmnm(self, lam, mu, n, m) -> None:
        alfa = lam / mu
        summa1 = float()
        for k in range(1, n + 1):
            summa1 += (alfa ** k) / math.factorial(k)
        summa2 = float()
        for s in range(1, m + 1):
            summa2 += (alfa / n) ** s
        p0 = (1 + summa1 + (alfa ** n) / math.factorial(n) * summa2) ** -1
        p = [p0]
        for k in range(1, n + 1):
            p.append((alfa ** k) / math.factorial(k) * p0)
        for s in range(1, m + 1):
            p.append(((alfa ** n) / math.factorial(n)) * ((alfa / n) ** s) * p0)
        p_otk = p[n + m]
        q = lam * (1 - p_otk)
        n_pod = alfa * (1 - p_otk)
        m_pod = float()
        for s in range(1, m + 1):
            m_pod += s * p[n + s]
        n_big = n_pod + m_pod
        t_c = n_big / lam
        table.add_row(['2', p_otk, q, n_pod, (n_pod / n) * 100, t_c, sum(p)])

    # модель MMN∞
    def mmn8(self, lam, mu, n, m) -> None:
        alfa = lam / mu
        summa1 = float()
        for k in range(1, n + 1):
            summa1 += (alfa ** k) / math.factorial(k)
        p0 = (1 + summa1 + ((alfa ** (n + 1)) / (math.factorial(n) * (n - alfa)))) ** -1
        p = [p0]
        for k in range(1, n + 1):
            p.append(((alfa ** k) / math.factorial(k)) * p0)

        print(p, sum(p))
        # table.add_row(['∞', pOch, q, nPod, (nPod / n) * 100, tc, '---'])
        pass

    def tableResult(self) -> tablePr:
        return table
