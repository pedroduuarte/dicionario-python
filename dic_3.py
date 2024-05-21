"""
Escreva um programa para armazenar uma agenda de telefones em um
dicionário. Cada pessoa pode ter um ou mais telefones e a chave do
dicionário é o nome da pessoa. Seu programa deve conter um menu onde
dependendo da entrada do usuário, será possível:
incluirNovoNome – acrescenta um novo nome na agenda, com um ou mais telefones.
incluirTelefone – acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo.
excluirTelefone – exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
excluirNome – exclui uma pessoa da agenda.
consultarTelefone – retorna os telefones de uma pessoa na agenda.
"""

agenda ={}
while True:
    print('OPÇÕES: incluirNovoNome // incluirTelefone // excluirTelefone // excluirNome // consultarTelefone // sair')
    print('=-'*53)
    opcao = (input('Digite aqui o que você deseja fazer: '))

    if opcao == 'incluirNovoNome': 
        nome = input('Digite o nome do contato: ')
        if nome not in agenda: 
            agenda[nome] = []
        else: print('O nome já existe na agenda!')
       
    elif opcao == 'incluirTelefone': 
        nome = input('Digite o nome do contato: ')
        if nome in agenda: 
            telefone = input('Contato já encontrado! Digite seu novo número: ')
            agenda[nome].append(telefone)
        if nome not in agenda: 
            opcao = input('O nome do contato não existe na agenda, deseja incluí-lo? [s/n] ')
            if opcao == 's': 
                telefone = input(f'Digite o número de {nome}: ')
                agenda[nome] = [telefone]

    elif opcao == 'excluirTelefone': 
        nome = input('Digite o nome do contato: ')
        if len(agenda[nome]) == 1: 
            del agenda[nome]
            print('Contato excluído com sucesso!')
        else: 
            telefone = input(f'Dgite qual telefone de {nome} que você deseja excluir: ')
            if telefone in agenda[nome]: 
                agenda[nome].remove(telefone)
                print(f'Telefone de {nome} excluído com sucesso!')
   
    elif opcao == 'excluirNome': 
        nome = input('Digite aqui o nome do contato que você deseja excluir: ')
        del agenda[nome]
        print('Contado excluído com sucesso!')
    
    elif opcao == 'consultarTelefone':
        nome = input('Digite o nome do contato que você deseja ver o(s) número(s): ')
        if nome in agenda: 
            print(f'Telefones de {nome}: {agenda[nome]}')
    elif opcao == 'sair': 
        print('Programa Encerrado!')
        break 
    else: print('Opção Não encontrada, tente novamente...')