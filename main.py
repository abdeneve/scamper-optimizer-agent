import os
from typing import TypedDict
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END

# Carregar variáveis de ambiente (como GOOGLE_API_KEY/GEMINI_API_KEY)
load_dotenv()

class OptimizerState(TypedDict):
    diagram_input: str
    report_input: str
    optimized_output: str

def read_inputs(state: OptimizerState):
    """Nó 1: Lê os arquivos de entrada."""
    diagram_path = os.path.join("input", "diagrama-input.md")
    report_path = os.path.join("input", "report-input.md")
    
    with open(diagram_path, "r", encoding="utf-8") as f:
        diagram = f.read()
        
    with open(report_path, "r", encoding="utf-8") as f:
        report = f.read()
        
    return {"diagram_input": diagram, "report_input": report}

def scamper_optimize(state: OptimizerState):
    """Nó 2: Gera a otimização usando a técnica SCAMPER e um LLM."""
    print(">> Analisando pontos de atrito usando LLM e metodologia SCAMPER...")
    
    # Utiliza-se o modelo gemini-2.5-flash
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", temperature=0.5)
    
    system_prompt = (
        "Você é o Agente SCAMPER Optimizer, um meta-agente estratégico e especialista em reengenharia de processos. "
        "Seu núcleo é um motor reflexivo que ingere fluxos de trabalho com suas correspondentes "
        "métricas de falhas ou gargalos e aplica iterativamente simulações baseadas na "
        "metodologia SCAMPER (Substituir, Combinar, Adaptar, Modificar, Propor outro uso, Eliminar, Reverter).\n\n"
        "O objetivo não é simplesmente automatizar a tarefa humana, mas 'destruir e remontar' o fluxo original, "
        "aproveitando paralelismo, integrações de API e agentes resolutivos de IA.\n"
        "A saída DEVE conter:\n"
        "1. Visão arquitetônica e descobertas do relatório.\n"
        "2. Loop de Raciocínio (como o SCAMPER foi aplicado passo a passo para atacar os problemas apontados no relatório).\n"
        "3. O novo diagrama otimizado renderizado como um bloco de código ```mermaid\ngraph TD...```.\n\n"
        "Responda integralmente em Português do Brasil (pt-BR)."
    )
    
    user_prompt = (
        "Abaixo é apresentado o GRAFO ORIGINAL do processo (Mermaid):\n"
        "{diagram}\n\n"
        "Abaixo é apresentado o RELATÓRIO DE AUDITORIA com os pontos de atrito:\n"
        "{report}\n\n"
        "Gere a reengenharia e o novo diagrama otimizado aplicando SCAMPER contextualizado para o cenário corporativo brasileiro."
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", user_prompt)
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "diagram": state["diagram_input"],
        "report": state["report_input"]
    })
    
    return {"optimized_output": response.content}

def write_output(state: OptimizerState):
    """Nó 3: Escreve o diagrama otimizado no sistema de arquivos."""
    print(">> Salvando relatório e diagrama resultante...")
    os.makedirs("output", exist_ok=True)
    out_path = os.path.join("output", "diagrama-output.md")
    
    # Dependendo da versão do LangChain/Gemini, response.content pode ser uma lista.
    content = state["optimized_output"]
    if isinstance(content, list):
        if content and isinstance(content[0], dict) and "text" in content[0]:
            content = "".join(item["text"] for item in content if "text" in item)
        else:
            content = "".join(str(c) for c in content)
    elif not isinstance(content, str):
        content = str(content)
            
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    return state

# ==========================================
# CONSTRUÇÃO DO GRAFO LANGGRAPH
# ==========================================
workflow = StateGraph(OptimizerState)

workflow.add_node("read", read_inputs)
workflow.add_node("optimize", scamper_optimize)
workflow.add_node("write", write_output)

workflow.set_entry_point("read")
workflow.add_edge("read", "optimize")
workflow.add_edge("optimize", "write")
workflow.add_edge("write", END)

app = workflow.compile()

def main():
    print("Iniciando Agente SCAMPER Optimizer...")
    try:
        # Invocamos o grafo passando o estado inicial
        result = app.invoke({
            "diagram_input": "",
            "report_input": "",
            "optimized_output": ""
        })
        print(f"Sucesso! Os resultados foram salvos em 'output/diagrama-output.md'")
    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()
