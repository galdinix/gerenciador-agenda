from Validations import*

def receberNome():
    while True:
        try: 
            nome = input('Informe seu nome: ')
            if isNomeValid(nome):
                return nome
            print('Informe um nome válido (com pelo menos 5 caracteres)')
        except Exception:
            print('Erro')

def receberRua():
    while True:
        try: 
            rua = input('Informe a rua: ')
            return rua
        except Exception:
            print('Erro')


def receberNumero():
    while True:
        try: 
            numero = input('Informe o número: ')
            if isNumeroValid(numero):
                return numero
            print('Informe um número válido')
        except Exception:
            print('Erro')

def receberComplemento():
    while True:
        try: 
            complemento = input('Informe o complemento (opcional): ')
            return complemento
        except Exception:
            print('Erro')

def receberBairro():
    while True:
        try: 
            bairro = input('Informe o bairro: ')
            return bairro
        except Exception:
            print('Erro')

def receberMunicipio():
    while True:
        try: 
            municipio = input('Informe o município: ')
            return municipio
        except Exception:
            print('Erro')

def receberEstado():
    while True:
        try: 
            estado = input('Informe o estado: ')
            if isEstadoValid(estado):
                return estado
            print('Informe um estado válido com 2 caracteres')
        except Exception:
            print('Erro')

def receberCep():
    while True:
        try: 
            cep = input('Informe o CEP: ')
            if isCepValid(cep):
                return cep
            print('Informe um CEP válido com 8 dígitos')
        except Exception:
            print('Erro')

def receber_data_nascimento():
    while True:
        try: 
            data_nas = input('Informe a data de nascimento (DD/MM/AAAA): ')
            dia, mes, ano = map(int, data_nas.split('/'))
            if isDataNascimentoValid(dia, mes, ano):
                return data_nas
            print('Informe uma data de nascimento válida no formato DD/MM/AAAA')
        except Exception:
            print('Erro')

def receberEmail():
    while True:
        try: 
            email = input('Informe o e-mail: ')
            if isEmailValid(email):
                return email
            print('Informe um e-mail válido')
        except Exception:
            print('Erro')

def receberTelefone():
    while True:
        try: 
            telefone = input('Informe o telefone: ')
            if isTelefoneValid(telefone):
                return telefone
            print('Informe um telefone válido com pelo menos 8 dígitos')
        except Exception:
            print('Erro')

def  receberOpcMenuPrincipal():
    while True:
        try:
            opcao = int(input("Entre com a opção: "))
            if isOpcValid(opcao):
                return  opcao
            print('Infome um número de 0 a 4')
        except ValueError:
            print('Erro, tente novamente')

def verificar_nome_existe(agenda):
    nome = input('Informe o nome do contato a ser alterado ou excluido: ')
    if nome in agenda:
        return nome
    return 

