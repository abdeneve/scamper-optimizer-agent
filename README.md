# SCAMPER Optimizer Agent

O **SCAMPER Optimizer Agent** é um meta-agente estratégico especializado em reengenharia de processos. Utilizando a metodologia SCAMPER (Substituir, Combinar, Adaptar, Modificar, Propor outro uso, Eliminar, Reverter) e inteligência artificial generativa através do LangGraph e LangChain (com o Google Gemini 2.5), este agente analisa fluxos de trabalho existentes abordados por um relatório de auditoria e propõe otimizações estruturais para aumentar a eficiência, o paralelismo e a automação.

## 🚀 Funcionalidades

- **Leitura Automática de Entradas:** Lê um diagrama de processo inicial e um relatório de auditoria detalhando pontos de atrito (gargalos e falhas manuais).
- **Análise com Metodologia SCAMPER:** Analisa o fluxo original aplicando táticas de reengenharia sistêmica (destrói e remonta), visando inovação e não apenas automação simples.
- **Geração de Novo Diagrama Otimizado:** Produz como saída um relatório reflexivo com as justificativas das mudanças e um novo diagrama renderizado nativamente em formato Markdown com código `mermaid`.

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/):** Linguagem principal do projeto (>=3.12).
- **[LangChain](https://www.langchain.com/) / [LangGraph](https://langchain-ai.github.io/langgraph/):** Utilizados para criar o fluxo de processamento baseado em grafos de estado estruturados e orquestração de LLMs.
- **[Google Generative AI (Gemini)](https://aistudio.google.com/):** Modelo `gemini-2.5-flash` processado via `langchain-google-genai`.

## 📁 Estrutura do Projeto

```text
scamper-optimizer-agent/
├── .env                  # Variáveis de ambiente (necessário criar e adicionar GOOGLE_API_KEY)
├── input/
│   ├── diagrama-input.md # Diagrama Mermaid com o fluxo atual
│   └── report-input.md   # Relatório com os gargalos apontados pela auditoria
├── main.py               # Grafo LangGraph e lógica de execução do agente
└── output/
    └── diagrama-output.md # Novo relatório e diagrama de processo aprimorado
```

## ⚙️ Instalação e Configuração

1. Certifique-se de ter o Python (>=3.12) instalado em seu sistema.
2. Clone este repositório para o seu ambiente local.
3. Considerando que o projeto utiliza [uv](https://docs.astral.sh/uv/) como gerenciador de pacotes, instale as dependências:

```bash
uv sync
```

*(Caso não possua o `uv` instalado, pode utilizar o pip padrão: `pip install -e .`)*

4. Crie um arquivo `.env` na raiz do projeto contendo a sua chave do Google Gemini:

```env
GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
```

## 🧠 Como Utilizar

1. Preencha adequadamente os arquivos na pasta `input/`:
   - `input/diagrama-input.md`: Insira o código Mermaid correspondente ao processo original.
   - `input/report-input.md`: Cole o relatório de auditoria com os pontos de lentidão, fricção e erros identificados.
2. Execute o agente estruturado LangGraph:

```bash
python main.py
```

3. Após a execução ser concluída com sucesso, verifique a pasta `output/` e abra o arquivo `diagrama-output.md` para visualizar as resoluções apontadas pelo modelo, bem como a nova arquitetura do processo sugerida!
