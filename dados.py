import csv
import os

PASTA = "arquivos"
CAMPOS = ["valorInicial", "aporte", "taxa", "meses", "final"]

def inicializar_diretorio():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

def salvar_no_arquivo(lista_dados, nome_arquivo):
    inicializar_diretorio()
    
    if not nome_arquivo.endswith(".csv"):
        nome_arquivo += ".csv"
    
    caminho_completo = os.path.join(PASTA, nome_arquivo)
    
    try:
        with open(caminho_completo, "w", encoding="utf-8", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(lista_dados)
        print(f"\nDados salvos com sucesso em: {caminho_completo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def carregar_do_arquivo():
    caminho_padrao = os.path.join(PASTA, "biblioteca.csv")
    if os.path.exists(caminho_padrao):
        biblioteca_aux = []
        with open(caminho_padrao, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                # Converte campos numéricos para evitar problemas em cálculos futuros
                for campo in CAMPOS:
                    if campo in linha and linha[campo]:
                        linha[campo] = float(linha[campo])
                biblioteca_aux.append(linha)
        return biblioteca_aux
    return []