graph TD
    %% Estilos de Nós
    classDef default fill:#1E1E1E,stroke:#333,stroke-width:2px,color:#fff;
    classDef bottleneck fill:#FF3333,stroke:#990000,stroke-width:3px,color:#fff,font-weight:bold;
    classDef agent_solution fill:#00CC66,stroke:#006633,stroke-width:2px,color:#fff,stroke-dasharray: 5 5;

    %% Fluxo Inicial
    A[Paciente envia mensagem de tentativa de agendamento por WhatsApp/IG] --> B{Recepcionista Disponível?}
    
    %% Gargalo 1
    B -- NÃO --> C1[Espera horas por resposta]
    class C1 bottleneck
    B -- SIM --> C2[Recepcionista lê a mensagem]

    %% Gargalo 2
    C2 --> D[Solicitação manual de dados: Nome, Data, Convênio]
    D --> E[Paciente envia áudios ou fotos borradas]
    E --> F[Perda de contexto / Transcrição manual para o CRM]
    class F bottleneck

    %% Fase de Validação e Agendamento
    F --> G[Recepcionista verifica agenda de médicos em software Legado]
    G --> H{Tem vaga?}
    H -- NÃO --> I[Propõe nova data manualmente]
    H -- SIM --> J[Bloqueia horário]

    %% Gargalo 3
    J --> K[Preenchimento manual de pré-condições da seguradora]
    class K bottleneck

    K --> L[Consulta Confirmada]
    L --> M[Envio manual de lembrete 24h antes]

    %% Notas de Solução Agêntica
    C1 -.->|Agente Data Miner: Resposta 24/7 e extração JSON| Solution1((Solução IA))
    F -.->|Processamento Semântico Multimodal| Solution1
    K -.->|Action Node: API direta com Seguradora| Solution1
    
    class Solution1 agent_solution