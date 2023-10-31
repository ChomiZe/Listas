#instertar elementos en una lista
#Metodo insert() posicion exacta para agragar elemento

print('Agregando un elemento a la lista')
letters = ["a", "b", "c", "d"]
print(f"Lista: {letters}")

print("\nInsertando 'A' en posicion 0")
letters.insert(0, "A")
print(f"Lista: {letters}")

print("\nInsertando '♦' en posicion 2")
letters.insert(2, "♦")
print(f"Lista: {letters}")

print("\nInsertando 'z' en posicion 100")
letters.insert(100, "z")
print(f"Lista: {letters}")