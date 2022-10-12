import math
from prettytable import PrettyTable as tablePr

table = tablePr()
table.title = 'таблица результатов'.upper()
table.field_names = ['m', 'p(отк)', 'Q', 'n', 'kn', 'tc', 'сум. вер.']
table.align = 'c'
table.float_format = '.3'
table.encoding = 'utf-8'


def mmn0(lam, mu, n, m) -> None:
    """модель MMN0"""
    alfa = lam / mu
    summa = sum([(alfa ** k) / math.factorial(k) for k in range(1, n + 1)])
    p0 = (1 + summa) ** -1
    p = [(alfa ** k) / math.factorial(k) * p0 for k in range(1, n + 1)]
    p.insert(0, p0)
    p_otk = p[n]
    q = lam * (1 - p_otk)
    n_pod = alfa * (1 - p_otk)
    t_c = n_pod / lam
    table.add_row(['0', p_otk, q, n_pod, (n_pod / n) * 100, t_c, sum(p)])


def mmnm(lam, mu, n, m) -> None:
    """модель MMNM"""
    alfa = lam / mu
    summa1 = sum([(alfa ** k) / math.factorial(k) for k in range(1, n + 1)])
    summa2 = sum([(alfa / n) ** s for s in range(1, m + 1)])
    p0 = (1 + summa1 + (alfa ** n) / math.factorial(n) * summa2) ** -1
    p = [p0]
    for k in range(1, n + 1):
        p.append((alfa ** k) / math.factorial(k) * p0)
    for s in range(1, m + 1):
        p.append(((alfa ** n) / math.factorial(n)) * ((alfa / n) ** s) * p0)
    p_otk = p[n + m]
    q = lam * (1 - p_otk)
    n_pod = alfa * (1 - p_otk)
    m_pod = sum([s * p[n + s] for s in range(1, m + 1)])
    n_big = n_pod + m_pod
    t_c = n_big / lam
    table.add_row(['2', p_otk, q, n_pod, (n_pod / n) * 100, t_c, sum(p)])


def mmn8(lam, mu, n, m) -> None:
    """модель MMN∞"""
    alfa = lam / mu
    summa1 = sum([(alfa ** k) / math.factorial(k) for k in range(1, n + 1)])
    p0 = (1 + summa1 + ((alfa ** (n + 1)) / (math.factorial(n) * (n - alfa)))) ** -1
    p = [p0]
    for k in range(1, n + 1):
        p.append(((alfa ** k) / math.factorial(k)) * p0)
    for k in range(n + 1, n + 3):
        p.append((alfa ** k) / (math.factorial(n) * n ** (k - n)) * p0)
    p_och = 1 - sum(p[:-1])
    n_pod = m
    q = lam
    m_pod = (m * p_och) / (n - m)
    n_big = n_pod + m_pod
    t_c = n_big / lam
    t_och = m_pod / lam
    table.add_row(['∞', 'p(оч) ' + str(round(p_och, 3)), q, n_pod, (n_pod / n) * 100, t_c, '---'])


def tableResult() -> tablePr:
    return table


def table_clear():
    table.clear()
