
numero1 = 23
numero2 = 56
numero3 = 72
numero4 = 1

frase = "ola , aqui é o dolynhoseu amiguinho."
palavra = "DOLLY"

media = (numero1 + numero2 + numero3 + numero4) / 4

quadrado_numero3 = numero3 ** 2

dobro_numero4 = 2 * numero4

quantidade_letras_palavra = len(palavra)


quantidade_espacos_frase = frase.count(" ")

primeiro_maior_que_segundo = numero1 > numero2

maior_numero = max(numero1, numero2, numero3, numero4)

print(f"Média aritmética: {media:.2f}")
print(f"Quadrado do número 3: {quadrado_numero3}")
print(f"Dobro do número 4: {dobro_numero4}")
print(f"Quantidade de letras na palavra: {quantidade_letras_palavra}")
print(f"Quantidade de espaços em branco na frase: {quantidade_espacos_frase}")
print(f"O primeiro número é maior que o segundo? {primeiro_maior_que_segundo}")
print(f"O maior número é: {maior_numero}")
