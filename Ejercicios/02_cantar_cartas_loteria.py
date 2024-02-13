import random

# modulo SECRETS es para uso de aleatoriedad para usos en seguridad
baraja = list(range(1, 55))

for contador in range(6):
    carta = random.choice(baraja)

    baraja.remove(carta)

    print(f"Carta cantada: {carta}")
