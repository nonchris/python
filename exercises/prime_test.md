## Prime tester
The goal is to write a function `is_prime(number: int) -> bool` that returns `True` if the input is prime.  

#### What is a prime number?
> A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. (...)  
> For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself. 
[Source: Wikipedia](https://en.wikipedia.org/wiki/Prime_number)

### How to start
Have a quick thought how you can test a number for prime using a programming language

* Declare a function `is_prime` that takes one number as input
* implement your first algorithm for testing and return the result

#### Testing
Write the `__main__` section of your code.  
This part shall include a `for`-loop iterating over the follwoing list, giving the first entry of each tuple as input to the function and comparing the return with the second value of the tuple.  

```
[(0, False), (1, False), (2, True), (3, True),
(4, False), (5, True), (6, False), (7, True),
(15, False), (21, False), (22, False), (23, True),
(32, False), (37, True),(41, True), (42, False),
(-1, False), (0, False), (2.1, False), (5.5, False)]
```

### Using the function
Create a second function:  
`generate_prime_table(limit: int) -> dict[int, bool]`  
This function takes an integer and generates a dict that mapps all integers form `0` to `limit` (limit is included) to a `boolean` indicating if the number is prime or not.  
Use your written* `isprime`-function to complete the task.  
Testing: `generate_prime_table(10)` should create the follwing output:  
> {0: False, 1: False, 2: True, 3: True, 4: False,
>  5: True, 6: False, 7: True, 8: False, 9: False, 10: False}

### Bonus
#### Quick tasks
* accept floats of the format `x.0`
* accept numbers as strings

#### Runtime optimization
Import the `time` modul at the top of you program:  
`import time`
Copy this finction into your code:  

```python=
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
```

Call `benchmark` with `generate_prime_table` as function, `1000` for times and `1000` for input.  
This should not take longer than 5 seconds.  
Maybe use some different values to get a feeling for the durations.  
Compare your result to the `0.43` seconds the implementation in the solution-file runs (on a Ryzen 3600 with 32gB RAM).  
If your code is significantly slower than that, try thinking about some ways to improve your runtime.  
Here are some hints:  
* what things do non-prime numbers have in common?
    * find ways to check for those features to return an answer faster
* at some point you need to iterate over all numbers not checked yet
    * which numbers are those, how can you only check these numbers?
    * up to which number is this needed


*Note*:  
If your test doesn't finish, decrease the numbers to `1` and `10` and try again. This should be as fast as your own generation of the first 10 numbers from the previous section.  
Try to work your way up from there.  

##### Caching
Python offers a `decorator` for caching processed return-values. Using it on the `is_prime` function should give your runtime a good boost. But this comes -obviously - at the cost of memory.  
[Documnentation for @cache]([generated](https://docs.python.org/3/library/functools.html#functools.cache)).  
Wait - what is a decorator?  
In short: It's a way to wrap your function inside an other one.
[A good real python tutorial about decorators](https://realpython.com/primer-on-python-decorators/).


### What else to say?
The generation of the `prime_table` using the `is_prime` function is *not efficient*.  
The program needs to run the whole check, counting up for each input number.  
For example: If we already know that 21 is not prime, why do we check for greater numbers if this number can be divided by 21? - We already checked that implicitly when checking for division by three (and seven).  

It would be way more efficent to use the generated knowledge while increasing the numbers.  
A better, simple, but not perfect solution for generating all primes up to a specific number would be the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).  
