name = input("Please enter your name:")
print(f"Your name is {name[0]}")

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Hello(self):
        print(f"Hello my name is {self.name}, I'm {self.age} years old.")

tom = Person("Tom", 18)
tom.Hello()