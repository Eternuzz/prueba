import random

print("Bienvenido al juego 'Adivina el número'!")
print("Tienes que adivinar un número entre 1 y 100.")
print("Tienes 5 oportunidades para adivinar el número correcto.")

number = random.randint(1, 100)
chances = 5

while chances > 0:
    guess = int(input("Adivina el número: "))

    if guess == number:
        print("¡Felicidades! Adivinaste el número correcto.")
        break
    elif guess < number:
        print("El número es más grande.")
    else:
        print("El número es más pequeño.")

    chances -= 1
    if chances == 0:
        print(f"Se acabaron tus oportunidades. El número correcto era {number}.")
