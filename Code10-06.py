def star(n):
    if n > 0:
        star(n-1)
        print('*'*n)




star(5)