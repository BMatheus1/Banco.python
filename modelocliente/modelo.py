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

