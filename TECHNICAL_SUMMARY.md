# Sumário Técnico - I See Stars

## 🔬 Resumo Executivo

O projeto **I See Stars** investiga como Large Language Models (LLMs) podem apoiar a Engenharia de Requisitos através da transformação automática de requisitos em linguagem natural em modelos estruturados usando a notação **iStar 2.0**. A principal inovação é uma abordagem interativa onde o LLM atua como um engenheiro de requisitos, fazendo perguntas de clarificação antes de gerar o modelo final.

---

## 🏛️ Arquitetura Técnica

### Componentes Principais

```
┌─────────────────┐
│   Scenarios     │  → Requisitos em linguagem natural
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│    Prompts      │  → Templates e estratégias de prompting
└────────┬────────┘
         │
         ├─────────────────┐
         ↓                 ↓
┌─────────────────┐  ┌─────────────────┐
│   Baseline      │  │  Interactive    │
│   Approach      │  │   Approach      │
└────────┬────────┘  └────────┬────────┘
         │                    │
         └────────┬───────────┘
                  ↓
         ┌─────────────────┐
         │     Models      │  → Modelos iStar 2.0 (JSON)
         └────────┬────────┘
                  ↓
         ┌─────────────────┐
         │   Evaluation    │  → Métricas e análises
         └────────┬────────┘
                  ↓
         ┌─────────────────┐
         │      Docs       │  → Relatórios e documentação
         └─────────────────┘
```

---

## 🔧 Stack Tecnológico

### Linguagens e Frameworks
- **Python**: Scripts de experimentação e processamento
- **JSON**: Formato de saída para modelos iStar 2.0
- **Markdown**: Documentação e cenários

### Ferramentas de LLM
- **OpenAI API** ou **Anthropic API**: Para acesso a modelos como GPT-4, Claude, etc.
- **LangChain** (opcional): Para orquestração de prompts complexos
- **Prompt Engineering Tools**: Para versionamento e teste de prompts

### Ferramentas de Análise
- **Pandas**: Processamento de dados e métricas
- **Matplotlib/Seaborn**: Visualizações
- **Jupyter Notebooks**: Análise exploratória

### Interface (Opcional)
- **Streamlit** ou **Gradio**: Interface web rápida
- **Flask/FastAPI**: API REST para integração
- **React/Vue**: Interface mais sofisticada (se necessário)

---

## 📐 Estrutura de Dados

### Formato iStar 2.0 (JSON)

```json
{
  "model": {
    "name": "Taxi App System",
    "actors": [
      {
        "id": "passenger",
        "type": "agent",
        "name": "Passenger"
      },
      {
        "id": "driver",
        "type": "agent",
        "name": "Driver"
      }
    ],
    "goals": [
      {
        "id": "g1",
        "actor": "passenger",
        "name": "Request a ride",
        "type": "goal"
      }
    ],
    "softgoals": [
      {
        "id": "sg1",
        "actor": "passenger",
        "name": "Fast service",
        "type": "softgoal"
      }
    ],
    "tasks": [
      {
        "id": "t1",
        "actor": "passenger",
        "name": "Select destination",
        "type": "task"
      }
    ],
    "dependencies": [
      {
        "depender": "passenger",
        "dependee": "driver",
        "dependum": "g1"
      }
    ]
  }
}
```

### Estrutura de Cenário

```json
{
  "id": "scenario_001",
  "name": "Taxi App System",
  "domain": "transportation",
  "complexity": "medium",
  "description": "A system for requesting taxi rides...",
  "intentional_ambiguities": [
    "Payment method not specified",
    "Rating system unclear"
  ]
}
```

---

## 🔄 Pipeline de Processamento

### Abordagem Baseline (Zero-Shot)

```
1. Input: Cenário em linguagem natural
2. Prompt: Template com explicação iStar 2.0 + cenário
3. LLM: Gera modelo diretamente
4. Output: Modelo iStar 2.0 em JSON
5. Validação: Verificar estrutura JSON
6. Armazenamento: Salvar em /models
```

### Abordagem Interativa

```
1. Input: Cenário em linguagem natural
2. Prompt Fase 1: Gerar 5-8 perguntas de clarificação
3. LLM: Gera lista de perguntas
4. Interface: Apresenta perguntas ao usuário
5. Input: Respostas do usuário
6. Prompt Fase 2: Cenário + perguntas + respostas → modelo
7. LLM: Gera modelo final
8. Output: Modelo iStar 2.0 em JSON
9. Validação: Verificar estrutura JSON
10. Armazenamento: Salvar em /models
```

---

## 📊 Métricas de Avaliação

### Métricas Quantitativas

1. **Completude**
   - Número de atores identificados vs. esperado
   - Número de metas identificadas vs. esperado
   - Cobertura de elementos (goals, softgoals, tasks, dependencies)

2. **Conformidade**
   - Validação de estrutura JSON
   - Verificação de tipos de elementos
   - Consistência de referências (IDs válidos)

3. **Qualidade das Perguntas**
   - Número de perguntas geradas
   - Categorização (atores, metas, tarefas, etc.)
   - Relevância (avaliação manual)

### Métricas Qualitativas

1. **Avaliação por Especialistas**
   - Completude percebida
   - Correção do modelo
   - Utilidade das perguntas

2. **Comparação com Gold Standard**
   - Diferenças estruturais
   - Elementos faltantes
   - Elementos incorretos

---

## 🧪 Design Experimental

### Variáveis Independentes
- **Abordagem**: Baseline vs. Interativa
- **Cenário**: Diferentes domínios e complexidades
- **Modelo LLM**: Diferentes modelos (GPT-4, Claude, etc.)

### Variáveis Dependentes
- Completude do modelo
- Conformidade à notação iStar 2.0
- Qualidade das perguntas (apenas para abordagem interativa)

### Controles
- Mesmos cenários para ambas as abordagens
- Mesmos parâmetros do LLM (temperatura, tokens)
- Mesmos avaliadores

---

## 🔐 Considerações de Implementação

### Versionamento
- Git para controle de versão
- Tags para versões de prompts
- Timestamps em modelos gerados

### Reprodutibilidade
- Seeds para aleatoriedade
- Configurações salvas em arquivos JSON/YAML
- Logs detalhados de execução

### Validação
- Schemas JSON para validar modelos iStar 2.0
- Testes unitários para scripts de processamento
- Validação manual de amostras

### Performance
- Cache de respostas do LLM (para economia)
- Processamento em lote quando possível
- Paralelização de experimentos independentes

---

## 📈 Escalabilidade

### Fase Atual (Pesquisa)
- 3-5 cenários
- 2 abordagens
- Avaliação manual focada

### Expansão Futura
- Mais cenários e domínios
- Automação de métricas
- Interface mais robusta
- Integração com ferramentas iStar existentes

---

## 🎯 Entregas Técnicas

1. **Código e Scripts**
   - Scripts de experimentação (`/experiments`)
   - Scripts de avaliação (`/evaluation`)
   - Interface interativa (`/interface`)

2. **Dados**
   - Cenários (`/scenarios`)
   - Modelos gerados (`/models`)
   - Resultados de avaliação (`/evaluation`)

3. **Documentação**
   - Metodologia (`/docs`)
   - Relatório final (`/docs`)
   - README e guias de uso

4. **Prompts**
   - Templates versionados (`/prompts`)
   - Documentação de estratégias (`/prompts`)

---

## 🔍 Pontos de Atenção Técnica

1. **Consistência de Output**
   - LLMs podem variar na estrutura JSON
   - Necessário parsing robusto e validação

2. **Custos de API**
   - Múltiplas chamadas na abordagem interativa
   - Monitoramento de uso

3. **Qualidade das Perguntas**
   - Perguntas devem ser relevantes e acionáveis
   - Balancear número de perguntas vs. fadiga do usuário

4. **Validação de Modelos**
   - Schemas JSON rigorosos
   - Verificação de integridade referencial

---

## 📚 Referências Técnicas

- **iStar 2.0**: Especificação da notação
- **LLM Prompting**: Técnicas de prompt engineering
- **Requirements Engineering**: Metodologias de elicitação
- **JSON Schema**: Validação de estruturas

---

## 🚀 Próximas Implementações Técnicas

1. Desenvolver schemas JSON para validação
2. Criar scripts de processamento automatizado
3. Implementar interface básica de interação
4. Desenvolver métricas de avaliação automatizadas
5. Criar pipeline de experimentação completo

