import os


#           CLASSE CONTA BANCÁRIA E SUAS FUNÇÕES


class ContaBancaria:
    clientes = []

    def __init__(self, titular, saldo, cpf, profissao):
        self._titular = titular.strip().title()
        self._saldo = f'R${saldo:.2f}'
        self._cpf = self.formatar_cpf(cpf)
        self._profissao = profissao.strip().title()
        self._ativo = False
        
        ContaBancaria.clientes.append(self)

    @staticmethod
    def formatar_cpf(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    def __str__(self):
        return f'{self._titular} | {self._saldo} | {self._cpf} | {self._profissao}'
    
    @classmethod
    def listar_clientes(cls):
        print(
            f'{'Nome do cliente'.ljust(25)} | '
            f'{'Saldo da conta'.ljust(25)} | ' 
            f'{'CPF'.ljust(25)} | '
            f'{'profissão'.ljust(25)} | ' 
            f'{'Status'}'
            )
        

        for cliente in cls.clientes:
            print(f'{cliente._titular.ljust(25)} | {cliente._saldo.ljust(25)} | {cliente._cpf.ljust(25)} | {cliente._profissao.ljust(25)} | {cliente.ativo} | ')

        

    @classmethod
    def criar_conta(cls):
            
       while True:     
            try:
                titular = input('\nDigite o nome do titular da conta: ').title()
                saldo = float(input('Digite o saldo inicial da conta: '))
                cpf = input('Digite o cpf do titular da conta: ')
                profissao = input('Digite a profissão do titular da conta: ')
                cls(titular, saldo, cpf, profissao)
                
                print('\nNovo cliente adicionado com sucesso ✔️. ')
                break
            except ValueError:
                print('\nEntrada inválida. \n')

            

    @property

    def ativo(self):
        return 'Ativada ✔️' if self._ativo else 'Desativada ❌'

    def ativar_conta(self):
        self._ativo = not self._ativo


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


#           CLIENTES FIXOS


cliente1 = ContaBancaria('José da Silva', 5000, '02155075011', 'pedreiro')
cliente2 = ContaBancaria('Carlos Silva', 1200, '03166098066', 'operador de produção')
cliente3 = ContaBancaria('Mariana Oliveira', 3200, '14598732044', 'enfermeira')
cliente4 = ContaBancaria('Ricardo Pereira', 7800, '30945612088', 'analista de sistemas')
cliente5 = ContaBancaria('Fernanda Costa', 2100, '87530944012', 'secretária')
cliente6 = ContaBancaria('Bruno Matias', 950, '22490877055', 'vendedor')
cliente7 = ContaBancaria('Patrícia Santos', 4300, '98712456033', 'professora')
cliente8 = ContaBancaria('Leonardo Rocha', 5100, '66723389014', 'motorista')
cliente9 = ContaBancaria('Amanda Freitas', 1500, '80211945007', 'esteticista')
cliente10 = ContaBancaria('Thiago Menezes', 2750, '41988233090', 'designer gráfico')
cliente11 = ContaBancaria('Juliana Ramos', 3600, '58321099011', 'advogada')
cliente12 = ContaBancaria('Marcelo Nogueira', 8900, '91044312056', 'engenheiro civil')


if __name__ == '__main__':
    main()