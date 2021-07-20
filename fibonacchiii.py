def fibonachii(num):
    if num == 1:
        return 0
    elif num ==2:
        return 1
    else:
        return fibonachii(num-1)+ fibonachii(num-2)


# 0 1 1 2 3 5 8 13 21



n = int(input("Enter which no. fibonachi you want to find: "))

print(fibonachii(n))