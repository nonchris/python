The output is:  
```
(9, 8, 7)
(9, 8, 7)
(9, 8, 7)
```

### Why?
Python does assume `9, 8, 7` as a tuple: `(9, 8, 7)`.  
This tuple will then be assigned to x, y and z.  
Don't get confused with `x, y, z = 9, 8, 7` which would _unpack_ the tuple to `x = 9`, `y = 8`, `z = 7`.  