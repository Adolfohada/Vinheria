'''
Exercicio:
A vinheria Agnello e descreva com a idade se pode ou não beber e com escolhas de vinhos e os preços e o frete
'''

print("Seja bem vindo à Vinheria Agnello!!!")
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade < 18:
    print("Que feio !!!!! Exclamatio marks!!!")
else:
    endereco = input("Diga seu endereço : ")
    vinho1 = 'Chapinha'
    vinho2 = 'Sangue de Boi'
    vinho3 = 'Levanta Defunto'
    preco1 = 10
    preco2 = 20
    preco3 = 30
    frete = 10
    print(f"Esssa são as nossas opções de vinhos :\n{vinho1}: R${preco1:.2f}"
          f"\n{vinho2}: R${preco2:.2}\n{vinho3}:R${preco3:.2f}")
    escolha = input("Diga o nome do vinho de sua preferência: ")
    if escolha ==vinho1:
        preco = preco1
    elif escolha == vinho2:
        preco = preco2
    else:
        preco = preco3

    qtd = int(input(f"Quantas garrafas de {escolha} você vai levar?\n "))

    valor = qtd * preco
    if valor < 100:
        valor += frete
    else:
        print("Frete gratis")
        print(f" Você gastou R${valor:.2f} em {qtd} garrafas de {escolha} que serão entregues"
              f"em {endereco}")
