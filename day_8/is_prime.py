# def prime_checker(number):
#     if number == 2:
#         print(f"{number} is a prime number")
#     elif number % 2 != 0:
#         if number % number == 0:
#             print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")


def prime_checker(number):
    is_prime = True

    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
