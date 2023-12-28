import math
import time


def simple_primality_test(n):
    if n > 1:
        max_test = int(math.sqrt(n)) + 1
        for i in range(2, max_test):
            if n % i == 0:
                return i
        return 0
    return 1


def only_odd_primality_test(n):
    if n > 1:
        max_test = int(math.sqrt(n)) + 1
        if n % 2 == 0:
            return 2
        for i in range(3, max_test, 2):
            if n % i == 0:
                return i
        return 0
    return 1


def six_k_primality_testing(n):
    # All prime numbers greater than 3 are of the form 6k +- 1. We can check only divisors of the form 6k +-1 and 2, 3.
    if n > 1:
        if n % 2 == 0:
            return 2
        if n % 3 == 0:
            return 3
        max_test = int(math.sqrt(n)) + 1
        for k in range(1, int(max_test/6) + 1):  # max_k = int(max_test/6) + 1
            if n % (6 * k - 1) == 0:
                return 6 * k - 1
            if n % (6 * k + 1) == 0:
                return 6 * k + 1
        return 0
    return 1


def run_primality(n):

    print("Simple primality testing")
    start = time.time()
    output = simple_primality_test(n)
    end = time.time()
    elapsed = end - start
    if output == 0:
        print(n, " is a prime number!")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using simple primality testing)")
    elif output == 1:
        print(n, " is not a prime number. ")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using simple primality testing)")
    else:
        print(n, " is divisible by ", output, ". Therefore it is not prime.")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using simple primality testing)")

    print("Only odd primality testing: ")
    start = time.time()
    output = only_odd_primality_test(n)
    end = time.time()
    elapsed = end - start
    if output == 0:
        print(n, " is a prime number!")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using only odd primality testing)")
    elif output == 1:
        print(n, " is not a prime number. ")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using only odd primality testing)")
    else:
        print(n, " is divisible by ", output, ". Therefore it is not prime.")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using only odd primality testing)")

    print("Six k primality testing: ")
    start = time.time()
    output = only_odd_primality_test(n)
    end = time.time()
    elapsed = end - start
    if output == 0:
        print(n, " is a prime number!")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using six k primality testing)")
    elif output == 1:
        print(n, " is not a prime number. ")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using six k primality testing)")
    else:
        print(n, " is divisible by ", output, ". Therefore it is not prime.")
        print(f"Calculated in: {elapsed:.6f} seconds. (Using six k primality testing)")


def main():
    # run_primality(5)
    # run_primality(2)
    # run_primality(1)
    # run_primality(4)
    run_primality(7919)
    run_primality(999983)
    run_primality(9000011)
    run_primality(800000000047)
    run_primality(990000017087)


if __name__ == '__main__':
    main()
