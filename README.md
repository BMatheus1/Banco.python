🏦 Sistema Bancário em Python

Este é um projeto didático desenvolvido para treinar Programação Orientada a Objetos (POO) em Python, utilizando menus interativos no terminal.
A aplicação simula um sistema simples de gerenciamento de contas bancárias.

✨ Funcionalidades do Sistema

✔ Cadastro de clientes

Nome formatado automaticamente

Saldo inicial

CPF com formatação automática (000.000.000-00)

Profissão

Status da conta (ativada/desativada)

✔ Listagem de clientes cadastrados

Mostra nome, saldo, CPF, profissão e status

Tabela formatada no terminal

✔ Ativação ou desativação da conta

Busca feita pelo CPF (independente de como o usuário digitar)

Atualiza o status da conta entre "Ativada ✔️" e "Desativada ❌"

✔ Menu interativo

Navegação simples e limpa

Opções intuitivas

Retorno ao menu inicial ou encerramento do sistema

🧠 Recursos técnicos utilizados

Este projeto foi desenvolvido aplicando conceitos fundamentais de POO e boas práticas em Python, incluindo:

Classes e Objetos

Atributos protegidos

Métodos de instância

@staticmethod

@classmethod

Propriedades (@property)

Validação de entrada

Limpeza e formatação de strings

Organizações em módulos

Estrutura de menu com repetições (while True)

Interface textual no terminal

🔧 Melhorias Implementadas em Relação à Versão Original

A primeira versão do código trabalhava apenas com:

Nome do cliente

Saldo

Status da conta

A versão atual evoluiu bastante e agora inclui:

🔹 Novos campos no cadastro

CPF (com formatação automática)

Profissão

Formatação e padronização automática de nomes

🔹 Busca de cliente mais robusta

Busca por CPF

Aceita CPF com ou sem pontos, traços ou espaços

🔹 Tabela mais organizada

Colunas alinhadas

Exibição clara e legível dos dados

🔹 Menu reestruturado

Fluxo corrigido

Opção de retornar ou sair

Tela limpa a cada operação

📌 Objetivo do Projeto

Este projeto foi criado com o objetivo de:

Praticar conceitos de POO

Aprender boas práticas de organização de código

Criar menus dinâmicos no terminal

Trabalhar com validação e formatação de dados

Desenvolver uma lógica de fluxo contínuo em sistemas

Ideal para iniciantes que desejam fortalecer fundamentos de Python.

▶️ Como executar

No terminal:

python banco.py


Certifique-se de estar na pasta correta do projeto.

📚 Próximos passos (possíveis melhorias)

Implementar opção de exclusão de clientes

Sistema de depósito e saque

Geração de extrato completo

Persistência em arquivo (JSON)

Uso de IDs únicos por conta

Interface visual utilizando Tkinter ou PyQt
