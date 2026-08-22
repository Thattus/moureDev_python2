# Conditionals in Python
# # if, elif, else statements
# Comparison operators: ==, !=, <, >, <=, >=
# Logical operators: and, or, not
# Membership operators: in, not in
# Identity operators: is, is not
# Ternary operator: value_if_true if condition else value_if_false

my_condition = False  # Variable booleana para la condición
if my_condition:  # Verificar si my_condition es True
    print(f"if my_condition: {my_condition}")  # Imprimir si la condición es verdadera
else:  # Si la condición es falsa
    print(f"else my_condition: {my_condition}") # Imprimir si la condición es falsa

print("Fin del if_1\n")  # Imprimir al final del programa

my_condition = 5 * 2 == 10  # Evaluar una condición booleana
if my_condition:  # Verificar si my_condition es True
    print(f"if my_condition: {my_condition}")  # Imprimir si la condición es verdadera
else:  # Si la condición es falsa
    print(f"else my_condition: {my_condition}")  # Imprimir si la condición es falsa

print(f"Fin del if_2\n")  # Imprimir al final del programa

my_condition = 5 * 2 - 4
if my_condition >= 10 and my_condition < 20:  # Verificar si my_condition
    print(f"if my_condition >= 10 and my_condition < 20: {my_condition}")  # Imprimir si la condición es verdadera
elif my_condition < 10:  # Verificar si my_condition es menor que 10
    print(f"elif my_condition < 10 from if my_condition >= 10 and my_condition < 20: {my_condition}")  # Imprimir si la condición es verdadera
else:  # Si la condición es falsa
    print(f"else from elif my_condition < 10 from if my_condition >= 10 and my_condition < 20: {my_condition}")  # Imprimir si la condición es falsa

print(f"Fin del if_3\n")  # Imprimir al final del programa

my_string = "Saul"
if my_string:  # Verificar si my_string no está vacío
    print(f"my_string no está vacío: {my_string}")  # Imprimir si my_string no está vacío
else:  # Si my_string está vacío
    print(f"my_string está vacío: {my_string}")  # Imprimir si my_string está vacío

print(f"Fin del if_4")  # Imprimir al final del programa