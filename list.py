matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(len(matrix[0]))
print(matrix[1][2])


for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end=" ")
    print("\n")


rows=int(input("enter the number of rows."))
cols=int(input("enter the number of columns."))

matrix=[]

for i in range(rows):
    temp=[]
    for j in range(cols):
        x=int(input("enter your element "))
        temp.append(x)
    matrix.append(temp)
print(matrix)

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end="*")
    print("\n")