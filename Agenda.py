from Utils import*
from Crud import*
from Menu import*
FIM = 0
exibirMenu()
opcao = receberOpcMenuPrincipal()
agenda={}
while (opcao != 0):
    match (opcao):
        case 1: adicionar_contato(agenda)
        case 2: atualizar_contato(agenda)
        case 3: excluir_contato(agenda)
        case 4: listar_contatos(agenda)
    exibirMenu()
    opcao = receberOpcMenuPrincipal()
        
