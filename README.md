# README: Simulador CONEXIA B2B

## Descrição
Este projeto é um simulador para a análise e processamento de dados no contexto particular. Ele utiliza o framework **Streamlit** para criar uma interface interativa, permitindo que usuários carreguem e manipulem arquivos Excel, apliquem regras específicas aos dados e visualizem resultados detalhados.

---

## Funcionalidades

### Entrada de Dados:
- Permite que o usuário insira um **CNPJ** e carregue um arquivo **Excel**.

### Transformações de Dados:
- Limpeza e padronização de colunas.
- Aplicação de regras específicas para configuração de produtos e plataformas.
- Manipulação e agrupamento de dados por séries, segmentos e produtos.

### Integração:
- Combinação de dados de diversas fontes, como itens, séries e configurações específicas do cliente.

### Exportação:
- Geração de planilhas Excel com os resultados finais processados.

---

## Requisitos

### Versão do Python:
- **Python 3.8** ou superior

### Dependências:
- Streamlit
- Pandas
- Numpy
- OpenPyXL
- XlsxWriter
- IPython
- Datetime

---

## Como Executar

### Instale as dependências:
```bash
pip install streamlit pandas numpy openpyxl xlsxwriter ipython
