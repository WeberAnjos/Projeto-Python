import dados

biblioteca = dados.carregar_do_arquivo()

def simular():
    print("\n--- Simulação por Período Fixo ---")
    v_inicial = float(input("Valor Inicial: "))
    aporte = float(input("Aporte Mensal: "))
    taxa_input = float(input("Taxa de juros mensal (em %): "))
    meses = int(input("Quantidade de Meses: "))

    taxa = taxa_input / 100
    saldo = v_inicial
    
    for i in range(1, meses + 1):
        saldo = saldo + (saldo * taxa) + aporte
    
    print(f"Resultado final: R$ {round(saldo, 2)}")

    biblioteca.append({
        "valorInicial": v_inicial,
        "aporte": aporte,
        "taxa": taxa_input,
        "meses": meses,
        "final": round(saldo, 2)
    })

def meta():
    print("\n--- Cálculo de Meta Financeira ---")
    v_inicial = float(input("Valor Inicial: "))
    aporte = float(input("Aporte Mensal: "))
    taxa_input = float(input("Taxa de juros (em %): "))
    v_final_desejado = float(input("Valor Final desejado: "))

    taxa = taxa_input / 100
    saldo = v_inicial
    meses = 0

    while saldo < v_final_desejado:
        saldo = saldo + (saldo * taxa) + aporte
        meses += 1
    
    print(f"Levará {meses} meses para atingir a meta.")

    biblioteca.append({
        "valorInicial": v_inicial,
        "aporte": aporte,
        "taxa": taxa_input,
        "meses": meses,
        "final": round(saldo, 2)
    })

def encerrar_e_salvar(nome_arquivo):
    dados.salvar_no_arquivo(biblioteca, nome_arquivo)