#eliminar elementos de una lista 
#Metodo pop()  elimina el ultimo o un elemento indicando suposicion

letters = ["a", "b", "c", "d", "e"]
print(f"Lista : {letters}")
print(f"Elemento eliminiado: {letters.pop()}")
print(f"Lista: {letters}")

letters = ["a", "b", "c", "d", "e"]
print(f"\nLista : {letters}")
print(f"Elemento eliminiado en la posicion 2: {letters.pop(2)}")
print(f"Lista: {letters}")

letters = ["a", "b", "c", "d", "e"]
print(f"\nLista : {letters}")
print(f"Elemento eliminiado en la posicion 0: {letters.pop(0)}")
print(f"Lista: {letters}")

letters = ["a", "b", "c", "d", "e"]
print(f"\nLista : {letters}")
print(f"Elemento eliminiado en la posicion -2: {letters.pop(-2)}")
print(f"Lista: {letters}")

