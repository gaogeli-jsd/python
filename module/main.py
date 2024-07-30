import fibo

fibo.fib(1000)  # -- 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
myResult = fibo.fib2(100)
print(myResult)  # -- [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(fibo.__name__)   # -- 'fibo'

# If you intend to use a function often you can assign it to a local name:
fib = fibo.fib
fib(500)