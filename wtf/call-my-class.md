The output is:  
```
Hello World!
Hello World!
Hello World!
Hello World!
```

### Why?
#### Basic mechanic
In python a function is basically an object that implements magic function `__call__(self, ...)`.  
Calling an object by `x` 'writing round brackets behind an object' like `x(a, b, c)` is effectively syntactic sugar for `x.__call__(a, b, c)`.  

#### This case
What happens is that the first bracket calls the 'constructor' method `__init__(self, ...)` (which calls itself once).   
After that the object is created, so that the other three tuples are directed to the `__call__` method.  
This example works because `__call__` returns `self` (hidden behind the print), so that we can chain function-calls.  
So the output stays `Hello World!` because the variable `self.w` is only set one (at the call of init) the latter inputs are simply swallowed by `*args` and thereby ignored.  
The obfuscation with arguments is a bit cheesy, the original version had no arguments and was just `MyClass()()()()` and printed `Hello World!` trice, but I like this more :)  

##### Extra tip
If you wanna give this to someone as a quiz consider introducing the `__str__()` function:  
```py
    def __str__(self):
        return f"{self.w}"
```
and replacing the `print(self.w)` in `__call__` to `print(self)`.  
This makes things a bit more confusing, since we're playing on even more magic functions.  
But I wanna keep my example a bit more understandable :D  
