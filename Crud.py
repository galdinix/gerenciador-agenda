from Utils import*
agenda = {}
def adicionar_contato(agenda):
    nome = receberNome()
    data_nas = receber_data_nascimento()
    email = receberEmail()
    telefone = receberTelefone()
    rua = receberRua()
    numero = receberNumero()
    complemento = receberComplemento()
    bairro = receberBairro()
    municipio = receberMunicipio()
    estado = receberEstado()
    cep = receberCep() 
    contato = {
        'Data de Nascimento': data_nas,
        'Emails': [email],
        'Telefones': [telefone],
        'Rua': rua,
        'Número': numero,
        'Complemento': complemento,
        'Bairro': bairro,
        'Município': municipio,
        'Estado': estado,
        'CEP': cep
    }
    agenda[nome] = contato
    
def atualizar_contato(agenda):
    if agenda == None:
        print('Não existe contato na agenda')
        return
    nome = verificar_nome_existe(agenda)
    if nome != None:
        data_nas = receber_data_nascimento()
        email = receberEmail()
        telefone = receberTelefone()
        rua = receberRua()
        numero = receberNumero()
        complemento = receberComplemento()
        bairro = receberBairro()
        municipio = receberMunicipio()
        estado = receberEstado()
        cep = receberCep()
        agenda[nome]['Data de Nascimento'] = data_nas
        agenda[nome]['Emails'] = email
        agenda[nome]['Telefones'] = [telefone]  
        agenda[nome]['Rua'] = rua
        agenda[nome]['Número'] = numero
        agenda[nome]['Complemento'] = complemento
        agenda[nome]['Bairro'] = bairro
        agenda[nome]['Município'] = municipio
        agenda[nome]['Estado'] = estado
        agenda[nome]['CEP'] = cep
        return
    print('contato não existe')
    
def excluir_contato(agenda):
    if agenda is None:
        print('Não existe contatos')
        return
    nome = verificar_nome_existe(agenda)
    if nome != None:
        del(agenda[nome])

def listar_contatos(agenda):
    if not agenda:  # Verifica se a agenda está vazia
        print('A agenda está vazia.')
        return
    print('Lista de Contatos:')
    for nome, info_contato in agenda.items():
        print(f'Nome: {nome}')
        for chave, valor in info_contato.items():
            print(f'  {chave}: {valor}')
        print()