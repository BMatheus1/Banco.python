import os

from modelocliente.modelo import ContaBancaria  

from clientes import clientesall

#           FUNÇÕES GERAIS


def main():
    escolher_opcao()

def limpar_tela():
    os.system('cls')

def mostrar_titulo():
    print(''' 
╔═══╗───╔╗──────────╔╗
║╔═╗║──╔╝╚╗─────────║║
║╚══╦╦═╩╗╔╬══╦╗╔╦══╗║╚═╦══╦═╗╔══╦══╦═╦╦══╗
╚══╗╠╣══╣║║║═╣╚╝║╔╗║║╔╗║╔╗║╔╗╣╔═╣╔╗║╔╬╣╔╗║
║╚═╝║╠══║╚╣║═╣║║║╔╗║║╚╝║╔╗║║║║╚═╣╔╗║║║║╚╝║
╚═══╩╩══╩═╩══╩╩╩╩╝╚╝╚══╩╝╚╩╝╚╩══╩╝╚╩╝╚╩══╝
''')

def voltar_menu_inicial():
    while True: 
        voltar = input('\nDeseja voltar ao menu inicial ? (s/n)').lower()  
        if voltar == 's':
            return
            
        elif voltar == 'n':
            limpar_tela()
            print('\nFinalizando sistema. \n')
            exit()
            
        else:
            print('\nOpção inválida. ')
        
def menu_inicial():

    print('1 - Adiconar cliente. ')
    print('2 - Listar clientes. ')
    print('3 - Ativar conta. ')
    print('4 - Sair. ')

def escolher_opcao():
    while True:
        limpar_tela()
        mostrar_titulo()
        menu_inicial()

        opcao_escolhida = input('\nDigite a opção desejada: ')
        if opcao_escolhida == '1':
            ContaBancaria.criar_conta()
            voltar_menu_inicial()

        elif opcao_escolhida == '2':
            ContaBancaria.listar_clientes()
            voltar_menu_inicial()

        elif opcao_escolhida == '3':
            
            cpf = input('\nDigite o CPF do cliente que deseja ativar a conta: ')
            cpf = ContaBancaria.formatar_cpf(cpf)

            encontrado = False
            
            for cliente in ContaBancaria.clientes:
                if cliente._cpf == cpf:
                    cliente.ativar_conta()
                    print(f'\nO status da conta do cliente {cliente._titular} CPF {cliente._cpf} foi alterada para {cliente.ativo}')
                    encontrado = True
                    
            
            if not encontrado:
                print('\nCliente não encontrado. ')
            
            voltar_menu_inicial()

        elif opcao_escolhida == '4':
            limpar_tela()
            print('\nFinalizando sistema. \n')
            break
        else:
            print('\nOpção inválida. ')





if __name__ == '__main__':
    main()