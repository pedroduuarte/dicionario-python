"""
Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi
lançado. Preencha 5 filmes e acesse os dados do dicionários.
"""

filmes = {}
filmes['Batman - O cavaleiro das trevas'] = {'Vilão' : 'Coringa', 'Ano' : 2008}
filmes['Vingadores -  Ultimato'] = {'Vilão' : 'Thanos' , 'Ano' : 2019}
filmes['Harry Potter - As relíquias da morte parte II'] = {'Vilão' : 'Voldemort' , 'Ano' : 2011}
filmes['Homem Aranha 2'] = {'Vilão' : 'Dr. Octopus' , 'Ano' :2004}
filmes['Vingadores - A Era de Ultron'] = {'Vilão' : 'Ulton' , 'Ano' : 2013}

for filme in filmes: 
    vilao = filmes[filme]['Vilão']
    ano = filmes[filme]['Ano']
    print(f'Filme: {filme} // Vilão do filme: {vilao} // Ano de lançamento: {ano}')