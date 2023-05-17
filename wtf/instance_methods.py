class MyClass:
    def __init__(self):
        self._value = "Cyber"

    def say_value(self):
        print(f"Old <say_value> function: {self._value}")


def scream_value(self):
    return print(f"{str(self._value).upper()}!")


def new_say_value(self):
    print(f"New <say_value> function: {self._value}")


old_instance = MyClass()

print()
print("Old instance before attach:")
old_instance.say_value()

print()
print("<Attaching new functions to class>")
setattr(MyClass, "scream_value", scream_value)
setattr(MyClass, "say_value", new_say_value)

new_instance = MyClass()

print()
print("New instance:")
new_instance.say_value()
new_instance.scream_value()

print()
print("Old instance after attach:")
old_instance.say_value()
old_instance.scream_value()
