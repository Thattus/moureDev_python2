# Exceptions Handling in Python
# Exceptions are used to handle errors and other exceptional events in Python.
# They allow you to manage errors gracefully without crashing the program.

number1 = 5
number2 = 1
number2 = "1"

# try except

try:
    print(f"number1: {number1}, number2: {number2}, suma = {number1 + number2}")
    print("Suma realizada correctamente")
except:
    print(f"Error: No se puede sumar {number1} y {number2}")

# try except else finally
try:
    print(f"number1: {number1}, number2: {number2}, suma = {number1 + number2}")
    print("Suma realizada correctamente")
except:
    print(f"Error: No se puede sumar {number1} y {number2}")
else:
    print("Se ejecuta si no hay error")
finally:
    print("Se ejecuta siempre, haya o no error")


# Exceptions por type
try:
    print(f"number1: {number1}, number2: {number2}, suma = {number1 + number2}")
    print("Suma realizada correctamente")
except ValueError as error:
    print(f"Value Error: No se puede sumar {number1} y {number2} porque son de tipos diferentes. Detalles del error: {error}")
except TypeError as error:
    print(f"Type Error: No se puede sumar {number1} y {number2} porque son de tipos diferentes. Detalles del error: {error}")

# Captura de la información del error
try:
    print(f"number1: {number1}, number2: {number2}, suma = {number1 + number2}")
    print("Suma realizada correctamente")
except TypeError as error:
    print(f"Type Error: No se puede sumar {number1} y {number2} porque son de tipos diferentes. Detalles del error: {error}")
except Exception as error:
    print(f"Error: No se puede sumar {number1} y {number2}. Detalles del error: {error}")
