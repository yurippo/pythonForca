# Sobre funções em Python, temos as seguintes afirmativas:
#
# 1 - Uma função é um bloco de código que pode ser guardado, para ser chamado
# assim que desejarmos, contanto que saibamos seu nome.
# Contudo, não é necessário
# sabermos a sua implementação.
#
# 2 - A seguinte declaração de função é válida:

# declara a função
def imprime_mensagem():
    print("Olá")

# chama a função
# imprime_mensagem()
# imprime_mensagem()
# imprime_mensagem()
# imprime_mensagem()

#ainda melhor :)

for x in range(4):
    imprime_mensagem()


# 3 - Em Python, a convenção é criarmos funções no padrão snake_case,
# isto é, cada palavra é iniciada com letras minúsculas e separadas por
# um underscore (_).

# Uma função, quando carregada, não tem o seu bloco de código executado automaticamente.
# A função é guardada em algum lugar, para mais tarde alguém chamá-la.
# Mas para que alguém a chame, execute-a, precisa saber seu nome.
# É por isso que a
# declaração de uma função é:
#
# def imprime_mensagem():
#     print("Olá")
#
# Quando a função é carregada, nada acontece, mas se chamamos a função pelo seu nome,
# executamos todo aquele código do bloco da função:

# def imprime_mensagem():
#     print("Olá")
#
# imprime_mensagem()

# def imprime_mensagem():
#     print("Olá")
#
# imprime_mensagem()
# imprime_mensagem()
# imprime_mensagem()
# imprime_mensagem()
#
# No exemplo acima, executaremos o bloco da função quatro vezes, porque a chamamos quatro vezes!
#
# Aliás, há uma convenção no nome de funções assim como nos nomes das variáveis, usamos o padrão
# snake_case. Sendo assim, toda função possui todas as letras minúsculas e cada palavra que forma
# o nome da função é separada por um underscore (o caractere _).






