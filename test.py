import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("🎮 Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("🔼 O número é maior!")
    elif tentativa > numero_secreto:
        print("🔽 O número é menor!")
    else:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
        break 
