#João criou a seguinte lista:

frutas = ["maçã", "banana", "laranja", "melancia"]

#Agora ele precisa criar uma nova lista com as mesmas frutas,
# mas tudo escrito em letras maiúsculas. Ele escreveu o laço abaixo:

lista = []

for fruta in frutas:
    lista.append(fruta.upper())

print(lista)

#O código funciona, mas será que você pode mostrar para ele como usar as List Comprehensions?
#Qual solução abaixo é relativa ao laço?

list_comprehension = [fruta.upper() for fruta in frutas]

print(list_comprehension)