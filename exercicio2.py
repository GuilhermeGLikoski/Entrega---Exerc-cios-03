numero = float(input("Digite um número e revele seu peso: "))

if 10 <= numero <= 50:
    print("O número está entre 10 e 50 (inclusive).")
elif numero < 10:
    print("O número é menor que 10.")
else:
    print("O número é maior que 50.")
