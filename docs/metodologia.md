# Metodologia de Pesquisa - I See Stars

## 1. Introdução

Este documento descreve a metodologia completa do projeto **I See Stars**, que investiga como Large Language Models (LLMs) podem apoiar a Engenharia de Requisitos através da transformação automática de requisitos em linguagem natural em modelos estruturados usando a notação iStar 2.0.

## 2. Objetivos de Pesquisa

### 2.1 Objetivo Principal

Avaliar se uma abordagem interativa de elicitação de requisitos (onde o LLM faz perguntas de clarificação antes de gerar o modelo) produz modelos iStar 2.0 de melhor qualidade comparado a uma abordagem baseline (zero-shot).

### 2.2 Objetivos Específicos

1. **Transformação Automática**: Investigar a capacidade de LLMs em transformar requisitos informais em modelos iStar 2.0 estruturados
2. **Elicitação Interativa**: Avaliar a efetividade de um processo interativo onde o LLM atua como engenheiro de requisitos
3. **Comparação de Abordagens**: Comparar sistematicamente abordagens baseline e interativa em termos de:
   - Completude dos modelos gerados
   - Clareza dos elementos modelados
   - Conformidade com a notação iStar 2.0
4. **Qualidade das Perguntas**: Avaliar a relevância e utilidade das perguntas geradas na abordagem interativa

## 3. Design Experimental

### 3.1 Tipo de Estudo

**Estudo Comparativo Experimental**: Comparação entre duas abordagens de prompting (baseline vs. interativa) para geração de modelos iStar 2.0.

### 3.2 Variáveis

#### Variáveis Independentes
- **Abordagem de Prompting**: 
  - Baseline (zero-shot): Geração direta do modelo
  - Interativa: Geração de perguntas seguida de geração do modelo
- **Cenários de Requisitos**: 3-5 cenários diferentes variando em:
  - Domínio (transporte, educação, saúde, comércio, social)
  - Complexidade (simples, médio, complexo)
  - Nível de ambiguidade intencional
- **Modelo LLM**: Modelo específico utilizado (ex: GPT-4, Claude)

#### Variáveis Dependentes
- **Completude**: Extensão em que o modelo captura elementos esperados
- **Clareza**: Quão claros e bem definidos são os elementos
- **Conformidade**: Aderência à especificação iStar 2.0
- **Qualidade das Perguntas**: Relevância e utilidade (apenas abordagem interativa)

#### Variáveis de Controle
- Mesmos cenários para ambas as abordagens
- Mesmos parâmetros do LLM (temperatura, max_tokens)
- Mesmos avaliadores
- Mesmo processo de validação
- Mesma versão de prompts

### 3.3 Hipóteses

**Hipótese Principal (H1)**:
A abordagem interativa produz modelos iStar 2.0 com maior completude comparada à abordagem baseline.

**Hipóteses Secundárias**:
- **H2**: A abordagem interativa produz modelos com maior clareza
- **H3**: A abordagem interativa produz modelos com maior conformidade à notação iStar 2.0
- **H4**: As perguntas geradas na abordagem interativa são relevantes e úteis para reduzir ambiguidade

## 4. Abordagens de Prompting

### 4.1 Abordagem Baseline (Zero-Shot)

#### Descrição
O LLM recebe um cenário de requisitos e é solicitado a gerar diretamente um modelo iStar 2.0, sem interação prévia.

#### Processo
1. **Input**: Cenário de requisitos em linguagem natural
2. **Prompt**: Template contendo:
   - Explicação sobre notação iStar 2.0
   - Contexto do domínio (se aplicável)
   - Cenário de requisitos
   - Instruções de geração
   - Especificação do formato JSON (Pistar 2.0.0)
   - Constraints e regras
3. **Output**: Modelo iStar 2.0 em formato JSON

#### Características
- **Uma única interação** com o LLM
- **Sem clarificação prévia** de ambiguidades
- **Geração direta** do modelo final
- **Eficiente** em termos de tempo e custo

#### Limitações Esperadas
- Pode gerar modelos incompletos devido a ambiguidades não resolvidas
- Pode inventar elementos não mencionados no cenário
- Pode ter menor conformidade devido à falta de clarificação

### 4.2 Abordagem Interativa (Elicitação Guiada)

#### Descrição
Processo em duas fases onde o LLM primeiro gera perguntas de clarificação, e depois gera o modelo usando as respostas fornecidas.

#### Processo - Fase 1: Geração de Perguntas
1. **Input**: Cenário de requisitos em linguagem natural
2. **Prompt**: Template contendo:
   - Explicação sobre notação iStar 2.0
   - Cenário de requisitos
   - Instruções para gerar 5-8 perguntas de clarificação
   - Foco em: atores, goals, softgoals, tasks, dependencies
3. **Output**: Lista de 5-8 perguntas numeradas

#### Processo - Fase 2: Geração do Modelo
1. **Input**: 
   - Cenário original
   - Perguntas geradas
   - Respostas do usuário
2. **Prompt**: Template contendo:
   - Explicação sobre notação iStar 2.0
   - Cenário original
   - Perguntas e respostas
   - Instruções para gerar modelo completo
   - Especificação do formato JSON (Pistar 2.0.0)
   - Constraints e regras
3. **Output**: Modelo iStar 2.0 em formato JSON

#### Características
- **Duas interações** com o LLM
- **Clarificação prévia** de ambiguidades
- **Geração informada** do modelo final
- **Mais interativo** e colaborativo

#### Vantagens Esperadas
- Redução de ambiguidades através de perguntas direcionadas
- Maior completude devido a informações adicionais
- Melhor conformidade devido a clarificações específicas
- Processo mais próximo da elicitação tradicional

## 5. Conhecimento Incluído nos Prompts

### 5.1 Explicação sobre iStar 2.0

Todos os prompts incluem uma breve explicação sobre:
- **Conceito**: iStar 2.0 é uma notação para modelagem de requisitos orientada a objetivos
- **Elementos Principais**:
  - **Actors**: Agentes do sistema (humanos, sistemas, organizações)
    - Tipos: `istar.Agent`, `istar.Role`, `istar.Actor`
  - **Goals**: Objetivos que atores desejam alcançar (`istar.Goal`)
  - **Softgoals/Qualities**: Critérios de qualidade (`istar.Quality`)
  - **Tasks**: Atividades específicas para alcançar goals (`istar.Task`)
  - **Resources**: Recursos necessários (`istar.Resource`)
  - **Dependencies**: Relações de dependência entre atores
  - **Links**: Conexões entre elementos (refinamento, contribuição, etc.)

### 5.2 Contexto do Domínio

Quando aplicável, prompts incluem:
- Informações sobre o domínio do cenário
- Terminologia específica
- Padrões comuns do domínio

### 5.3 Constraints de Estrutura

Todos os prompts especificam:
- **Formato JSON exato**: Estrutura Pistar 2.0.0 (ver `ISTAR_2_0_JSON_STRUCTURE.md`)
- **Regras obrigatórias**:
  - `tool` deve ser `"pistar.2.0.0"`
  - `istar` deve ser `"2.0"`
  - IDs devem ser únicos (UUIDs)
  - source/target devem referir a IDs existentes
- **Restrições**:
  - Não inventar elementos não mencionados
  - Usar apenas informações do cenário (e respostas, se interativo)

## 6. Seleção e Preparação de Cenários

### 6.1 Critérios de Seleção

Cenários devem:
- Ser **representativos** de problemas reais de requisitos
- Ter **ambiguidades intencionais** apropriadas (não excessivas)
- Ser **compreensíveis** para avaliadores
- **Variar em domínio** (transporte, educação, saúde, etc.)
- **Variar em complexidade** (simples, médio, complexo)
- Ter **tamanho gerenciável** (200-500 palavras)

### 6.2 Ambiguidades Intencionais

Cenários incluem ambiguidades em:
- **Atores**: Não explicitamente definidos ou implícitos
- **Metas**: Objetivos vagos ou implícitos
- **Softgoals**: Critérios de qualidade não especificados
- **Tarefas**: Processos incompletos ou vagos
- **Dependências**: Relações não claras entre atores

### 6.3 Modelos de Referência (Gold Standard)

Para cada cenário:
- Criar modelo iStar 2.0 manualmente
- Incluir todos os elementos esperados
- Validar conformidade com iStar 2.0
- Documentar decisões de modelagem
- Usar como referência para avaliação

## 7. Processo de Execução

### 7.1 Fase de Preparação

1. Criar/validar cenários de requisitos
2. Desenvolver prompts baseline e interativos
3. Criar modelos de referência (gold standard)
4. Configurar ambiente de experimentação
5. Preparar scripts e ferramentas

### 7.2 Fase de Execução Baseline

1. Para cada cenário:
   - Carregar cenário
   - Preparar prompt baseline
   - Executar geração com LLM
   - Validar e armazenar modelo gerado
   - Registrar logs e metadados

### 7.3 Fase de Execução Interativa

1. Para cada cenário:
   - **Fase 1**: Gerar perguntas
     - Carregar cenário
     - Preparar prompt de perguntas
     - Executar geração de perguntas
     - Processar e validar perguntas
   - **Fase 2**: Coletar respostas
     - Apresentar perguntas ao usuário
     - Coletar respostas
     - Validar respostas
   - **Fase 3**: Gerar modelo
     - Preparar prompt com cenário + perguntas + respostas
     - Executar geração do modelo
     - Validar e armazenar modelo gerado
     - Registrar logs e metadados

### 7.4 Fase de Avaliação

1. Calcular métricas quantitativas
2. Coletar avaliações de especialistas
3. Comparar com modelos de referência
4. Analisar qualidade das perguntas (interativo)

### 7.5 Fase de Análise

1. Análise estatística comparativa
2. Interpretação de resultados
3. Documentação completa
4. Preparação de visualizações

## 8. Considerações Éticas

- **Transparência**: Documentar claramente o uso de LLMs
- **Reprodutibilidade**: Garantir que experimentos sejam reproduzíveis
- **Validação**: Validar modelos gerados com especialistas
- **Bias**: Considerar possíveis vieses dos LLMs
- **Custos**: Monitorar custos de uso de APIs

## 9. Limitações do Estudo

- **Número limitado de cenários**: 3-5 cenários
- **Avaliação manual**: Requer especialistas humanos
- **Dependência de LLM**: Resultados dependem do modelo LLM usado
- **Subjetividade**: Algumas métricas são subjetivas (clareza)
- **Custos**: Abordagem interativa requer mais chamadas de API

## 10. Contribuições Esperadas

1. **Metodológica**: Proposta de abordagem interativa para elicitação com LLMs
2. **Empírica**: Evidência sobre efetividade de abordagens de prompting
3. **Prática**: Insights para uso de LLMs em Engenharia de Requisitos
4. **Técnica**: Templates de prompts e processos validados

## 11. Referências Metodológicas

- Design experimental comparativo
- Engenharia de Requisitos orientada a objetivos
- Prompt Engineering para LLMs
- Avaliação de qualidade de modelos de requisitos
- Notação iStar 2.0 e Pistar 2.0.0

---

**Documento criado em**: 2024-12-01  
**Versão**: 1.0  
**Status**: Base metodológica do projeto




