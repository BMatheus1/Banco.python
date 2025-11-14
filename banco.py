import os

class ContaBancaria:
    clientes = []

    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = f'R${saldo:.2f}'
        self._ativo = False
        ContaBancaria.clientes.append(self)


    def __str__(self):
        return f'{self._titular} | {self._saldo}'
    
    @classmethod
    def listar_clientes(cls):
        print(f'{'Nome do cliente'.ljust(25)} | {'Saldo da conta'.ljust(25)} | {'Status'} ')
        for cliente in cls.clientes:
            print(f'{cliente._titular.ljust(25)} | {cliente._saldo.ljust(25)} | {cliente.ativo}')

        

    @classmethod
    def criar_conta(cls):
            
       while True:     
            try:
                titular = input('\nDigite o nome do titular da conta: ')
                saldo = float(input('Digite o saldo inicial da conta: '))
                cls(titular, saldo)
                
                print('\nNovo cliente adicionado com sucesso ✔️. ')
                break
            except ValueError:
                print('\nO saldo precisa ser um número. \n')

            

    @property

    def ativo(self):
        return 'Ativada ✔️' if self._ativo else 'Desativada ❌'

    def ativar_conta(self):
        self._ativo = not self._ativo

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
            
            nome = input('\nDigite o nome do cliente que deseja ativar a conta: ')
            encontrado = False
            
            for cliente in ContaBancaria.clientes:
                if cliente._titular == nome:
                    cliente.ativar_conta()
                    print(f'\nO status da conta do cliente {nome} foi alterada para {cliente.ativo}')
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


cliente1 = ContaBancaria('José da Silva', 5000)
cliente2 = ContaBancaria('Carlos Silva', 1200)



if __name__ == '__main__':
    main()