# OPERADORES

# OPERADORES ARITMÉTICOS
# suma:             +
# resta:            -
# multiplicación:   *
# división:         /
# módulo:           %
# división entera:  // (floor division)
# exponente:        **

# operadores aplicados a números
print("OPERADORES ARITMÉTICOS APLICADOS A NÚMEROS")
print(3 + 4)    # 7
print(3 - 4)    # -1
print(3 * 4)    # 24
print(3 / 4)    # 0.75
print(10 % 3)   # 1
print(10 // 3)  # 3
print(2 ** 3)   # 8

# operadores aplicados a strings
print("OPERADORES ARITMÉTICOS APLICADOS A STRINGS")
print("hello " + "python")  # hello python
print("hello " + str(5))    # hello 5
print("hello " * 3)         # hello hello hello -> debe ser un entero, no funcionaría con floats
#print("hello " + 2)        # error
#print("hello " - "o")      # error

my_float = 2.5 * 2 # my_float = 5.0
print("hello " * int(my_float)) # hello hello hello hello hello



# OPERADORES COMPARATIVOS
# igualdad              ==
# desigualdad           !=
# mayor que             >
# menor que             <
# mayor o igual que     >=
# menor o igual que     <=

# operadores aplicados a números
print("OPERADORES COMPARATIVOS APLICADOS A NÚMEROS")
print(3 == 4)   # False
print(3 != 4)   # True
print(3 > 4)    # False
print(3 < 4)    # True
print(3 >= 4)   # False
print(3 <= 4)   # True
print(4 <= 4)   # True

# operadores aplicados a strings
print("OPERADORES COMPARATIVOS APLICADOS A STRINGS")
print("hello" == "python")  # False
print("hello" == "world")   # False
print("hello" == "hello")   # True
print("hello" != "python")  # True
print("hello" > "python")   # False
print("hello" < "python")   # True
print("hello" >= "python")  # False
print("hello" <= "python")  # True
# tiene en cuenta la ordenación de ASCII



# OPERADORES LÓGICOS
# and
# or
# not
# aquí los operadores lógicos se escriben como palabras, no símbolos

print("OPERADORES LÓGICOS")
print(3 < 4 and "hello" < "python")     # True
print(3 > 4 or "hello" < "python")      # True
print(3 > 4 and "hello" < "python")     # False
print(3 > 4 or "hello" > "python")      # False
print(not(3 > 4))                       # True