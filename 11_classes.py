# Classes
# Classes are blueprints for creating objects. They encapsulate data and behavior.
# A class is defined using the `class` keyword followed by the class name and a colon.
# Classes can have attributes (data) and methods (functions) that operate on that data.
# Classes can also have a constructor method `__init__` that initializes the object's attributes.
# Classes can be empty, meaning they do not have any attributes or methods defined con pass.
# Classes can also have methods that perform actions or calculations.
# Classes can be instantiated to create objects, which are instances of the class.
# Classes can be used to create objects with specific attributes and methods.
# Classes are a fundamental part of object-oriented programming in Python.


class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(type(MyEmptyPerson))
print(MyEmptyPerson())
print(type(MyEmptyPerson()))


class Person:

    def __init__(self, age, name = "Pedri", surname = "Loco"): #Constructor method that initializes the object's attributes
        self.name = name
        self.surname = surname
        self.age = age
        self.__name = "Pepe"  # Atributo privado, no se puede acceder directamente desde fuera de la clase
        self.__surname = "Loco"  # Atributo privado, no se puede acceder directamente desde fuera de la clase
        self.__age = 589  # Atributo privado, no se puede acceder directamente desde fuera de la clase
       # Eliminamos el atributo full_name para evitar conflicto con el método

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def greating(self):
        return f"Hola, soy {self.full_name()} y tengo {self.age} años"
    def walk(self):
        print(f"{self.full_name()} está caminando")
    
    def full_name(self):
        return f"{self.name} {self.surname}"


pepe = Person(30)
print(f"\ntype(pepe): {type(pepe)}\n")
print(f"{pepe.name} {pepe.surname} tiene {pepe.age} años") 

pepe.name = "Pedro"
pepe.surname = "Fernandez"
pepe.age = 36
print(pepe.greating())  # Imprime el saludo personalizado

carlos = Person(25, "Carlos", "Lara")
carlos.greating = carlos.greating()
print(carlos.greating)  # Imprime el saludo personalizado
#print(f"{carlos.name} {carlos.surname} tiene {carlos.age} años")
carlos.walk()  # Llama al método walk de la clase Person

print(carlos.get_name())  # Imprime el nombre de Carlos usando el método get_name
print(f"{carlos.name} {carlos.surname} AND {carlos.get_name()} {carlos.get_surname()} que tiene {carlos.get_age()} años")  # Imprime el nombre completo de Carlos usando el método full_name
carlos.set_name("Juan")  # Intento de modificar el atributo privado __name directamente desde fuera de la clase
print(carlos.get_name())  # Imprime el nombre de Carlos usando el método get_name
#print(pepe.get_name())  # Imprime el nombre de Pepe usando el método get_name   
