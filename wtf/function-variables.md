The output is:  
```
10
```

### Why?
Python is a dynamic programming language, it's possible to set new variables on objects during runtime.  
Functions are objects too.  
The function body won't be evaluated (except for syntax) until it's called in the code. So it's no problem that `function.x` doesn't exit yet.  
Then `function.x` is set to `5` on the function-object.  
After that the function is called. It can access and modify the variable set on itself (note that there is no `self`-context.  
Now the modified variable is printed :)   
The parameter `x` in the function is just there for confusion, it has no effect :P
