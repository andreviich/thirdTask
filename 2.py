import numpy as np
# используем nashpy для теории игр
import nashpy as nash
import random
vars = input('Введите количество стратегий...\n')

if vars.isdigit():
    vars = int(vars)
else:
    exit()
inputType = int(input("Введите вариант ввода:\n1. При помощи клавиатуры\n2. Случайные числа...\n"))

if inputType == 1:

    variants1 = [input(f'Введите {i+1} стратегию для игрока A...\n') for i in range(vars)]

    variants2 = [input(f'Введите {i+1} стратегию для игрока B...\n') for i in range(vars)]

    startMatrixPlayerA = []
    for i in range(vars):
        kfs = []
        for j in range(vars):
            kfs.append(float(input(f"Введите коэфициент для игрока A ({i+1} строка, {j+1} колонка)...")))
        startMatrixPlayerA.append(kfs)
    # startMatrixPlayerA = [[2,0],[4,2]]
    startMatrixPlayerB = []
    for i in range(vars):
        kfs = []
        for j in range(vars):
            kfs.append(float(input(f"Введите коэфициент для игрока B ({i+1} строка, {j+1} колонка)...")))
        startMatrixPlayerB.append(kfs)
elif inputType == 2:
    variants1 = ['Top', "Bottom"]
    variants2 = ['Left', "Right"]
    startMatrixPlayerA = [[random.randint(1,9) for i in range(2)] for i in range(2)]
    startMatrixPlayerB = [[random.randint(1,9) for i in range(2)] for i in range(2)]

game1 = nash.Game(np.array(startMatrixPlayerA),np.array(startMatrixPlayerB))

equilibria = list(game1.support_enumeration())

solution = equilibria[0]

print(f'Оптимальная стратегия для игрока A: {variants1[solution[0].tolist().index(1)]}')
print(f'Цена для игрока A: {startMatrixPlayerA[solution[0].tolist().index(1)][solution[1].tolist().index(1)]}')
print(f'Оптимальная стратегия для игрока B: {variants2[solution[1].tolist().index(1)]}')
print(f'Цена для игрока B: {startMatrixPlayerA[solution[1].tolist().index(1)][solution[0].tolist().index(1)]}')
print(f"Общая цена игры: {startMatrixPlayerA[solution[0].tolist().index(1)][solution[1].tolist().index(1)] + startMatrixPlayerA[solution[1].tolist().index(1)][solution[0].tolist().index(1)]}")
print(f"Количество равновесий: {len(list(equilibria))}")

if (len(equilibria) > 1):
    print(f"Таблица смежных стратегий для игрока A")
    for a,b in zip(variants1, list(equilibria[::-1][0][0])):
        print(f"{a} : {round(b, 3)*100}%")
    print("Цена игры для игрока А при выборе смешанной оптимальной стратегии")
    print(game1[startMatrixPlayerA, startMatrixPlayerB])
