### Custom String
A task to play with function overloading and slicing of elements.  
Our goal is to implement a basic string-class that is mutable (parts can be changed after creation).    
The built-in string-class of python is not mutable, this class will be.   

```py
class CustomString:
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass

    def __str__(self):
        pass
```

This is important for all the upcoming tasks:  
Just try it out!  
Try to figure out what you're getting in e.g. `__getitem__` as inputs when calling the function by simply printing the types and values of the inputs it received.  

#### 1. Basic implementation
Let `__init__` take a normal python string as an argument and fill `__str__` with useful code.  

#### 2. Write code for `__getitem__`
Get item is the function called when accessing slices of a string, a list or something similar. It returns the requested part of that object:  
```py
my_string = "Hello"
print(my_string[0])     # Output: H
print(my_string[0:4])   # Output: Hell
```
Make `__getitem__` return the accessed item.  
It's enough if you just focus on the first example only for now.  

#### 3. Write `__setitem__`
This is the function called when replacing an element in e.g. a dict or a list.  
Strings can't do that since they're immutable.  
The whole goal of this task is to create a class that can do this.  
Example:  
```py
my_list = ["a", "b", "c"]
my_list[0] = "z"
print(my_list)  # Output: ["z", "b", "c"]
```
Implement `__setitem__` in a way that your class can do this.  

Ensure that `my_list[0] = "xx"` does not work. The string shall have the same length after replacement.  

#### 4. Futher operations
Let's try something more wild, now that your class can to 'simple' replacements.  
What happens if we do the following:  

```py
s1 = CustomString("0123456789")
s1[4:6] = "xx"
print(s1)
```

What happens? - Are you able to make this work too?  
Make sure, that the first way of access (from `3`) keeps working!  

#### 5. Replacing part three
You might know that slicing supports this syntax e.g. `[1:]` to get every item in you object expect the first one (at position 0).  
Try how your CustomString behaves when you're trying this:
```py
s1 = CustomString("0123456789")
s1[4:] = "xx"
print(s1)
```
Does it handle this access as expected? - If not, can you fix it?  
What happens if you try: `[:]` as slicining?  

A valid implementation would be that a replacement 'up to the end' is only valid if the length of the replacement equals the length of the characters to replace.  
So that the given example above would be invalid, because it does not define what should happen to the `"6789"` substring.  

#### 6. `__getitem__` part 2
Now that you saw what's possible in `__setitem__` with task `4` and `5`...  
Are you able to allwo the same operations for `_getitem__`?  
Example:  
```py
s1 = CustomString("0123456789")
print(s1[1:])
```

#### 7. One more thing
Now that you went through all of this pain getting a string-class that is mutable...  
Should you go ahead and use it all the time? - Why didn't the python devs just do exactly what you did? It wasn't _that hard_... was it?  
No. But you're not quite done yet.  
First you should consider implementing functions for comparing your class to other objects of you class and maybe even to objects the normal string class?  
And there are other functions as well that should be written.  

Second: Immutability has advantages! - You can hash those objects to use them as keys in dictionaries for example.  
You'll lerarn more on those topics when continuing to study computer science.  
Just hang on a bit for now :)  

This task was mainly for fun and showing you the power of slicing and how those fancy brackets are just syntactic sugar for some more basic function calls.  
There is nothing to fear. Just stay curious! :)
