import json

data = json.load(open("C:/Users/larag/OneDrive/Área de Trabalho/Trilha/movies_and_series.json"))
x = data.get("data", "")

# 1
filme = x.get("movies", "")

lista_filmes = []
titulo_filme = ""
for i in range(len(filme)):
    lista_filmes.append(filme[i].get("title", ""))

for element in lista_filmes:
    titulo_filme += element

# 2
serie = x.get("series", "")

lista_series = []
titulo_serie = ""
for i in range(len(serie)):
    lista_series.append(serie[i].get("title", ""))

for element in lista_series:
    titulo_serie += element

# 3
nota_filme = filme[0].get("rating", "")
nota_serie = serie[0].get("rating", "")

if(nota_filme > nota_serie):
    notao = titulo_filme + " - " + str(nota_filme)
else:
    notao = titulo_serie + " - " + str(nota_serie)

# 4
gen_filme = filme[0].get("genres", "")
gen_serie = serie[0].get("genres", "")

generos = []
generos_geral = ""
for element in gen_filme:
    generos.append(element)

for element in gen_serie:
    generos.append(element)

generos = list(set(generos))
for element in generos:
    generos_geral = generos_geral + element + ", "

# 5
total = [titulo_filme, titulo_serie]

def anteriores(midia, anterior):
    elenco = midia[0].get("cast", "")
    for i in range(len(elenco)):
        ant = elenco[i].get(anterior, "")
        ant = ant[0].get("title", "")
        total.append(ant)

anteriores(filme, "previousMovies")
anteriores(serie, "previousShows")

premios_f = filme[0].get("awards", "")
nomeados_f = premios_f[0].get("nominees", "")

for element in nomeados_f:
    total.append(element)
    
premios_s = serie[0].get("awards", "")
nomeados_s = premios_s[0].get("nominees", "")

for element in nomeados_s:
    total.append(element)

total = str(len(total))

# 6
lista_plataformas = []
plataformas = ""

serviços_f = filme[0].get("streaming", "")
serviços_s = serie[0].get("streaming", "")

for chave in serviços_f:
    lista_plataformas.append(chave)

for chave in serviços_s:
    lista_plataformas.append(chave)

lista_plataformas = list(set(lista_plataformas))
for element in lista_plataformas:
    plataformas = plataformas + element +", "

# 7
lista_4k = []
filtro4k = ""
def resolucao(midia, titulo):
    serviços = midia[0].get("streaming", "")
    netflix = serviços.get("Netflix", "")
    resolucao = netflix.get("resolution", "")
    if "4K" in resolucao:
        lista_4k.append(titulo)

resolucao(filme, titulo_filme)
resolucao(serie, titulo_serie)

for element in lista_4k:
    filtro4k += element + ", "

# 8
serviços = filme[0].get("streaming", "")
plataforma = serviços.get("Netflix", "")
bool_plataforma = plataforma.get("available", "")
if bool_plataforma == True:
    disponivel = "\n   " + titulo_filme + ": " + "Netflix - " + plataforma.get("url", "")

serviços = filme[0].get("streaming", "")
plataforma = serviços.get("Amazon Prime", "")
bool_plataforma = plataforma.get("available", "")
if bool_plataforma == True:
    disponivel += "\n   " + titulo_filme + ": " + "Amazon Prime - " + plataforma.get("url", "")

# 9
atores = []
def procurarAtor(elenco):
    for i in range(len(elenco)):
        atores.append(elenco[i].get("actor", ""))
    return atores

procurarAtor(filme[0].get("cast", ""))
procurarAtor(serie[0].get("cast", ""))

personagens = []
def procurarPersonagem(elenco):
    for i in range(len(elenco)):
        personagens.append(elenco[i].get("character", ""))
    return personagens

procurarPersonagem(filme[0].get("cast", ""))
procurarPersonagem(serie[0].get("cast", ""))

def credito(pessoa, personagem):
    credito = "\n   " + pessoa + " - " + personagem 
    return credito

papeis = ""
for i in range(len(atores)):
    papeis += credito(atores[i], personagens[i])

# 10
salarios = {}

def granaAtor(elenco):
    for i in range(len(elenco)):
        salario_ator = elenco[i].get("salary", "")
        ator = elenco[i].get("actor", "")
        salarios[ator] = salario_ator

granaAtor(filme[0].get("cast", ""))
granaAtor(serie[0].get("cast", ""))

maior_salario = []
for valor in salarios.values():
    maior_salario.append(valor)

maior_salario = max(maior_salario)

maior_ator = ""
for i, j in salarios.items():
    if j == maior_salario:
        maior_ator = i

salarios = str(maior_ator) + " com o salario de " + str(maior_salario)

# 11
locais = ""
for i in range(len(filme)):
    produçao_f = filme[i].get("production", "")
    filme_locais = produçao_f.get("filmingLocations", "")

for element in filme_locais:
    locais = locais + "\n   " + element

# 12
for i in range(len(filme)):
    diretores_f = filme[i].get("directors", "")
    for element in diretores_f:
        diretor = element
diretor = titulo_filme + " -> " + diretor 

# 13
lucros_f = []
for i in range(len(filme)):
    produçao = filme[i].get("production", "")
    caixa = produçao.get("boxOffice", "")
    lucros_f.append(caixa.get("revenue", ""))

maior_lucro = ""

for i in range(len(filme)):
    produçao = filme[i].get("production", "")
    caixa = produçao.get("boxOffice", "")
    if (caixa.get("revenue", "")) == max(lucros_f):
        maior_lucro += lista_filmes[i]

# 14
media_lucros = str(sum(lucros_f)/len(lista_filmes))

#15
for i in range(len(filme)):
    produçao = filme[0].get("production", "")
    caixa = produçao.get("boxOffice", "")
    ticket = caixa.get("ticketSales", "")
    domestico = ticket.get("domestic", "")
    internacional = ticket.get("international", "")

tickets = f"\n   Domestico - {domestico}\n   Internacional - {internacional}"

# 16
awards = ""

for i in range(len(premios_f)):
    nomeados = ""

    nome = premios_f[i].get("award", "")
    ano = premios_f[i].get("year", "")
    categoria = premios_f[i].get("category", "")
    lista_nomeados = premios_f[i].get("nominees", "")

    for element in lista_nomeados:
        nomeados += element + ", "
    nomeados = nomeados[:-2]

    awards += f"\n   {nome} = {categoria}, ano: {ano}.\n   Filmes indicados: {nomeados}.\n"

for i in range(len(premios_s)):
    nomeados = ""

    nome = premios_s[i].get("award", "")
    ano = premios_s[i].get("year", "")
    categoria = premios_s[i].get("category", "")
    lista_nomeados = premios_s[i].get("nominees", "")

    for element in lista_nomeados:
        nomeados += element + ", "
    nomeados = nomeados[:-2]

    awards += f"\n   {nome} = {categoria}, ano: {ano}.\n   Series indicados: {nomeados}."

# 17 
ganhadores = ""

for i in range(len(filme)):
    ganhou = premios_f[0].get("won", "")
    if ganhou == True:
        ganhadores += str(filme[i].get("title", ""))

for i in range(len(serie)):
    ganhou = premios_s[0].get("won", "")
    if ganhou == True:
        ganhadores += str(serie[i].get("title", ""))

# 18
indicados = ""

ano = premios_f[0].get("year", "")
categoria = premios_f[0].get("category", "")
if categoria == "Best Picture":
    indicados += str(ano) + " -> " + titulo_filme

# 19
votos = {}

def comment(midia):
    reviews = midia[0].get("reviews", "")

    for i in range(len(reviews)):
        detalhes = reviews[i].get("details", "")
        comentario = reviews[i].get("comment", "")
        votos[comentario] = (detalhes.get("helpfulVotes", ""))

comment(filme)
comment(serie)

mais_votos = max(votos.values())

for i, j in votos.items():
    if j == mais_votos:
        comment = i

# 20 
media_nota = str(nota_filme/len(filme))

# 21 
lista_avaliacoes = []
avaliacoes = ""

def data(midia):
    reviews = midia[0].get("reviews", "")
    

    for i in range(len(reviews)):
        comentario = reviews[i].get("comment", "")
        detalhes = reviews[i].get("details", "")
        data = detalhes.get("date", "")
        lista_data = data.split("-")
        data = int(lista_data[0])
        if data < 2022:
            lista_avaliacoes.append(comentario)
 
data(filme)
data(serie)

for element in lista_avaliacoes:
    avaliacoes += element

# Arquivo txt

def divisoria():
    arquivo.write("\n\n")
    arquivo.write("="*44)
    arquivo.write("\n")

def intro():
    arquivo.write("-"*20)
    arquivo.write(" Mini Projeto por Lara Gomes ")
    arquivo.write("-"*20)

with open ("C:/Users/larag/OneDrive/Área de Trabalho/Trilha/miniProjeto.txt", 'w') as arquivo:
    intro()
    arquivo.write("\n\n1. Todos os titulos de filmes:\n   ")
    arquivo.write(titulo_filme)
    divisoria()
    arquivo.write("\n2. Todos os titulos de series:\n   ")
    arquivo.write(titulo_serie)
    divisoria()    
    arquivo.write("\n3. Recuperar o filme/serie com maior nota (rating):\n   ")
    arquivo.write(notao)
    divisoria()
    arquivo.write("\n4. Listar os generos de todos os filmes e series:\n   ")
    arquivo.write(generos_geral[:-2])
    divisoria()
    arquivo.write("\n5. Obter o numero total de filmes e series:\n   ")
    arquivo.write(total)
    divisoria()
    arquivo.write("\n6. Listar todas as plataformas de streaming disponiveis:\n   ")
    arquivo.write(plataformas[:-2])
    divisoria()
    arquivo.write("\n7. Filtrar os filmes/séries disponíveis em 4K no Netflix:\n   ")
    arquivo.write(filtro4k[:-2])
    divisoria()
    arquivo.write("\n8. Identificar plataformas onde um filme específico está disponível:\n   ")
    arquivo.write(disponivel)
    divisoria()
    arquivo.write("\n9. Listar todos os atores e os personagens que interpretam:\n")
    arquivo.write(papeis)
    divisoria()
    arquivo.write("\n10. Obter o ator com maior salário em um filme ou série:\n   ")
    arquivo.write(salarios)
    divisoria()
    arquivo.write("\n11. Listar todas as localizações de filmagem dos filmes:\n")
    arquivo.write(locais)
    divisoria()
    arquivo.write("\n12. Listar os diretores de cada filme:\n   ")
    arquivo.write(diretor)
    divisoria()
    arquivo.write("\n13. Obter o filme com maior receita na bilheteria (revenue):\n   ")
    arquivo.write(maior_lucro)
    divisoria()
    arquivo.write("\n14. Calcular o lucro medio dos filmes:\n   ")
    arquivo.write(media_lucros[:-2])
    divisoria()
    arquivo.write("\n15. Obter a distribuiçao de vendas de ingressos por regiao:\n   ")
    arquivo.write(tickets)
    divisoria()
    arquivo.write("\n16. Listar todos os premios e categorias de cada filme/serie:\n   ")
    arquivo.write(awards)
    divisoria()
    arquivo.write("\n17. Identificar filmes/series que ganharam premios:\n   ")
    arquivo.write(ganhadores)
    divisoria()
    arquivo.write("\n18. Listar os indicados ao premio de 'Melhor Filme' de cada ano:\n   ")
    arquivo.write(indicados)
    divisoria()
    arquivo.write("\n19. Obter o comentario com maior numero de votos uteis:\n   ")
    arquivo.write(comment)
    divisoria()
    arquivo.write("\n20. Calcular a nota media dos filmes:\n   ")
    arquivo.write(media_nota)
    divisoria()
    arquivo.write("\n20. Filtrar todas as avaliaçoes feitas antes de 2022:\n   ")
    arquivo.write(avaliacoes)