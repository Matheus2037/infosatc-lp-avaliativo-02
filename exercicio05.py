lista = ['arroz', 'macarrão', 'farofa', 'feijão', 'batata', 'linguiça', 'leite', 'cenoura', 'repolho', 'beterraba']

n1 = input("Qual item você deseja verificar se está na lista? ")

if n1 in lista:
    print("Sim, o item digitado está nessa lista.")
else:
    print("Não, este item não está nessa lista")