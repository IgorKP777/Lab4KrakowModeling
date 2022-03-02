import openpyxl as xl
from prettytable import PrettyTable as tablePr
from mmn import MMN


def data(v: int):
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


if __name__ == '__main__':

    variant = int()
    try:
        variant = int(input('введите вариант '))
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
    models = MMN()
    models.mmn0(lam=lam, mu=mu, n=n, alfa=m)
    models.mmnm(lam, mu, n, m)
    models.mmn8(lam=lam, mu=mu, n=n, alfa=m)
    # models.mmn0(2, 2, 2, 1)
    # models.mmnm(2, 2, 2, 1)
    # models.mmn8(2, 2, 2, 1)
    print('таблица результатов')
    print(models.tableResult())
