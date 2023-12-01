matrix = []
maior = []

for i in range(3):
    matrix.append([])
    maior.append([])
    for c in range(3):
        matrix[i].append([])
        
for i in range(3):
    for c in range(3):
        matrix[i][c] = float(input('Insira um valor: '))
        if c == 0:
            maior[i] = float(matrix[i][c])
        else:
            if float(matrix[i][c]) > float(maior[i]):
                maior[i] = float(matrix[i][c])
print(f'Os maiores valores de cada linha da matriz {matrix} são: {maior}')
