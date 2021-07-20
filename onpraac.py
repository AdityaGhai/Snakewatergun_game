def matrix(a,b):
    o = []
    for i in range(a):
       row =[]
       for j in range(b):
           inp = int(input(f"Enter value [{i}][{j}]"))
           row.append(inp)
       o.append(row)

    return o

def sum(c,d):
    output = []
    for i in range(len(c)):
        rows = []
        for j in range(len(c[0])):
            rows.append(c[i][j] + d[i][j])

        output.append(rows)
    return output




m = int(input("Enter no. of rows: "))
n = int(input("Enter no. of coloumns: "))

print("Enter matrix A ")
A = matrix(m,n)
print(A)

print("Enter matrix B ")
B = matrix(m,n)
print(B)

print("Sum of matrix ")
C = sum(A,B)
print(C)


