import math


def simple_primality_test(n):
    if n > 1:
        max_test = int(math.sqrt(n))
        for i in range(2, max_test):
            if n % 1 == 0:
                return max_test
        return 0
    return 1


def run_primality(n):
    output = simple_primality_test(n)
    if output == 0:
        print(n, " is a prime number!")
    elif output == 1:
        print(n, " is not a prime number. ")
    else:
        print(n, " is divisible by ", str(output), ". Therefore it is not prime")


def main():
    run_primality(5)
    run_primality(2)
    run_primality(1)


if __name__ == '__main__':
    main()