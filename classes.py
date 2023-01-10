#Collins Wanga

class Dog:
    
    species = "Canis familiaris"
    def __init__(self, name, age,coat_color):
        
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
    def color (self):
        return f" {self.name}'s coat is {self.coat_color}."

class JackRussellTerrier(Dog):
    pass
class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass
