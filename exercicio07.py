lista_filmes = ['vingadores ultimato', 'star wars', 'as branquelas', 'vovó... zona']#Criando as 4 listas
print("lista filmes: " ,lista_filmes)
print("\n")
lista_jogos = ['genshin impact', 'the witcher 3', 'dying light', 'destiny']#Criando as 4 listas
print("lista jogos: " ,lista_jogos)
print("\n")
lista_livros = ['o ultimo desejo', 'a espada do destino', 'o sangue dos elfos', 'a torre da andorinha']#Criando as 4 listas
print("lista livros: " ,lista_livros)
print("\n")
lista_esportes = ['futebol', 'vôlei', 'basquete']#Criando as 4 listas
print("lista esportes: " ,lista_esportes)

print("\n")

lista_filmes.append("carros 2") #adicionando 2 itens nas listas
lista_filmes.append("o exterminador do futuro")#adicionando 2 itens nas listas
print("lista filme atualizada: " ,lista_filmes)
print("\n")
lista_jogos.append("minecraft")#adicionando 2 itens nas listas
lista_jogos.append("terraria")#adicionando 2 itens nas listas
print("lista jogos atualizada: " ,lista_jogos)
print("\n")
lista_livros.append("tempo do desprezo")#adicionando 2 itens nas listas
lista_livros.append("a dama do lago")#adicionando 2 itens nas listas
print("lista livros atualizada: " ,lista_livros)
print("\n")
lista_esportes.append("ginastica")#adicionando 2 itens nas listas
lista_esportes.append("salto com vara")#adicionando 2 itens nas listas
print("lista esportes atualizada: " ,lista_esportes)
print("\n")



lista_geral = [lista_filmes, lista_jogos, lista_livros, lista_esportes]#lista com todas as outras listas
print("lista geral atualizada: " ,lista_geral)
print("\n")


print("lista livros atualizada: " ,lista_livros[1])#mostrando algum item da lista livros
print("\n")


del lista_esportes[0] #removendo item da lista esporte
print("livros esportes atualizada: " ,lista_esportes)
print("\n")

lista_geral.append("lista_disciplina =['matematica', 'portugues', 'ingles', programação]")#criando uma nova lista disciplina na lista onde tem todas as outras
print("lista geral atualizada: ",lista_geral)