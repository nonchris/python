import time


def is_prime(n: int) -> bool:
    """
    A (rather optimized) prime tester
    :param n: integer to test for prime
    :returns: boolean if n is prime
    """

    # we only support integers
    if not isinstance(n, int):
        return False

    if n <= 1:  # n is negative, 0 or 1
        return False

    elif n <= 3:  # case n=2, n=3
        return True

    if n % 2 == 0 or n % 3 == 0:  # cases we can rule out to skip numbers in for-loop
        return False

    # only need to check each odd number and only until its square-root
    # after that the number can't be composed by any multiplication we didn't cover yet
    # int creates the floor of the root, but that's since it's the greatest int that could create the number
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False

    return True  # everything was tested, the number must be prime


def generate_prime_table(limit: int) -> dict[int, bool]:
    """
    Generate a table mapping each integer to a bool indicating if number is prime
    :param limit: Table will be generated for all numbers including limit
    :return: A dict that maps each number to the boolean value if number is prime
    """
    prime_table = {}
    for i in range(limit+1):
        prime_table[i] = is_prime(i)

    return prime_table


def benchmark(function, times: int, fn_input=1000) -> float:
    """
    A function executing an other function measuring the time the execution took, prints the result
    :param function: Reference to the function that shall be executed
    :param times: How often the function shall be executed
    :param fn_input: Input to give the function to test
    :return: the time delta the processing took
    """
    start = time.time()
    for i in range(times):
        function(fn_input)

    stop = time.time()
    delta = stop-start
    print(f"The time was {delta} seconds")

    return delta


if __name__ == '__main__':

    # testing function with those inputs
    to_test = [(0, False), (1, False), (2, True), (3, True),
               (4, False), (5, True), (6, False), (7, True),
               (15, False), (21, False), (22, False), (23, True),
               (32, False), (37, True), (41, True), (42, False),
               (-1, False), (0, False), (2.1, False), (5.5, False)]

    for num, truth in to_test:
        if not is_prime(num) == truth:
            print(f"{num} returned the wrong value! - It should be: '{truth}'")

    print("Finished testing")

    # generating a dict of all numbers up to 10
    table = generate_prime_table(10)

    # running benchmark
    benchmark(generate_prime_table, 1000, 1000)
