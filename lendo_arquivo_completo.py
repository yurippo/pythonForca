#Dado um arquivo como o seguinte: frutas.txt
"""
Banana
Maçã
Pera
Uva
Jamelão
"""

#Que foi aberto deste modo:

arquivo = open('frutas.txt','r')

#E quando executamos os comandos:

linha = arquivo.readline()
print(linha)

linha = arquivo.readline()
print(linha)
arquivo.close()
#Banana
#Maçã

#Mas quando abrimos o arquivo e usamos os comandos:

arquivo = open('frutas.txt','r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

arquivo = open('frutas.txt','r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

"""
A primeira vez é exibida corretamente o conteudo,
porém na segunda não é exibido nada. Porque?

"""
# Pois o comando read() lê o arquivo inteiro de uma vez,
# colocando o ponteiro de leitura no final do mesmo.
# Se chamarmos a função read() novamente, como o ponteiro de
# leitura está no final, nada será lido.

# Se desejarmos ler o arquivo novamente, devemos fechá-lo com o comando
# .close(), reabri-lo com o comando .open() e ai sim conseguiremos lê-lo
# por inteiro novamente.