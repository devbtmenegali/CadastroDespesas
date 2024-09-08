import matplotlib.pyplot as plt

def apresentar_menu():
    print("CADASTRO DE DESPESAS")
    print("1 - LANÇAR")
    print("2 - RELATÓRIO")
    print("3 - SAIR")
    
    while True:
        try:
            menu = int(input("Digite o código: "))
            if menu == 1:
                return 1  
            elif menu == 2:
                return 2  
            elif menu == 3:
                return 3  
            else:
                print("Digite um código válido!")
        except ValueError:
            print("Digite um código válido!")

def cadastro_despesas():
    relacao_despesas = {}
    while True:
        descricao_despesa = input("Cadastro de despesa ou digite '0' para sair: ")
        if descricao_despesa == "0":
            break
        try:
            valor_despesa = float(input("Digite o valor gasto: "))
            relacao_despesas[descricao_despesa] = valor_despesa
        except ValueError:
            print("Valor inválido. Digite um número.")
    return relacao_despesas

def relatorio_grafico(relacao_despesas):
    
    print(relacao_despesas)
    soma_despesas = sum(relacao_despesas.values())
    
    x = list(relacao_despesas.keys())  # categorias (nomes das despesas)
    y = list(relacao_despesas.values())  # valores das despesas

    plt.bar (x,y)

    plt.title ("Relação de Despesas")
    plt.xlabel ("Despesas")
    plt.ylabel ("Valores R$")

    plt.show()

    return soma_despesas

def main():
    relacao_despesas = {}
    while True:
        opcao = apresentar_menu()
        if opcao == 1:
            relacao_despesas = cadastro_despesas()
        elif opcao == 2:
            if relacao_despesas:
                soma_despesas = relatorio_grafico(relacao_despesas)
                print("A soma dos valores no dicionário é:", soma_despesas)
            else:
                print("Não há despesas cadastradas.")
        elif opcao == 3:
            print("Obrigado por utilizar o sistema")
            break

if __name__ == "__main__":
    main()
