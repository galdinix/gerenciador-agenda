def isNomeValid(nome):
    return len(nome) >= 5

def isNumeroValid(numero):
    return numero.isdigit()

def isEstadoValid(estado):
    return len(estado) == 2

def isCepValid(cep):
    return len(cep) == 8 and cep.isdigit()

def isDataNascimentoValid(dia, mes, ano):
    return 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 9999

def isEmailValid(email):
    return '@' in email and '.' in email

def isTelefoneValid(telefone):
    return len(telefone) >= 8 and telefone.isdigit()

def isContatoValid(contato, agenda):
    if contato in agenda:
        return True
    return False

def isOpcValid(opcao):
    if opcao > 4 or opcao < 0:
        return False
    return True