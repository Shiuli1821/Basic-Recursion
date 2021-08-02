def Fibonacci(n):
    """Implement the method below to calculate the nth fibonacci value."""
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == '__main__':
    print("Enter the number")
    nth_fibonacci = int(input())
    print("Fibonacci value at position " + str(nth_fibonacci) + " is " + str(Fibonacci(nth_fibonacci)))
