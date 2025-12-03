# Plano de Ação Completo - I See Stars

## 📋 Índice

1. [Metodologia](#1-metodologia)
2. [Setup dos Cenários](#2-setup-dos-cenários)
3. [Processo de Prompting](#3-processo-de-prompting)
4. [Métricas de Avaliação](#4-métricas-de-avaliação)
5. [Validação de JSON](#5-processo-para-validar-o-json)
6. [Comparação Baseline vs Interativo](#6-processo-para-comparar-baseline-vs-interativo)
7. [Checklist de Reprodutibilidade](#7-checklist-de-reprodutibilidade)

---

## 1. Metodologia

### 1.1 Objetivo da Metodologia

Avaliar se uma abordagem interativa de elicitação de requisitos (onde o LLM faz perguntas antes de gerar o modelo) produz modelos iStar 2.0 de melhor qualidade comparado a uma abordagem baseline (zero-shot).

### 1.2 Design Experimental

**Tipo**: Estudo comparativo experimental

**Variáveis Independentes**:
- Abordagem de prompting (baseline vs. interativa)
- Cenários de requisitos (3-5 diferentes)
- Modelo LLM utilizado (ex: GPT-4, Claude)

**Variáveis Dependentes**:
- Completude do modelo
- Clareza do modelo
- Conformidade com iStar 2.0
- Qualidade das perguntas (apenas abordagem interativa)

**Controles**:
- Mesmos cenários para ambas as abordagens
- Mesmos parâmetros do LLM (temperatura, max_tokens)
- Mesmos avaliadores
- Mesmo processo de validação

### 1.3 Fases do Estudo

#### Fase 1: Preparação (Semana 1-2)
- **Objetivo**: Preparar todos os materiais necessários
- **Atividades**:
  - Criar/validar cenários de requisitos
  - Desenvolver prompts baseline e interativos
  - Criar modelos de referência (gold standard)
  - Configurar ambiente de experimentação

#### Fase 2: Execução Baseline (Semana 3)
- **Objetivo**: Gerar modelos usando abordagem zero-shot
- **Atividades**:
  - Executar experimentos baseline para todos os cenários
  - Validar e armazenar modelos gerados
  - Registrar logs e metadados

#### Fase 3: Execução Interativa (Semana 4-5)
- **Objetivo**: Gerar modelos usando abordagem interativa
- **Atividades**:
  - Executar processo interativo para todos os cenários
  - Coletar perguntas e respostas
  - Gerar e validar modelos finais
  - Registrar logs e metadados

#### Fase 4: Avaliação (Semana 6-7)
- **Objetivo**: Avaliar qualidade dos modelos gerados
- **Atividades**:
  - Calcular métricas quantitativas
  - Coletar avaliações de especialistas
  - Comparar com modelos de referência
  - Analisar qualidade das perguntas

#### Fase 5: Análise e Relatório (Semana 8)
- **Objetivo**: Consolidar resultados e escrever relatório
- **Atividades**:
  - Análise estatística comparativa
  - Interpretação de resultados
  - Documentação completa
  - Preparação de visualizações

### 1.4 Critérios de Sucesso

- **Completude**: Modelos interativos devem ter ≥ 10% mais elementos identificados
- **Conformidade**: ≥ 95% dos modelos devem passar validação estrutural
- **Qualidade**: Especialistas devem preferir modelos interativos em ≥ 70% dos casos

---

## 2. Setup dos Cenários

### 2.1 Objetivo

Criar e preparar cenários de requisitos em linguagem natural que sejam representativos, tenham ambiguidades intencionais apropriadas e variem em domínio e complexidade.

### 2.2 Passos para Criação de Cenários

#### Passo 2.2.1: Seleção de Domínios
- [ ] Identificar 3-5 domínios diferentes
  - Exemplos: transporte, educação, saúde, comércio, social
- [ ] Garantir que domínios sejam familiares aos avaliadores
- [ ] Documentar escolha dos domínios

#### Passo 2.2.2: Redação dos Cenários
- [ ] Escrever descrição do sistema (200-500 palavras)
- [ ] Incluir requisitos informais em linguagem natural
- [ ] **Inserir ambiguidades intencionais**:
  - Atores não explicitamente definidos
  - Metas implícitas ou vagas
  - Processos incompletos
  - Dependências não claras
  - Critérios de qualidade não especificados
- [ ] Garantir que cenário seja compreensível apesar das ambiguidades
- [ ] Revisar clareza básica do texto

#### Passo 2.2.3: Documentação de Metadados
- [ ] Criar arquivo `scenarios_metadata.json` com:
  ```json
  {
    "scenario_id": "scenario_001",
    "name": "Taxi App System",
    "domain": "transportation",
    "complexity": "medium",
    "word_count": 250,
    "intentional_ambiguities": [
      "Payment method not specified",
      "Rating criteria unclear"
    ],
    "expected_actors": ["passenger", "driver", "system"],
    "expected_goals": 5,
    "created_at": "2024-12-01"
  }
  ```
- [ ] Salvar cenário em `/scenarios/scenario_{id}_{name}.md`
- [ ] Atualizar índice de cenários

#### Passo 2.2.4: Validação dos Cenários
- [ ] Revisar com pelo menos 2 especialistas em RE
- [ ] Verificar que ambiguidades são apropriadas (não excessivas)
- [ ] Confirmar que cenário é representativo
- [ ] Validar tamanho e complexidade
- [ ] Incorporar feedback e revisar

#### Passo 2.2.5: Criação de Modelos de Referência
- [ ] Para cada cenário, criar modelo iStar 2.0 manualmente
- [ ] Incluir todos os elementos esperados (atores, metas, softgoals, tarefas, dependências)
- [ ] Validar conformidade com iStar 2.0
- [ ] Salvar em `/models/reference/scenario_{id}_gold_standard.json`
- [ ] Documentar decisões de modelagem

### 2.3 Checklist de Qualidade dos Cenários

- [ ] Cenário tem 200-500 palavras
- [ ] Contém 3-5 ambiguidades intencionais claras
- [ ] É compreensível para leitores não-especialistas
- [ ] Representa um sistema realista ou plausível
- [ ] Varia em complexidade (simples, médio, complexo)
- [ ] Metadados completos documentados
- [ ] Modelo de referência criado e validado
- [ ] Revisado por especialistas

---

## 3. Processo de Prompting

### 3.1 Abordagem Baseline (Zero-Shot)

#### 3.1.1 Objetivo
Gerar modelo iStar 2.0 diretamente a partir do cenário, sem interação prévia.

#### 3.1.2 Estrutura do Prompt Baseline

**Componentes obrigatórios**:
1. **Contexto sobre iStar 2.0**
2. **Explicação do domínio** (se aplicável)
3. **Cenário de requisitos**
4. **Instruções de geração**
5. **Especificação do formato JSON**
6. **Constraints e regras**

#### 3.1.3 Passos para Execução Baseline

**Passo 3.1.3.1: Preparar Prompt**
- [ ] Carregar template base de prompt (`/prompts/baseline/zero_shot_template.md`)
- [ ] Inserir explicação sobre iStar 2.0
- [ ] Inserir cenário de requisitos
- [ ] Inserir especificação do formato JSON esperado
- [ ] Adicionar constraints (ex: "Não invente elementos não mencionados")
- [ ] Validar prompt completo

**Passo 3.1.3.2: Configurar Parâmetros do LLM**
- [ ] Definir modelo LLM (ex: `gpt-4`, `claude-3-opus`)
- [ ] Configurar temperatura: `0.3` (baixa para consistência)
- [ ] Configurar max_tokens: `2000-4000` (dependendo do modelo)
- [ ] Salvar configuração em `/experiments/config/baseline_config.json`

**Passo 3.1.3.3: Executar Geração**
- [ ] Enviar prompt para API do LLM
- [ ] Registrar timestamp e metadados
- [ ] Capturar resposta completa
- [ ] Salvar log em `/experiments/logs/baseline_{scenario_id}_{timestamp}.log`

**Passo 3.1.3.4: Processar Resposta**
- [ ] Extrair JSON da resposta (pode estar em code blocks)
- [ ] Validar estrutura JSON básica
- [ ] Se inválido, tentar parsing/limpeza
- [ ] Salvar modelo em `/models/baseline/scenario_{id}_baseline_{timestamp}.json`

**Passo 3.1.3.5: Validar e Registrar**
- [ ] Executar validação de JSON (ver Seção 5)
- [ ] Registrar resultado da validação
- [ ] Adicionar metadados ao modelo:
  ```json
  {
    "metadata": {
      "generated_at": "2024-12-01T10:00:00Z",
      "approach": "baseline",
      "scenario_id": "scenario_001",
      "llm_model": "gpt-4",
      "temperature": 0.3,
      "prompt_version": "v1.0",
      "validation_status": "valid|invalid|partial"
    }
  }
  ```

#### 3.1.4 Template de Prompt Baseline

```
Você é um especialista em Engenharia de Requisitos e notação iStar 2.0.

CONTEXTO SOBRE iSTAR 2.0:
[iStar 2.0 é uma notação para modelagem de requisitos orientada a objetivos...]

ELEMENTOS PRINCIPAIS:
- Actors: Agentes do sistema (humanos, sistemas, organizações)
- Goals: Objetivos que atores desejam alcançar
- Softgoals: Objetivos qualitativos (ex: "segurança", "usabilidade")
- Tasks: Atividades específicas para alcançar goals
- Dependencies: Relações de dependência entre atores

CENÁRIO DE REQUISITOS:
[Inserir cenário aqui]

INSTRUÇÕES:
1. Analise o cenário acima
2. Identifique todos os atores, goals, softgoals, tasks e dependencies
3. Gere um modelo iStar 2.0 completo em formato JSON

FORMATO DE SAÍDA (JSON):
IMPORTANTE: Use EXATAMENTE a estrutura JSON do Pistar 2.0.0. Consulte ISTAR_2_0_JSON_STRUCTURE.md para a estrutura completa.

Estrutura básica:
{
  "actors": [
    {
      "id": "uuid",
      "text": "Nome do Ator",
      "type": "istar.Agent | istar.Role | istar.Actor",
      "x": 0,
      "y": 0,
      "nodes": [
        {
          "id": "uuid",
          "text": "Nome",
          "type": "istar.Goal | istar.Task | istar.Quality | istar.Resource",
          "x": 0,
          "y": 0
        }
      ]
    }
  ],
  "orphans": [],
  "dependencies": [
    {
      "id": "uuid",
      "text": "Nome",
      "type": "istar.Goal | istar.Task | istar.Quality | istar.Resource",
      "x": 0,
      "y": 0,
      "source": "id-ator-depender",
      "target": "id-ator-dependee"
    }
  ],
  "links": [
    {
      "id": "uuid",
      "type": "istar.AndRefinementLink | istar.OrRefinementLink | ...",
      "source": "id-origem",
      "target": "id-destino",
      "label": ""
    }
  ],
  "display": {},
  "tool": "pistar.2.0.0",
  "istar": "2.0",
  "saveDate": "",
  "diagram": {
    "width": 1700,
    "height": 1300,
    "name": "",
    "customProperties": {}
  }
}

CONSTRAINTS:
- Use apenas elementos mencionados no cenário
- Não invente detalhes não especificados
- Siga estritamente o formato JSON acima
- Todos os IDs devem ser únicos
```

### 3.2 Abordagem Interativa (Elicitação Guiada)

#### 3.2.1 Objetivo
Gerar modelo iStar 2.0 através de um processo em duas fases: primeiro o LLM gera perguntas de clarificação, depois gera o modelo usando as respostas.

#### 3.2.2 Estrutura do Processo Interativo

**Fase 1: Geração de Perguntas**
- LLM analisa cenário
- Gera 5-8 perguntas de clarificação
- Perguntas focam em: atores, goals, softgoals, tasks, dependencies

**Fase 2: Geração do Modelo**
- LLM recebe: cenário original + perguntas + respostas
- Gera modelo iStar 2.0 final

#### 3.2.3 Passos para Execução Interativa

**FASE 1: Geração de Perguntas**

**Passo 3.2.3.1: Preparar Prompt de Perguntas**
- [ ] Carregar template (`/prompts/interactive/question_generation_template.md`)
- [ ] Inserir explicação sobre iStar 2.0
- [ ] Inserir cenário de requisitos
- [ ] Inserir instruções para gerar perguntas
- [ ] Especificar número de perguntas (5-8)
- [ ] Especificar categorias (atores, goals, softgoals, tasks, dependencies)
- [ ] Validar prompt completo

**Passo 3.2.3.2: Configurar Parâmetros do LLM (Fase 1)**
- [ ] Definir modelo LLM
- [ ] Configurar temperatura: `0.5` (mais criativo para perguntas)
- [ ] Configurar max_tokens: `1000-1500`
- [ ] Salvar configuração

**Passo 3.2.3.3: Executar Geração de Perguntas**
- [ ] Enviar prompt para API do LLM
- [ ] Registrar timestamp
- [ ] Capturar resposta com perguntas
- [ ] Salvar log

**Passo 3.2.3.4: Processar e Validar Perguntas**
- [ ] Extrair lista de perguntas da resposta
- [ ] Validar formato (lista numerada ou JSON)
- [ ] Verificar que há 5-8 perguntas
- [ ] Categorizar perguntas (atores, goals, etc.)
- [ ] Salvar perguntas em `/experiments/interactive/questions_{scenario_id}_{timestamp}.json`

**Passo 3.2.3.5: Apresentar Perguntas ao Usuário**
- [ ] Usar interface (`/interface`) ou processo manual
- [ ] Exibir cada pergunta numerada
- [ ] Coletar resposta do usuário
- [ ] Validar que respostas não estão vazias
- [ ] Salvar perguntas e respostas pareadas

**FASE 2: Geração do Modelo**

**Passo 3.2.3.6: Preparar Prompt de Geração Final**
- [ ] Carregar template (`/prompts/interactive/model_generation_template.md`)
- [ ] Inserir explicação sobre iStar 2.0
- [ ] Inserir cenário original
- [ ] Inserir perguntas geradas
- [ ] Inserir respostas do usuário
- [ ] Inserir instruções para gerar modelo
- [ ] Inserir especificação do formato JSON
- [ ] Validar prompt completo

**Passo 3.2.3.7: Configurar Parâmetros do LLM (Fase 2)**
- [ ] Definir modelo LLM (mesmo da Fase 1)
- [ ] Configurar temperatura: `0.3` (consistência)
- [ ] Configurar max_tokens: `2000-4000`
- [ ] Salvar configuração

**Passo 3.2.3.8: Executar Geração do Modelo**
- [ ] Enviar prompt completo para API do LLM
- [ ] Registrar timestamp
- [ ] Capturar resposta completa
- [ ] Salvar log em `/experiments/logs/interactive_{scenario_id}_{timestamp}.log`

**Passo 3.2.3.9: Processar Resposta**
- [ ] Extrair JSON da resposta
- [ ] Validar estrutura JSON básica
- [ ] Se inválido, tentar parsing/limpeza
- [ ] Salvar modelo em `/models/interactive/scenario_{id}_interactive_{timestamp}.json`

**Passo 3.2.3.10: Validar e Registrar**
- [ ] Executar validação de JSON (ver Seção 5)
- [ ] Registrar resultado da validação
- [ ] Adicionar metadados ao modelo incluindo:
  - Perguntas geradas
  - Respostas fornecidas
  - Timestamp de cada fase

#### 3.2.4 Template de Prompt - Fase 1 (Perguntas)

```
Você é um engenheiro de requisitos especializado em iStar 2.0.

CONTEXTO SOBRE iSTAR 2.0:
[Explicação sobre iStar 2.0...]

CENÁRIO DE REQUISITOS:
[Inserir cenário aqui]

TAREFA:
Analise o cenário acima e identifique áreas que precisam de clarificação para criar um modelo iStar 2.0 completo e preciso.

Gere 5-8 perguntas de clarificação focadas em:
- Atores: Quem são os principais atores? Há atores implícitos?
- Goals: Quais são os objetivos principais de cada ator?
- Softgoals: Quais são os critérios de qualidade (ex: segurança, usabilidade)?
- Tasks: Quais são as tarefas específicas para alcançar os goals?
- Dependencies: Quais são as dependências entre atores?

FORMATO DE SAÍDA:
Liste as perguntas numeradas, uma por linha. Cada pergunta deve ser:
- Específica e acionável
- Focada em um aspecto do modelo iStar
- Capaz de ser respondida de forma concisa
```

#### 3.2.5 Template de Prompt - Fase 2 (Modelo)

```
Você é um especialista em Engenharia de Requisitos e notação iStar 2.0.

CONTEXTO SOBRE iSTAR 2.0:
[Explicação sobre iStar 2.0...]

CENÁRIO DE REQUISITOS ORIGINAL:
[Inserir cenário original]

PERGUNTAS DE CLARIFICAÇÃO E RESPOSTAS:
Q1: [Pergunta 1]
A1: [Resposta 1]

Q2: [Pergunta 2]
A2: [Resposta 2]

[... mais perguntas e respostas ...]

INSTRUÇÕES:
1. Use o cenário original E as respostas às perguntas acima
2. Gere um modelo iStar 2.0 completo e preciso
3. Incorpore as informações das respostas no modelo
4. Siga estritamente o formato JSON do Pistar 2.0.0 (consulte ISTAR_2_0_JSON_STRUCTURE.md)

FORMATO DE SAÍDA (JSON):
IMPORTANTE: Use EXATAMENTE a estrutura JSON do Pistar 2.0.0.

{
  "actors": [
    {
      "id": "uuid",
      "text": "Nome",
      "type": "istar.Agent | istar.Role | istar.Actor",
      "x": 0,
      "y": 0,
      "nodes": [
        {
          "id": "uuid",
          "text": "Nome",
          "type": "istar.Goal | istar.Task | istar.Quality | istar.Resource",
          "x": 0,
          "y": 0
        }
      ]
    }
  ],
  "orphans": [],
  "dependencies": [
    {
      "id": "uuid",
      "text": "Nome",
      "type": "istar.Goal | istar.Task | istar.Quality | istar.Resource",
      "x": 0,
      "y": 0,
      "source": "id-ator-depender",
      "target": "id-ator-dependee"
    }
  ],
  "links": [],
  "display": {},
  "tool": "pistar.2.0.0",
  "istar": "2.0",
  "saveDate": "",
  "diagram": {
    "width": 1700,
    "height": 1300,
    "name": "",
    "customProperties": {}
  }
}

CONSTRAINTS:
- Use informações do cenário E das respostas
- Não invente elementos não mencionados
- Siga estritamente o formato JSON acima (Pistar 2.0.0)
- Todos os IDs devem ser únicos (use UUIDs)
- source/target sempre referem a IDs existentes
- tool deve ser exatamente "pistar.2.0.0"
- istar deve ser exatamente "2.0"
```

### 3.3 Versionamento de Prompts

- [ ] Cada versão de prompt deve ser salva com versão (v1.0, v1.1, etc.)
- [ ] Documentar mudanças entre versões
- [ ] Manter histórico de efetividade
- [ ] Usar mesma versão para todos os cenários em um experimento

---

## 4. Métricas de Avaliação

### 4.1 Objetivo

Avaliar quantitativamente e qualitativamente a qualidade dos modelos gerados, comparando abordagens baseline e interativa.

### 4.2 Métrica 1: Completude

#### 4.2.1 Definição
Mede a extensão em que o modelo captura todos os elementos esperados do cenário.

#### 4.2.2 Elementos Avaliados
- **Atores (Actors)**: Agentes identificados
- **Metas (Goals)**: Objetivos identificados
- **Softgoals**: Critérios de qualidade identificados
- **Tarefas (Tasks)**: Atividades identificadas
- **Dependências (Dependencies)**: Relações identificadas

#### 4.2.3 Cálculo de Completude

**Passo 4.2.3.1: Preparar Dados**
- [ ] Carregar modelo gerado
- [ ] Carregar modelo de referência (gold standard)
- [ ] Extrair listas de elementos de cada modelo

**Passo 4.2.3.2: Calcular Completude por Elemento**
Para cada tipo de elemento (atores, goals, etc.):

```
Completude = (Elementos Corretos Identificados / Elementos Esperados) × 100%
```

**Elementos Corretos**: Elementos do modelo gerado que correspondem a elementos do modelo de referência (match por nome/semântica).

**Passo 4.2.3.3: Calcular Completude Geral**
```
Completude Geral = Média das completudes de cada tipo de elemento
```

**Passo 4.2.3.4: Implementar Script**
- [ ] Criar script `/evaluation/metrics/completeness_calculator.py`
- [ ] Função para matching de elementos (exato + semântico)
- [ ] Função para calcular completude por tipo
- [ ] Função para calcular completude geral
- [ ] Salvar resultados em `/evaluation/results/completeness_{scenario_id}.json`

#### 4.2.4 Exemplo de Cálculo

```
Modelo de Referência:
- Atores: 3 (passenger, driver, system)
- Goals: 5
- Softgoals: 2
- Tasks: 4
- Dependencies: 3

Modelo Gerado:
- Atores: 2 (passenger, driver) → Completude: 2/3 = 66.7%
- Goals: 4 → Completude: 4/5 = 80%
- Softgoals: 1 → Completude: 1/2 = 50%
- Tasks: 3 → Completude: 3/4 = 75%
- Dependencies: 2 → Completude: 2/3 = 66.7%

Completude Geral: (66.7 + 80 + 50 + 75 + 66.7) / 5 = 67.7%
```

### 4.3 Métrica 2: Clareza

#### 4.3.1 Definição
Mede quão claros e bem definidos são os elementos do modelo.

#### 4.3.2 Aspectos Avaliados
- **Nomes de Elementos**: Claros e descritivos?
- **Relações**: Bem definidas e compreensíveis?
- **Estrutura**: Organizada e lógica?

#### 4.3.3 Processo de Avaliação de Clareza

**Passo 4.3.3.1: Avaliação por Especialistas**
- [ ] Preparar formulário de avaliação
- [ ] Para cada modelo, especialistas avaliam em escala Likert (1-5):
  - Nomes são claros e descritivos? (1=confuso, 5=muito claro)
  - Relações são bem definidas? (1=ambíguas, 5=muito claras)
  - Estrutura é lógica? (1=confusa, 5=muito lógica)
- [ ] Coletar avaliações de pelo menos 2 especialistas

**Passo 4.3.3.2: Calcular Score de Clareza**
```
Score de Clareza = Média das avaliações Likert
```

**Passo 4.3.3.3: Análise Qualitativa**
- [ ] Coletar comentários qualitativos dos especialistas
- [ ] Identificar padrões de problemas de clareza
- [ ] Categorizar tipos de ambiguidade encontrados

**Passo 4.3.3.4: Implementar Processo**
- [ ] Criar formulário em `/evaluation/expert_evaluations/clarity_form.md`
- [ ] Script para agregar avaliações: `/evaluation/metrics/clarity_analyzer.py`
- [ ] Salvar resultados em `/evaluation/results/clarity_{scenario_id}.json`

### 4.4 Métrica 3: Conformidade com iStar 2.0

#### 4.4.1 Definição
Mede a aderência do modelo à especificação da notação iStar 2.0.

#### 4.4.2 Aspectos Avaliados
- **Estrutura JSON**: Conforme schema?
- **Tipos de Elementos**: Tipos válidos?
- **Integridade Referencial**: IDs válidos e referências corretas?
- **Regras da Notação**: Segue regras do iStar 2.0?

#### 4.4.3 Processo de Avaliação de Conformidade

**Passo 4.4.3.1: Validação Estrutural**
- [ ] Validar JSON contra schema (ver Seção 5)
- [ ] Verificar tipos de elementos (agent, role, position, etc.)
- [ ] Verificar estrutura de cada elemento

**Passo 4.4.3.2: Validação de Integridade Referencial**
- [ ] Verificar que todos os IDs de atores em goals/tasks existem
- [ ] Verificar que dependências referenciam atores válidos
- [ ] Verificar que dependums referenciam elementos válidos

**Passo 4.4.3.3: Validação de Regras iStar 2.0**
- [ ] Goals devem ter ator associado
- [ ] Tasks devem ter ator associado
- [ ] Dependencies devem ter depender, dependee e dependum
- [ ] Softgoals devem ser distinguíveis de goals

**Passo 4.4.3.4: Calcular Score de Conformidade**
```
Conformidade = (Regras Válidas / Total de Regras) × 100%
```

**Passo 4.4.3.5: Implementar Script**
- [ ] Criar script `/evaluation/metrics/conformance_validator.py`
- [ ] Integrar com validação de JSON (Seção 5)
- [ ] Salvar resultados em `/evaluation/results/conformance_{scenario_id}.json`

### 4.5 Métrica 4: Qualidade das Perguntas (Apenas Interativo)

#### 4.5.1 Definição
Avalia a relevância e utilidade das perguntas geradas na abordagem interativa.

#### 4.5.2 Aspectos Avaliados
- **Relevância**: Pergunta é relevante para o modelo?
- **Especificidade**: Pergunta é específica o suficiente?
- **Utilidade**: Resposta ajudou a melhorar o modelo?

#### 4.5.3 Processo de Avaliação

**Passo 4.5.3.1: Categorização de Perguntas**
- [ ] Categorizar cada pergunta por tipo:
  - Atores
  - Goals
  - Softgoals
  - Tasks
  - Dependencies
- [ ] Contar distribuição por categoria

**Passo 4.5.3.2: Avaliação por Especialistas**
- [ ] Especialistas avaliam cada pergunta em escala Likert (1-5):
  - Relevância: (1=irrelevante, 5=muito relevante)
  - Especificidade: (1=vaga, 5=muito específica)
  - Utilidade: (1=não útil, 5=muito útil)

**Passo 4.5.3.3: Análise de Impacto**
- [ ] Comparar modelo gerado com e sem respostas
- [ ] Identificar quais perguntas levaram a melhorias no modelo
- [ ] Calcular correlação entre qualidade da pergunta e melhoria do modelo

**Passo 4.5.3.4: Implementar Script**
- [ ] Criar script `/evaluation/metrics/question_quality_analyzer.py`
- [ ] Salvar resultados em `/evaluation/results/question_quality_{scenario_id}.json`

### 4.6 Consolidação de Métricas

**Passo 4.6.1: Agregar Resultados**
- [ ] Para cada cenário e abordagem, calcular todas as métricas
- [ ] Criar tabela consolidada em `/evaluation/results/metrics_summary.csv`
- [ ] Incluir: cenário, abordagem, completude, clareza, conformidade

**Passo 4.6.2: Visualizações**
- [ ] Gráfico de barras: Completude (baseline vs. interativo)
- [ ] Gráfico de barras: Clareza (baseline vs. interativo)
- [ ] Gráfico de barras: Conformidade (baseline vs. interativo)
- [ ] Heatmap: Métricas por cenário
- [ ] Salvar em `/evaluation/visualizations/`

---

## 5. Processo para Validar o JSON

### 5.1 Objetivo

Garantir que os modelos gerados estão em formato JSON válido e conforme ao schema iStar 2.0.

### 5.2 Passos de Validação

#### Passo 5.2.1: Criar Schema JSON

- [ ] Definir schema JSON Schema para iStar 2.0 (Pistar 2.0.0) em `/experiments/utils/istar_schema.json`
- [ ] **IMPORTANTE**: Usar estrutura exata definida em `ISTAR_2_0_JSON_STRUCTURE.md`
- [ ] Schema deve validar:
  - Estrutura raiz com campos: actors, orphans, dependencies, links, display, tool, istar, saveDate, diagram
  - `tool` deve ser exatamente `"pistar.2.0.0"`
  - `istar` deve ser exatamente `"2.0"`
  - Atores com estrutura: id, text, type (istar.Actor | istar.Agent | istar.Role), x, y, nodes
  - Nodes dentro de atores: id, text, type (istar.Goal | istar.Task | istar.Quality | istar.Resource), x, y
  - Dependencies: id, text, type, x, y, source, target
  - Links: id, type (vários tipos válidos), source, target, label (opcional)
- [ ] Consultar `ISTAR_2_0_JSON_STRUCTURE.md` para estrutura completa e exemplos

#### Passo 5.2.2: Validação de JSON Básico

- [ ] Criar função para validar JSON sintático:
  ```python
  def validate_json_syntax(json_string):
      try:
          json.loads(json_string)
          return True, None
      except json.JSONDecodeError as e:
          return False, str(e)
  ```
- [ ] Testar com modelos gerados
- [ ] Registrar erros de sintaxe

#### Passo 5.2.3: Extração de JSON da Resposta

- [ ] Criar função para extrair JSON de respostas do LLM:
  - Procurar por code blocks (```json ... ```)
  - Procurar por objetos JSON diretos
  - Tentar parsing incremental se necessário
- [ ] Implementar em `/experiments/utils/json_parser.py`

#### Passo 5.2.4: Validação contra Schema

- [ ] Usar biblioteca `jsonschema` para validar contra schema
- [ ] Criar função:
  ```python
  def validate_istar_schema(json_data, schema):
      validator = jsonschema.Draft7Validator(schema)
      errors = list(validator.iter_errors(json_data))
      return len(errors) == 0, errors
  ```
- [ ] Implementar em `/experiments/utils/istar_validator.py`

#### Passo 5.2.5: Validação de Integridade Referencial

- [ ] Verificar que todos os IDs em `source` e `target` de dependencies referem a IDs de atores existentes
- [ ] Verificar que todos os IDs em `source` e `target` de links referem a IDs existentes (atores ou nodes)
- [ ] Verificar que todos os nodes estão dentro de atores (não em orphans, a menos que necessário)
- [ ] Verificar que todos os IDs são únicos em todo o modelo
- [ ] Implementar em `/experiments/utils/istar_validator.py`

#### Passo 5.2.6: Validação de Regras iStar 2.0

- [ ] Verificar tipos de atores: `istar.Actor`, `istar.Agent`, `istar.Role`
- [ ] Verificar tipos de nodes: `istar.Goal`, `istar.Task`, `istar.Quality`, `istar.Resource`
- [ ] Verificar tipos de links válidos (OrRefinementLink, AndRefinementLink, DependencyLink, etc.)
- [ ] Verificar que `tool` é exatamente `"pistar.2.0.0"`
- [ ] Verificar que `istar` é exatamente `"2.0"`
- [ ] Verificar estrutura de dependencies (source, target, type, text)
- [ ] Implementar regras adicionais conforme `ISTAR_2_0_JSON_STRUCTURE.md`

#### Passo 5.2.7: Script de Validação Completo

- [ ] Criar script `/experiments/utils/validate_model.py` que:
  1. Carrega modelo JSON
  2. Valida sintaxe JSON
  3. Valida contra schema
  4. Valida integridade referencial
  5. Valida regras iStar 2.0
  6. Retorna relatório de validação
- [ ] Salvar relatórios em `/evaluation/validation_reports/`

#### Passo 5.2.8: Classificação de Validação

- [ ] Classificar modelos como:
  - **Válido**: Passa todas as validações
  - **Parcialmente Válido**: Passa validação estrutural mas tem erros de integridade
  - **Inválido**: Falha validação estrutural ou tem muitos erros
- [ ] Registrar classificação nos metadados do modelo

### 5.3 Tratamento de Erros

- [ ] Se JSON inválido, tentar correção automática (se possível)
- [ ] Registrar todos os erros encontrados
- [ ] Gerar relatório detalhado de erros
- [ ] Para modelos inválidos, documentar tipo de erro mais comum

---

## 6. Processo para Comparar Baseline vs Interativo

### 6.1 Objetivo

Comparar sistematicamente os modelos gerados pelas abordagens baseline e interativa para identificar diferenças e determinar qual produz melhores resultados.

### 6.2 Passos de Comparação

#### Passo 6.2.1: Preparar Dados para Comparação

- [ ] Para cada cenário, carregar:
  - Modelo baseline: `/models/baseline/scenario_{id}_baseline_{timestamp}.json`
  - Modelo interativo: `/models/interactive/scenario_{id}_interactive_{timestamp}.json`
  - Modelo de referência: `/models/reference/scenario_{id}_gold_standard.json`
- [ ] Verificar que modelos são do mesmo cenário
- [ ] Verificar que modelos foram gerados com mesma versão de prompt

#### Passo 6.2.2: Comparação Quantitativa

**Passo 6.2.2.1: Comparar Completude**
- [ ] Calcular completude de baseline vs. referência
- [ ] Calcular completude de interativo vs. referência
- [ ] Calcular diferença: `Completude_Interativo - Completude_Baseline`
- [ ] Testar significância estatística (se aplicável)

**Passo 6.2.2.2: Comparar Número de Elementos**
- [ ] Contar elementos em cada modelo:
  - Número de atores
  - Número de goals
  - Número de softgoals
  - Número de tasks
  - Número de dependencies
- [ ] Calcular diferenças absolutas e percentuais

**Passo 6.2.2.3: Comparar Conformidade**
- [ ] Comparar scores de conformidade
- [ ] Identificar tipos de erros mais comuns em cada abordagem
- [ ] Calcular taxa de modelos válidos vs. inválidos

#### Passo 6.2.3: Comparação Qualitativa

**Passo 6.2.3.1: Análise de Elementos Faltantes**
- [ ] Identificar elementos no referência que estão:
  - Presentes em ambos (baseline e interativo)
  - Presentes apenas no interativo
  - Presentes apenas no baseline
  - Ausentes em ambos
- [ ] Categorizar por tipo de elemento

**Passo 6.2.3.2: Análise de Elementos Incorretos**
- [ ] Identificar elementos incorretos ou mal definidos:
  - Nomes incorretos
  - Relações incorretas
  - Elementos inventados (não no cenário)
- [ ] Comparar frequência entre abordagens

**Passo 6.2.3.3: Análise de Clareza**
- [ ] Comparar scores de clareza (avaliação de especialistas)
- [ ] Identificar padrões de problemas de clareza
- [ ] Analisar comentários qualitativos

#### Passo 6.2.4: Análise Estatística

**Passo 6.2.4.1: Estatísticas Descritivas**
- [ ] Calcular para cada métrica:
  - Média
  - Mediana
  - Desvio padrão
  - Mínimo e máximo
- [ ] Separar por abordagem (baseline vs. interativo)

**Passo 6.2.4.2: Testes Estatísticos (se aplicável)**
- [ ] Se múltiplos cenários, realizar:
  - Teste t de Student (se distribuição normal)
  - Teste de Wilcoxon (se não normal)
  - Análise de variância (ANOVA) se múltiplos fatores
- [ ] Calcular tamanho do efeito (Cohen's d)
- [ ] Interpretar significância estatística

#### Passo 6.2.5: Análise por Cenário

- [ ] Para cada cenário individualmente:
  - Comparar métricas
  - Identificar padrões específicos
  - Documentar observações
- [ ] Identificar se há diferenças por domínio ou complexidade

#### Passo 6.2.6: Análise de Qualidade das Perguntas (Interativo)

- [ ] Analisar correlação entre:
  - Qualidade das perguntas → Melhoria no modelo
  - Número de perguntas → Completude
  - Tipo de pergunta → Tipo de elemento melhorado
- [ ] Identificar perguntas mais efetivas

#### Passo 6.2.7: Script de Comparação Automatizado

- [ ] Criar script `/evaluation/comparison/compare_approaches.py` que:
  1. Carrega modelos baseline e interativo
  2. Calcula todas as métricas
  3. Compara métricas
  4. Gera relatório comparativo
  5. Cria visualizações
- [ ] Salvar resultados em `/evaluation/comparison/comparison_results.json`

#### Passo 6.2.8: Relatório Comparativo

- [ ] Criar relatório em `/evaluation/comparison/comparative_analysis.md` com:
  - Tabela comparativa de métricas
  - Análise de diferenças
  - Interpretação de resultados
  - Conclusões
- [ ] Incluir visualizações comparativas

### 6.3 Critérios de Superioridade

Definir quando uma abordagem é considerada "melhor":

- **Completude**: Interativo tem ≥ 10% mais completude
- **Clareza**: Interativo tem score ≥ 0.5 pontos maior (escala 1-5)
- **Conformidade**: Interativo tem ≥ 5% mais conformidade
- **Consenso**: Especialistas preferem interativo em ≥ 70% dos casos

### 6.4 Visualizações Comparativas

- [ ] Gráfico de barras lado a lado: Métricas (baseline vs. interativo)
- [ ] Gráfico de linha: Completude por tipo de elemento
- [ ] Heatmap: Diferenças por cenário
- [ ] Box plot: Distribuição de métricas
- [ ] Salvar em `/evaluation/visualizations/comparison/`

---

## 7. Checklist de Reprodutibilidade

### 7.1 Objetivo

Garantir que todos os experimentos podem ser reproduzidos exatamente, permitindo validação e extensão do trabalho.

### 7.2 Documentação de Ambiente

#### 7.2.1 Dependências de Software
- [ ] Criar `requirements.txt` com todas as dependências Python:
  ```
  openai==1.3.0
  anthropic==0.7.0
  jsonschema==4.20.0
  pandas==2.1.0
  matplotlib==3.8.0
  python-dotenv==1.0.0
  ```
- [ ] Especificar versões exatas
- [ ] Documentar sistema operacional testado
- [ ] Documentar versão do Python (ex: Python 3.11)

#### 7.2.2 Configurações de API
- [ ] Criar `.env.example` com estrutura de variáveis:
  ```
  OPENAI_API_KEY=your_key_here
  ANTHROPIC_API_KEY=your_key_here
  ```
- [ ] Documentar como obter chaves de API
- [ ] **NUNCA** commitar chaves reais no repositório

#### 7.2.3 Estrutura de Diretórios
- [ ] Documentar estrutura completa de diretórios
- [ ] Incluir no README principal
- [ ] Garantir que estrutura é criada automaticamente (script de setup)

### 7.3 Versionamento de Código

#### 7.3.1 Controle de Versão
- [ ] Usar Git para versionamento
- [ ] Criar tags para versões importantes:
  - `v1.0-baseline-experiments`
  - `v1.0-interactive-experiments`
  - `v1.0-final-results`
- [ ] Documentar tags no README

#### 7.3.2 Commits Descritivos
- [ ] Commits devem descrever claramente mudanças
- [ ] Usar convenção de mensagens (ex: Conventional Commits)
- [ ] Incluir referências a issues/tarefas

### 7.4 Versionamento de Dados

#### 7.4.1 Modelos Gerados
- [ ] Todos os modelos devem ter timestamps
- [ ] Metadados devem incluir:
  - Versão do prompt usado
  - Modelo LLM usado
  - Parâmetros (temperatura, tokens)
  - Hash do cenário usado
- [ ] Manter histórico de modelos (não sobrescrever)

#### 7.4.2 Prompts
- [ ] Versionar prompts (v1.0, v1.1, etc.)
- [ ] Documentar mudanças entre versões
- [ ] Salvar cada versão em arquivo separado
- [ ] Manter log de efetividade por versão

#### 7.4.3 Configurações
- [ ] Versionar arquivos de configuração
- [ ] Documentar propósito de cada configuração
- [ ] Manter histórico de mudanças

### 7.5 Sementes e Aleatoriedade

#### 7.5.1 Seeds para Reprodutibilidade
- [ ] Definir seed fixo para experimentos:
  ```python
  import random
  random.seed(42)
  ```
- [ ] Se usar LLM com opção de seed, configurar seed fixo
- [ ] Documentar seed usado em cada experimento

#### 7.5.2 Parâmetros do LLM
- [ ] Documentar todos os parâmetros:
  - Modelo (ex: `gpt-4`, `claude-3-opus`)
  - Temperature (ex: `0.3`)
  - Max tokens (ex: `2000`)
  - Top-p (se usado)
  - Frequency penalty (se usado)
- [ ] Salvar em arquivo de configuração versionado

### 7.6 Logs e Rastreabilidade

#### 7.6.1 Logs de Execução
- [ ] Registrar todas as chamadas de API:
  - Timestamp
  - Prompt enviado
  - Resposta recebida
  - Parâmetros usados
  - Custo (se disponível)
- [ ] Salvar logs em `/experiments/logs/`
- [ ] Formato estruturado (JSON ou CSV)

#### 7.6.2 Rastreabilidade de Modelos
- [ ] Cada modelo deve ser rastreável até:
  - Cenário usado
  - Prompt usado (versão)
  - Configuração do LLM
  - Timestamp de geração
- [ ] Manter índice de modelos em `/models/metadata/models_index.json`

### 7.7 Scripts de Reprodução

#### 7.7.1 Script de Setup
- [ ] Criar `setup.sh` ou `setup.py` que:
  - Cria estrutura de diretórios
  - Instala dependências
  - Configura ambiente
- [ ] Testar em ambiente limpo

#### 7.7.2 Scripts de Execução
- [ ] Criar scripts que podem ser executados de forma idempotente:
  - `run_baseline_experiments.py`
  - `run_interactive_experiments.py`
  - `run_evaluation.py`
- [ ] Scripts devem poder ser executados múltiplas vezes sem efeitos colaterais
- [ ] Documentar ordem de execução

#### 7.7.3 Scripts de Validação
- [ ] Criar script que valida ambiente:
  - Verifica dependências instaladas
  - Verifica variáveis de ambiente
  - Verifica estrutura de diretórios
  - Testa conexão com APIs

### 7.8 Documentação de Processo

#### 7.8.1 README Principal
- [ ] Incluir instruções completas de setup
- [ ] Incluir instruções de execução
- [ ] Incluir exemplos de uso
- [ ] Incluir troubleshooting comum

#### 7.8.2 Documentação de Experimentos
- [ ] Documentar cada experimento:
  - Objetivo
  - Configuração
  - Resultados esperados
  - Como executar
- [ ] Manter em `/experiments/README.md`

#### 7.8.3 Documentação de Resultados
- [ ] Documentar como interpretar resultados
- [ ] Incluir exemplos de outputs esperados
- [ ] Documentar formato de arquivos de resultado

### 7.9 Validação de Reprodutibilidade

#### 7.9.1 Teste de Reprodução
- [ ] Executar experimentos em ambiente diferente:
  - Máquina diferente
  - Sistema operacional diferente (se possível)
  - Usuário diferente
- [ ] Comparar resultados
- [ ] Documentar diferenças (se houver)

#### 7.9.2 Checklist de Validação
Antes de considerar experimento reproduzível, verificar:
- [ ] Todas as dependências estão documentadas
- [ ] Todas as configurações estão versionadas
- [ ] Todos os seeds estão definidos
- [ ] Todos os prompts estão versionados
- [ ] Logs estão completos
- [ ] Scripts podem ser executados sem intervenção manual
- [ ] Resultados são idênticos (ou diferenças são documentadas)

### 7.10 Checklist Final de Reprodutibilidade

Antes de publicar ou compartilhar:

- [ ] **Ambiente**
  - [ ] `requirements.txt` completo e testado
  - [ ] `.env.example` documentado
  - [ ] Versões de software documentadas

- [ ] **Código**
  - [ ] Código versionado no Git
  - [ ] Tags criadas para versões importantes
  - [ ] README atualizado

- [ ] **Dados**
  - [ ] Modelos têm metadados completos
  - [ ] Prompts estão versionados
  - [ ] Configurações estão versionadas

- [ ] **Execução**
  - [ ] Scripts podem ser executados automaticamente
  - [ ] Ordem de execução documentada
  - [ ] Logs são gerados automaticamente

- [ ] **Validação**
  - [ ] Testado em ambiente limpo
  - [ ] Resultados são reproduzíveis
  - [ ] Diferenças documentadas (se houver)

- [ ] **Documentação**
  - [ ] README completo
  - [ ] Instruções claras
  - [ ] Exemplos fornecidos
  - [ ] Troubleshooting documentado

---

## 📊 Resumo do Plano de Ação

### Fases Principais

1. **Preparação** (Semanas 1-2)
   - Setup de cenários
   - Desenvolvimento de prompts
   - Criação de modelos de referência

2. **Execução Baseline** (Semana 3)
   - Geração de modelos zero-shot
   - Validação e armazenamento

3. **Execução Interativa** (Semanas 4-5)
   - Processo interativo completo
   - Geração de modelos finais

4. **Avaliação** (Semanas 6-7)
   - Cálculo de métricas
   - Avaliação de especialistas
   - Comparação de abordagens

5. **Análise e Relatório** (Semana 8)
   - Consolidação de resultados
   - Documentação final

### Entregas Principais

- Cenários de requisitos validados
- Prompts versionados (baseline e interativo)
- Modelos gerados (baseline e interativo)
- Modelos de referência (gold standard)
- Métricas de avaliação calculadas
- Relatório comparativo
- Documentação completa para reprodução

---

## 📝 Notas Finais

- Este plano deve ser seguido sequencialmente
- Cada passo deve ser completado antes de avançar
- Documentar qualquer desvio do plano
- Manter registro de decisões e mudanças
- Revisar e atualizar plano conforme necessário

