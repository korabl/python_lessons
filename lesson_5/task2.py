with open('task2.txt', 'r') as f:
    i = 0
    j = 0
    for line in f:
        if not line.isspace():
            i += 1
        for s in line:
            if not s.isspace():
                j += 1
    print(f'Кол-во строк - {i}, Кол-во букв - {j}')

