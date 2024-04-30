# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:04:36 2024

@author: 202102463661
"""

print("Olá", "mundo", sep="-") # Saída: Olá-mundo
print("Olá", "Python", end="!\n") # Saída: Olá Python!
print("30", "04", "2024", sep="/")
# Saída: nome; sobrenome; email (útil em CSVs)
print("GUILHERME", "HAIKAL", "email", sep="; ") 
print("Loading", end=" ")
print("[OK]")

nome = input("digite seu nome ")
print("Olá", nome) 

itens = input("digite itens separados por virgula: ")

itens = itens.split(',')

print("Itens:", itens) 

idade = int(input("Digite sua idade: "))
print("Daqui a cinco anos, você terá", idade + 5, "anos.")

altura = float(input("Digite sua altura em metros: "))
print("Sua altura é", altura, "metros.") 

def infinito():
    print("Digite números para adicionar à lista (digite 'done' para terminar):")
    numeros = []
    while True:
        entrada = input()
        if entrada.lower() == 'done':
            break
        else:
            numeros.append(int(entrada))
    print("Números coletados:", numeros)
    
    
    
    
infinito()
    
    
    