
def fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        print(f"Terme {i} : {a}")
        a, b = b, a + b
        
fibonacci(10)