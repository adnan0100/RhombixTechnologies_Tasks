# Fibonacci Generator in Python

def fib_generator(n):
    """
    Generator that yields the first n Fibonacci numbers.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage: print the first 10 Fibonacci numbers
if __name__ == "__main__":
    for num in fib_generator(10):
        print(num)
