"""
Crie um dicionário vazio semana = {} e o complete com uma chave para cada
dia da semana, tendo como seu valor uma lista com as aulas que você tem
nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).
"""

semana = {}
semana['Segunda-feira'] = ['Lógica da matemática', 'Fundamentos da matemática']
semana['Terça-feira'] = ['Fundamentos da informática', 'Fundamentos da matemática']
semana['Quarta-feira'] = ['Inovação e Startups', 'Inglês I']
semana['Quinta-feira'] = ['Lógica da programação']
semana['Sexta-feira'] = ['Lógica da programação']
for key,value in semana.items():
    print(f'{key} ---> {value}')