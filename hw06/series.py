n = 4
s1 = 2
s2 = 1


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
    for i in range(2, n):
        ser[i] = ser[i - 1] + ser[i - 2]

# report the nth integer in the array.
print(ser[n - 1])
