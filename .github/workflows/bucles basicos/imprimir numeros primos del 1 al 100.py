def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

for i in range(2, 101):
    if es_primo(i):
        print(i)
