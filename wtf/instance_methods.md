The output is:
```
Old instance before attach:
Old <say_value> function: Cyber

<Attaching new functions to class>

New instance:
New <say_value> function: Cyber
CYBER!

Old instance after attach:
New <say_value> function: Cyber
CYBER!

Are instances of the same type?
True
```

### Why
Well. Since classes are objects too it seems, it seems like there is just one blueprint of a class that all instances reference too, ignoring if the class was modified since.  
But I actually don't know the internals or motivations behind this, so it's rather an educated guess.
