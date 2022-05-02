# What is this doing and why?

class MyClass:

    def __init__(self, word):
        self.w = word
        self()

    def __call__(self, *args, **kwargs):
        print(self.w); return self


MyClass("Hello World!")("How are you?")("I'm fine")("Thanks")
