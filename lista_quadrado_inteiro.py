#Suponha que tenhamos uma lista com os seguintes inteiros:

inteiros = [1,3,4,5,7,8]

#Podemos preencher uma nova lista com o quadrado de cada número da lista anterior
# através do recurso List Comprehension. Considerando que, para calcular o quadrado de um número,
# fazemos x*x, qual seria o código para obter a lista de quadrados?

lista_quadrados = [ inteiro * inteiro for inteiro in inteiros]

print(lista_quadrados)



