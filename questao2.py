# Questão 2.4
print('Bem vindo a Loja da Roberta da Silva de Oliveira')

#tabela

tamanho = ["P", "M", "G"]

codigos = {"TR": [6.00, 10.00, 18.00],

          "ES": [7.00, 12.00, 21.00],

          "PR": [8.00, 14.00, 21.00]}

compra = []

#pedindo os dados

while True:

   qual_tamanho = input("Qual o tamanho do sorvete desejado? ")

   qual_sabor = input("Qual o código do sorvete desejado? ")

   if qual_tamanho in tamanho and qual_sabor in codigos:

       pedido = codigos[qual_sabor][tamanho.index(qual_tamanho)]

       compra.append(pedido)

       algo_mais = input ("Deseja pedir algo mais?"

                          "\nDigite S para sim ou N para não. ")

       if algo_mais == "S":

           continue

       else:

           break

   else:

       print("TAMANHO ou CÓDIGO inválido(s)")

       continue

print ("Valor total da compra:", "R$",sum(compra))