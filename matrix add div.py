matrix_a=[[1,2],[22,4]]
matrix_b=[[5,6],[7,8]]
add_result=[[0,0],[0,0]]
div_result=[[0,0],[0,0]]

for i in range(0,len(matrix_a)):
    for j in range(0,len(matrix_a[0])):
        add_result[i][j]=matrix_a[i][j]+matrix_b[i][j]
        

print(add_result)


for i in range(0,len(matrix_a)):
    for j in range(0,len(matrix_a[0])):
        div_result[i][j]=matrix_a[i][j]/matrix_b[i][j]

print(div_result)