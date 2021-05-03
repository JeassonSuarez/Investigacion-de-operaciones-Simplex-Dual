mat = [[1,-60,-100,0,0,0],
       [0,-10,-25,1,0,-50],
       [0,-12,-20,0,1,-49]]

numeroVariables=2

if mat[1][5]<mat[2][5]:
    menor = mat[1][5]
    menorFila=1
elif mat[1][5]>mat[2][5]:
    menor = mat[2][5]
    menorFila=2
else:
    menor = mat[1][5]
    menorFila=1
    
print(menor)
print(menorFila) ##fila pivot

m=10000000

for i in range(1,numeroVariables+1):
    if mat[0][i]/mat[menorFila][i] <= m:
        m= mat[0][i]/mat[menorFila][i]
        menorColumna=i 
        
pivoteUno=(1/mat[menorFila][menorColumna])

print(pivoteUno)  
print(m)
print(menorColumna) ##col pivot
    
    