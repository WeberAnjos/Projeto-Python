import funcoes

def exibir_menu():
    while True:
        print("\n--- SISTEMA FINANCEIRO ---")
        print("1. Simulação por Período Fixo")
        print("2. Cálculo de Meta Financeira")
        print("3. Sair")
        
        opcao = input("\nEscolha: ")

        if opcao == "1":
            funcoes.simular()
        elif opcao == "2":
            funcoes.meta()
        elif opcao == "3":
            nome_arq = input("Digite o nome do arquivo para salvar os resultados: ")
            funcoes.encerrar_e_salvar(nome_arq)
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    exibir_menu()