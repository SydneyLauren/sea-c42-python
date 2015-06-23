

# write Fibonacci series up to n
def fibonacci(n):
    """The fibonacci function returns the nth values of the
    fibonacci series where n is a user-input number."""
    # create an array to populate
    fib = list(range(1, n + 2))
    # assign the first two values in the array
    fib[0] = 0
    fib[1] = 1
    # if the wants something beyond the first two values, calculate in loop
    if n > 2:
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
    # report the nth integer in the array.
    print(fib[n])


def lucas(n):
    """The lucas function returns the nth values of the
    lucas series where n is a user-input number."""
    # create an array to populate
    luc = list(range(1, n + 2))
    # assign the first two values in the array
    luc[0] = 2
    luc[1] = 1
    # if the wants something beyond the first two values, calculate in loop
    if n > 2:
        for i in range(2, n + 1):
            luc[i] = luc[i - 1] + luc[i - 2]
    # report the nth integer in the array.
    print(luc[n])


def sum_series(n, s1=0, s2=1):
    """The sum_series function returns the nth values of the
    either the fibonacci or lucas series where n is a
    user-input number. The fibonacci series will be calculated
    by default if no user input starting numbers (s1 and s2) are
    provided for the series."""
    # create an array to populate
    ser = list(range(1, n + 2))
    # assign the first two values in the array
    ser[0] = s1
    ser[1] = s2
    # if the wants something beyond the first two values, calculate in loop
    if n > 2:
        for i in range(2, n + 1):
            ser[i] = ser[i - 1] + ser[i - 2]
    # report the nth integer in the array.
    print(ser[n])
    if __name__ == "__main__":
        # Test fibonacci series
        assert(fibonacci(0) == 0)
        assert(fibonacci(1) == 1)
        assert(fibonacci(2) == 1)
        assert(fibonacci(3) == 2)
        # Test lucas series
        assert lucas(0) == 2
        assert lucas(1) == 1
        assert lucas(2) == 3
        assert lucas(3) == 4
        # Test sum_series
        assert sum_series(0) == 0
        assert sum_series(1) == 1
        assert sum_series(2) == 1
        assert sum_series(0, 2, 1) == 2
        assert sum_series(1, 2, 1) == 1
        assert sum_series(2, 2, 1) == 3
