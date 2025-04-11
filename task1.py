def fib(num):
    a=0
    b=1
    for _ in range(num):
        print(a, end=' ')
        temp = a
        a = b
        b = temp + b




x = int(input("Enter the number of Fibonacci numbers you want to print: "))
fib(x)

#done task 1