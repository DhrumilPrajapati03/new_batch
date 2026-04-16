#Area of triangle
def aot(b,h):
    return 0.5 *b * h

print(aot(5,6))

#Prime number
def is_prime(n):
    if n == 0 or n == 1:
        print(f"{n} is not prime")
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(f"{n} is not prime")
                break
        else:
            print(f"{n} is a prime number")
    else:
        print(f"{n} is not prime")

is_prime(17)

#reverse a string
def reverse_string(s):
    return s[::-1]

entered_string = input("Enter a string: ")
print(reverse_string(entered_string))