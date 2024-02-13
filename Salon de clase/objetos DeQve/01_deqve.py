# D-ouble
# E-nded
# Queve
# cola de dos lados
import collections

cola = collections.deque()  #

for valor in range(5):
    nuevo_valor = input("Dame el nuevo valor:")
    cola.append(nuevo_valor)
print(cola)
# while cola:
#     print(cola.popleft())

# para eliminar valores de un objeto "deque" y que este se comporte como una cola debo utilizar su metodo "popleft()"
