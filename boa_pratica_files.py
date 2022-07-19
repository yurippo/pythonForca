#É uma boa prática fecharmos o arquivo depois de utilizá-lo para escrita ou leitura,
# assim outros programas ou processos podem ter acesso ao arquivo e ele não fica preso
# apenas ao nosso script Python.

#Qual das funções é utilizada para fechar um arquivo que foi aberto desse jeito:

arquivo = open('nome.txt','w')

arquivo.close()