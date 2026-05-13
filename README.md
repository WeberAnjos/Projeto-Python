💰 Sistema de Simulação Financeira em Python
Este é um projeto modular desenvolvido em Python para auxiliar no planeamento financeiro pessoal. O sistema permite realizar simulações de investimentos com juros compostos e calcular o tempo necessário para atingir metas financeiras específicas.

🚀 Funcionalidades
Simulação por Período Fixo: Calcula o saldo final acumulado com base num valor inicial, aportes mensais, taxa de juro e tempo determinado.

Cálculo de Meta Financeira: Identifica quantos meses são necessários para atingir um valor final desejado, considerando os rendimentos e aportes informados.

Gestão de Dados (CSV): O sistema salva automaticamente o histórico de simulações em arquivos .csv dentro de uma pasta organizada (/arquivos), permitindo a exportação dos dados para Excel ou outras ferramentas.

Persistência Automática: Ao iniciar, o programa tenta carregar simulações anteriores de uma biblioteca padrão.

📂 Estrutura do Projeto
O código foi construído seguindo princípios de separação de responsabilidades:

app.py: Interface de menu e fluxo de interação com o utilizador.

funcoes.py: Lógica de negócio e fórmulas matemáticas de juros compostos.

dados.py: Camada de persistência responsável pela manipulação de ficheiros e diretórios.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Bibliotecas Nativas: csv para manipulação de dados e os para gestão de pastas do sistema.
