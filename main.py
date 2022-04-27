import openpyxl as xl
from prettytable import PrettyTable as tablePr
from mmn import MMN


# получаем данные для варианта из файла xlsx
def data(v: int):
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


while 1:
    # запрос варианта от пользователя
    variant = int()
    try:
        variant = int(input('введите вариант '))
        print()
    except ValueError:
        print('введите число')
        exit(-1)

    # проверка на номер варианта от 1 до 24
    if not 1 <= variant <= 24:
        print('введите номер варианта от 1 до 24')
        exit(-2)

    lam, mu, n, m = data(variant - 1)
    inputData = tablePr()
    inputData.title = 'исходные данные для варианта'
    inputData.field_names = ['вариант', 'lambda', 'mu', 'n', 'm']
    inputData.add_row(row=[variant, lam, mu, n, m])
    inputData.align = 'c'
    inputData.encoding = 'utf-8'
    print(inputData)
    print()
    # вызов трех моделей и вывод в консоль в виде таблицы
    models = MMN()
    # models.mmn0(lam=lam, mu=mu, n=n, m=m)
    # models.mmnm(lam=lam, mu=mu, n=n, m=m)
    # models.mmn8(lam=lam, mu=mu, n=n, m=m)
    models.mmn8(lam=2, mu=2, n=2, m=1)
    print(models.tableResult())
