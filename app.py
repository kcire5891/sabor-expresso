import os

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def finalizar_app():
    os.system('clear')
    # s.system('clear') no mac
    print('Finalizando o app')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # print('Você escolheu a opção', opcao_escolhida)
        # print(f'Você escolheu a opção {opcao_escolhida}')
        # print(type(opcao_escolhida))
        # print(type(1))

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()

# def escolher_opcao_match():
#     opcao_escolhida = int(input('Escolha uma opção: '))
#     match opcao_escolhida:
#         case 1:
#             print('Adicionar restaurante')
#         case 2:
#             print('Listar restaurantes')
#         case 3:
#             print('Ativar restaurante')
#         case 4:
#             print('Finalizar app')
#         case _:
#             print('Opção inválida!')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    # escolher_opcao_match()

    
if __name__ == "__main__":
    main()