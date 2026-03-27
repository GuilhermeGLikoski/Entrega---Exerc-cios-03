print("Onde no espaço você está?")
x = float(input("Coordenada X: "))
y = float(input("Coordenada Y: "))

# O domínio vai de (0,0) a (10,10)
if 0 < x < 10 and 0 < y < 10:
    print("Dentro do quadrado")
elif (0 <= x <= 10 and (y == 0 or y == 10)) or (0 <= y <= 10 and (x == 0 or x == 10)):
    print("Na fronteira")
else:
    print("Fora do quadrado")
