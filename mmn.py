import math
from prettytable import PrettyTable as tablePr


class MMN:

    lam = 0
    mu = 0
    n = 0
    m = 0
    table = tablePr()

    def __init__(self, lam: float, mu: int, n: int, m: int):
        self.lam = lam
        self.mu = mu
        self.n = n
        self.m = m
        self.table = tablePr()
        self.table.title = 'таблица результатов'.upper()
        self.table.field_names = ['m', 'p(отк)', 'Q', 'n', 'kn', 'tc', 'сум. вер.']
        self.table.align = 'c'
        self.table.float_format = '.3'
        self.table.encoding = 'utf-8'

    def mmn0(self) -> None:
        """модель MMN0"""
        alfa = self.lam / self.mu
        summa = sum([(alfa ** k) / math.factorial(k) for k in range(1, self.n + 1)])
        p0 = (1 + summa) ** -1
        p = [(alfa ** k) / math.factorial(k) * p0 for k in range(1, self.n + 1)]
        p.insert(0, p0)
        p_otk = p[self.n]
        q = self.lam * (1 - p_otk)
        n_pod = alfa * (1 - p_otk)
        t_c = n_pod / self.lam
        self.table.add_row(['0', p_otk, q, n_pod, (n_pod / self.n) * 100, t_c, sum(p)])

    def mmnm(self) -> None:
        """модель MMNM"""
        alfa = self.lam / self.mu
        summa1 = sum([(alfa ** k) / math.factorial(k) for k in range(1, self.n + 1)])
        summa2 = sum([(alfa / self.n) ** s for s in range(1, self.m + 1)])
        p0 = (1 + summa1 + (alfa ** self.n) / math.factorial(self.n) * summa2) ** -1
        p = [p0]
        for k in range(1, self.n + 1):
            p.append((alfa ** k) / math.factorial(k) * p0)
        for s in range(1, self.m + 1):
            p.append(((alfa ** self.n) / math.factorial(self.n)) * ((alfa / self.n) ** s) * p0)
        p_otk = p[self.n + self.m]
        q = self.lam * (1 - p_otk)
        n_pod = alfa * (1 - p_otk)
        m_pod = sum([s * p[self.n + s] for s in range(1, self.m + 1)])
        n_big = n_pod + m_pod
        t_c = n_big / self.lam
        self.table.add_row(['2', p_otk, q, n_pod, (n_pod / self.n) * 100, t_c, sum(p)])

    def mmn8(self) -> None:
        """модель MMN∞"""
        alfa = self.lam / self.mu
        summa1 = sum([(alfa ** k) / math.factorial(k) for k in range(1, self.n + 1)])
        p0 = (1 + summa1 + ((alfa ** (self.n + 1)) / (math.factorial(self.n) * (self.n - alfa)))) ** -1
        p = [p0]
        for k in range(1, self.n + 1):
            p.append(((alfa ** k) / math.factorial(k)) * p0)
        for k in range(self.n + 1, self.n + 3):
            p.append((alfa ** k) / (math.factorial(self.n) * self.n ** (k - self.n)) * p0)
        p_och = 1 - sum(p[:-1])
        n_pod = alfa
        q = self.lam
        m_pod = (self.m * p_och) / (self.n - self.m)
        n_big = n_pod + m_pod
        t_c = n_big / self.lam
        t_och = m_pod / self.lam
        self.table.add_row(['∞', 'p(оч) ' + str(round(p_och, 3)), q, n_pod, (n_pod / self.n) * 100, t_c, '---'])

    def tableResult(self) -> tablePr:
        return self.table
