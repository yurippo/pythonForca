#inicializando uma lista de números pares

#O recurso List Comprehension também permite utilizar condições para o preenchimento da lista.
# Considere o objetivo de inicializar uma lista com os números pares a partir de uma lista de números inteiros qualquer,
# por exemplo, os números 1,3,4,5,7,8,9. Para descobrir se um número é par, usamos a condição numero%2 == 0, que verifica
# se o resto de uma divisão por 2 é zero. O código abaixo usa um loop para inicializar a lista de pares.

inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros: #for numero in inteiros second argument
    if numero % 2 == 0: #if numero % 2 == 0 third argument
        pares.append(numero) #numero first argument
print(pares)

pares = [numero for numero in inteiros if numero % 2 ==0]

print(pares)

#List Comprehension é um dos recursos mais legais da linguagem Python :)