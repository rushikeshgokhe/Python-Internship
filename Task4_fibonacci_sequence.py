num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    print("Fibonacci sequence:")
    for i in range(num_terms):
        print(a, end=" ")
        a, b = b, a + b
