"""
Создайте следующую иерархию классов:

Animal (базовый класс)
    Mammal
        Dog
        Cat
        Horse
    Bird
        Eagle
        Penguin
    Reptile
        Snake
        Turtle
"""


class Animal:
    def __init__(self, name, class_, species):
        self.name = name
        self.class_ = class_
        self.species = species
    

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, 'mammal', species)

class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name, "dog")

class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name, "cat")

class Horse(Mammal):
    def __init__(self, name):
        super().__init__(name, "horse")



class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name, 'bird', species)

class Eagle(Bird):
    def __init__(self, name):
        super().__init__(name, "eagle")

class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name, "penguin")



class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, 'reptile', species)

class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name, "snake")

class Turtle(Reptile):
    def __init__(self, name):
        super().__init__(name, "turtle")