## Was sollte man in python machen? V2
Dieser Leitfaden nimmt an, dass die Zuhörer\*innen bereits C, oder einen andere typisierte Sprache können.  
Ist dies nicht der Fall, sollte man vlt besser mal erklären, was Variablen sind und nicht OO vor Funktionen machen...  
Trotzdem kann er natürlich als Checklist herhalten, ob man alles wichtige abgedeckt hat :)  

### Was python?
- Interpretierte Skriptsprache
- cpythons Core ist in C programmiert
    - gibt aber mehr Implementationen - jython.
- python3(.10) ist aktuell
- Beliebt weil optimiert auf Programmierzeit
- Mies langsam im Vergleich zu C
- Garbage collected
    - No need to manage our Arbeitsspeicher

### Einstieg über C vs python
- python ist ein ganzes Stück weniger formal.

Code Beispiele vergleichen.
#### Hello World

```c=
#include <stdio.h>

int main(){
    printf("hello world\n");
}
```

```python=
print("Hello World")
```

#### Summe
```c=
int my_sum(int num_numbers, int *numbers) {
    int i;
    int sum = 0;
    for (i = 0; i < num_numbers; i++) {
        sum += numbers[i];
    }
    return sum;
}
```

```python=
def my_sum(numbers: list[int]) -> int:
    s = 0
    for number in numbers:
        s += number

    return s
```

Oder ganz dumm:
```python=
sum(numbers)
```

* Syntaktische Unterschiede erläutern
    * Einrückung
    * Semicolons
* python hat ein Menge mehr Funktionen eingebaut

### Weitere Unterschiede
- if, elif, else
    - 'boolsche Syntax' -> ==, !=, >=, > , and, or, is, not
- for, while
    - hier schon enumerate? - joar, haben ja build in fkts gehinted
    - Laufzeit von for-loops ist besser bzw while sucks


# Generelles
`__main__`, einfach erstmal schlucken


### Dynamische Typisierung
* dynamische Typisierung
    * Beispiele zeigen (a = str, a = int -> Kein Ärger)

### Objektorierntierung
- Vergleich zu C ziehen
    - Funktionale Sprache
    - Structs ansprechen
    - Art und Weise wie man damit umgeht, wenn fkt Aufruf

"Objekte sind gekapselte, dynamisch erzeugte Einheiten von Daten und Operationen" ~SWT  
(Ich hoffe das ist das erste und letzte Mal, dass ich dieses Modul zitiere...)  
-> Im Prinzip ein Struct, dass seine eigenen Funktionen mitbringt  

- Idee für anderes Beispiel: Pokemon

```python=
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def whoami(self):
        print(f"Ich bin {self.name} und {self.age} alt")

    def how_old_am_i(self):
        print(f"Ich bin {self.age} Jahre alt")


class Student(Person):
    def __init__(self, name: str, age: int, school: str):
        super().__init__(name, age)
        self.school = school

    def whoami(self):
        print(f"Ich bin {self.name} und gehe zur {self.school} Schule")


peter = Person("Peter", 44)
maxi = Student("Maxi", 12, "Konrad Adenauer Gymnasium")
lina = Student("Lina", 13, "Rhein Gymnasium")

peter.whoami()
maxi.whoami()
maxi.how_old_am_i()
lina.how_old_am_i()
    
```
* Auf init eingehen (Constructor)
* Wie Funktionen definiert werden (self!)
* Jedes Objekt einer Klasse hat seine eigenen Vars (versch. Objekte erstellen?)
* f-String kommt später
* Vererbung vollst. erklären, oder nur anreißen?
    * "Wir können damit Funktionen übernehmen". Fertig.

* Zeigen wie man Variablen verändert

### Datentypen
So. Jetzt wo klar ist, was Objekte sind: Kommen wir zu Datentypen.

* Mutable vs Immutable kurz anreißen

#### `type()`
Cool. Und wie finde ich jetzt raus welchen Typ eine Variable / ein Objekt hat?
```python=
x = "Hallo Welt"
print(type(3))
print(type(x))
print(type(peter))
```

* `isinstance()`


#### immutable
##### bool
* - True, False, None
    - int (bel. Länge), float -> alle Nummern was gibt
```python=
x = True
y = False
z = None

if x:
    print("x ist True")

if not y:
    print("y ist False!")
else:
    print("y ist True")

if z:
    print("z ist True")
elif z is None:
    print("z ist None")
```
##### int
    - to hex, to bytes?
    - Kurz anreißen, wie man "rechnet"
```python=
x = 5
y = 2
z = 6
print(x / y)   # 2.5
print(x // y)  # 2
print(z / y)   # 3.0

x = 5
y = 2.0
print(x / y)   # 2.5
print(x // y)  # 2.0
```

##### string (boah, krass! Das hat C nicht! :0)
  - f strings
  - strings kann man addieren und multiplizieren  
##### typecasting
* wie jetzt? Man kann aus einem float ein int machen?!
    * Ach so, das sind auch nur die Konstruktoren der Klassen?
    * und so kann man sogar aus einem Wort eine Zahl machen?! sick!
```python=
int_var = int("42")
print(int_var)
print(type(int_var))

str_var = str(32.0)
print(str_var)
print(type(str_var))
```
* oh. ja... python Übernimmt die Interpretation der daten beim print
##### bytes
* verhalten basically wie strings
    * Vorsicht! python interpretiert die Daten als text! (ascii?)
##### tuple
    - Überleitung zu immutable
    - Vorsicht! `x = (1)` erzeugt kein Tupel! `x = (1,)` schon


#### mutable
- datentypen sind run and go. was ist speicher allokieren?!
##### listen (alles kann da rein)
  - wie man listen mit bestimmtem stuff initialisiert
  - append, extend, remove
  - wie man auf listen zugreift
  - listen kann man multiplizieren und addieren
  - list comprehensions :D
  - listen können listen, dicts und andere verschachtelte typen enthalten!
    

```python=
my_list = [True, "Hallo Welt!", 42]
for elm in my_list:
    print(elm)

print(my_list[2])

my_list.append(None)
print(my_list)

my_list[3] = True
print(my_list)

# my_list[4] = True  # Fehler!

my_list[-1] = False
print(my_list)
```

```python=
comp_list = [i for i in range(0, 43)]  # numbers 0, 1, ..., 42
print(comp_list)
```


##### dict

```python=
i_am = {
    "name": "chris",
    "alter": 22,
    42: True,
}

print(i_am["name"])
i_am["uni"] = "bonn"

print(i_am["uni"])

for key in i_am.keys():
    print(i_am[key])
```
- vergleich zu jsons ziehen?
- auf .items() und .values() hinweisen
  - guter Zeitpunkt zu zeigen, dass man über mehrere Werte iterieren kann mit `.items()`
  - hinweis auf enumerate
- keys dürfen nur immutable Dinge sein!
- dict comprehensions ^^
- pprint?
- auch dicts kann man schachteln...
    
##### set 
    - wie listen nur anders
    - vorsicht mit dem constructor `{}` erzeugt ein dict!

##### try/ except
* es könenn Fehler auftreten, zB ein `IndexError`

```python=
try:
    my_list[4] = True
except IndexError:
    print("Die Liste hat nicht genug Plätze!")
finally:
    pass
```
* oft unschön. Es wäre besser das explizit abzufangen...  
* finally wird ausgeführt, auch wenn etwas massiv schiefgeht...
* pass ist einfach "nichts" ein Platzhalter
```python=
if len(my_list) >= 4:
    print("Die Liste hat nicht genug Plätze!")
else:
    my_list[4] = True
```
* Teils gibt es auch bereits interne Strukturen dafür
```python=
print(i_am.get("dozent", False))
```

#### ducktyping
* haben bereits `len` und `print` gesehen. Wie geht das?
- str, getitem, setitem, eq, leq
- `Person` beispiel von oben erweitern.

##### Aufgabe zum Anwenden:
[Custom String](https://gist.github.com/nonchris/25676e4d9c61d933168e352ef8a0bde1)  

### funktionen
Manchmal ist ein ganzes Objekt etwas viel... Funktionen!
- synatx - def... 
```python=
def my_own_sum(x: int, y: int) -> int:
    return x + y


res = my_own_sum(41, 1)
print(res)

```
* lambdas
```python=
l = lambda v: print(v)
l("hi")
```

* scope von Variablen
    * Variablen von außerhalb lesbar
    * Variablen von innerhalb exist. außerhalb nicht
- typehinting
    - Optional, aber sehr sinnvoll, damit andere und man selbst Dinge versteht...
- keyword args! 
    - funktionen können nicht überladen werden
        - ein fkt name kann nur eine funktion haben
    - Beispiel um `print_result=False` ausbauen
- \*args
    - Zeigen wir dass man mit dieser Syntax auch Dinge in mehrere Variablen entpacken kann?
- \*\*kwargs
- krass man kann funktionen übergeben
- bock auf decoratoren?
    - Gerade eher nicht so....

#### Kontextmanager
- with
    - open, conn
```python=
with open("my_file.txt", "w") as f:
    f.write("Hello world!")
   
# the same but more complicated...
try:
    f = open("my_file.txt", "w")
    f.write("Hello World! (Without context manager)")
except (OSError, FileExistsError, FileNotFoundError):
    pass
finally:
    f.close()
```
* an dieser Stelle "r", "w", "a", "w+" erklären

- an dieser Stelle könnte man mal auf builtin funktionen eingehen
    - range, enumerate, zip, sum, min, max
    - input!
    - construktoren dict, list, tuple...
- open, type, filter, enumerate, range, print

### imports
- hier `__main__` erklären
- syntax Unterschiede zwischen import x und from x import y
- die standard libraries
    - os, json, csv, math, functools, datetime

- was is ein Modul? - ach so im Grunde einfach nur eine python datei.

- zeigen was bei import mit eigener Datei passiert
    - Daher nur Funktionen und Klassen schreiben
    - if name == main

#### meet pip
* pip installs packages ;)  
- requirements.txt

#### geile libraries
* der standard Kram, numpy, pandas, matplotlib
* discord.py :D
* telegram
* wie man docs ließt


### Wenn man Zeit hat

#### Coding style
- if return, else return
    - nicht alles in ein if/ else packen

#### Walruss und Ternary Operator
* joa, Überschrift self-explaining, huh?


#### logging
* zeig halt dein standard logger, den du seit Jahren mit kopierst...

### Was ich nicht zeigen will
##### C Code wrappen.
Ich hab mir ctypes mal angesehen. Yikes. Schön ist anders.  
Außerdem habe ich einen dummen Benchmark einer gewrappten Funktion gegen "dummes" python gemacht und python hat gewonnen (Faktor 10).  
Damit das so Sinn macht muss man also scheinbar schon mehr also nur eine "sum()" Funktion einbinden wollen...  

#### Hässliche Dinge
Wie man eine Variable zur Laufzeit an ein Objekt anhängt oder anderen cursed stuff aus meinem github python Repo, den ich witzig finde.

#### Programmfluss
Dass man durch ein retrun weniger Einrückungen hat, eine Invertierung der if-condition oder continue wunder bewirken kann, will ich hier ungern in Tiefe zeigen.  
Dafür entwickelt man irgendwann selbst ein Gefühl.
