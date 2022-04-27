import openpyxl as xl
from prettytable import PrettyTable as tablePr
from mmn import *


# получаем данные для варианта из файла xlsx
def data(v: int):
    """получение данных из файла xlsx"""
    book = xl.open(filename='table.xlsx', read_only=True)
    sheet = book.active
    lambdaV = []
    mu = []
    n = []
    m = []
    for row in range(2, sheet.max_row + 1):
        lambdaV.append(sheet[row][1].value)
        mu.append(sheet[row][2].value)
        n.append(sheet[row][3].value)
        m.append(sheet[row][4].value)
    return lambdaV[v], mu[v], n[v], m[v]


def table_designations() -> tablePr:
    """показатели эффективности СМО"""
    table = tablePr()
    table.title = 'показатели эффективности смо'.upper()
    table.field_names = ['показатель', 'значение показателя']
    table.align = 'l'
    table.add_row(['Q', 'пропускная способность'])
    table.add_row(['P(отк)', 'вероятность отказа в обслуживании'])
    table.add_row(['P(оч)', 'вероятность появления очереди'])
    table.add_row(['n_pod', 'среднее число занятых приборов'])
    table.add_row(['m_pod', 'среднее число заявок в очереди'])
    table.add_row(['N_pod', 'среднее число заявок в системе'])
    table.add_row(['t_оч', 'среднее время нахождения заявки в очереди'])
    table.add_row(['t_c', 'среднее время нахождения заявки в системе'])
    return table


# запрос варианта от пользователя
input_variant = input('введите номер варианта ')
variant = int()
if input_variant.isnumeric():
    variant = int(input_variant)
else:
    print('введите число')
    exit(-1)
# проверка на номер варианта от 1 до 24
if not 1 <= variant <= 24:
    print('введите номер варианта от 1 до 24')
    exit(-2)
lam, mu, n, m = data(variant - 1)
inputData = tablePr()
inputData.title = 'исходные данные для варианта'.upper()
inputData.field_names = ['вар.', 'λ', 'μ', 'n', 'm']
inputData.add_row(row=[variant, lam, mu, n, m])
inputData.align = 'c'
inputData.encoding = 'utf-8'
print(inputData)
print()
# вызов трех моделей и вывод в консоль в виде таблицы
mmn0(lam=lam, mu=mu, n=n, m=m)
mmnm(lam=lam, mu=mu, n=n, m=m)
mmn8(lam=lam, mu=mu, n=n, m=m)
print(table_designations(), '\n')
print(tableResult())
