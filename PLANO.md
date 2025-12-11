# Plano Inicial do Projeto I See Stars

## 📋 Visão Geral

Este documento apresenta o plano inicial e a estrutura organizacional do projeto **I See Stars**, um sistema que utiliza Large Language Models (LLMs) para transformar requisitos em linguagem natural em modelos iStar 2.0 estruturados em JSON, através de uma abordagem interativa de elicitação de requisitos.

---

## 🎯 Objetivos do Projeto

1. **Transformação Automática**: Converter requisitos informais em modelos iStar 2.0 estruturados
2. **Elicitação Interativa**: Implementar um processo onde o LLM faz perguntas de clarificação antes de gerar o modelo final
3. **Avaliação Comparativa**: Comparar a abordagem interativa com uma abordagem baseline (zero-shot)
4. **Geração Estruturada**: Produzir modelos em formato JSON para facilitar análise e visualização

---

## 🏗️ Estrutura do Projeto

### Diretórios Principais

```
iSeeStars-LLM4RE/
├── /prompts          # Templates e estratégias de prompt
├── /experiments      # Scripts e configurações de experimentos
├── /models           # Modelos iStar 2.0 gerados (JSON)
├── /evaluation       # Métricas, análises e resultados
├── /interface        # Interface guiada para elicitação interativa
├── /docs             # Documentação, relatórios e metodologia
└── /scenarios        # Cenários de requisitos em linguagem natural
```

---

## 📂 Descrição dos Diretórios

### `/prompts`
**Propósito**: Armazenar todos os templates de prompts utilizados no projeto.

**Conteúdo**:
- Prompts para abordagem baseline (zero-shot)
- Prompts para abordagem interativa (etapa de perguntas)
- Prompts para geração final do modelo
- Templates com explicações sobre notação iStar 2.0
- Variações de prompts para diferentes domínios

**Uso no Ciclo de Vida**:
- **Fase de Design**: Criação e refinamento dos prompts
- **Fase de Experimentação**: Aplicação dos prompts nos experimentos
- **Fase de Análise**: Comparação de diferentes estratégias de prompt

---

### `/experiments`
**Propósito**: Conter scripts, configurações e pipelines de experimentação.

**Conteúdo**:
- Scripts Python para execução de experimentos
- Configurações de modelos LLM (temperatura, tokens, etc.)
- Pipelines de processamento (baseline vs. interativo)
- Logs de execução
- Configurações de ambiente

**Uso no Ciclo de Vida**:
- **Fase de Implementação**: Desenvolvimento dos scripts
- **Fase de Execução**: Rodar experimentos com diferentes cenários
- **Fase de Reprodução**: Garantir reprodutibilidade dos resultados

---

### `/models`
**Propósito**: Armazenar os modelos iStar 2.0 gerados em formato JSON.

**Conteúdo**:
- Modelos gerados pela abordagem baseline
- Modelos gerados pela abordagem interativa
- Modelos de referência (gold standard) criados manualmente
- Versões diferentes do mesmo cenário (para análise de variação)

**Estrutura de Nomenclatura Sugerida**:
- `{cenario}_{abordagem}_{timestamp}.json`
- Exemplo: `taxi_app_baseline_20241201.json`

**Uso no Ciclo de Vida**:
- **Fase de Geração**: Armazenar outputs dos LLMs
- **Fase de Avaliação**: Comparar modelos gerados com referência
- **Fase de Análise**: Estudar padrões e diferenças entre abordagens

---

### `/evaluation`
**Propósito**: Métricas, análises quantitativas e qualitativas dos resultados.

**Conteúdo**:
- Scripts de cálculo de métricas (completude, conformidade, etc.)
- Resultados de avaliação por especialistas
- Análises comparativas entre abordagens
- Gráficos e visualizações
- Tabelas de resultados

**Métricas Principais**:
- **Completude**: Cobertura de atores, metas, softgoals, tarefas
- **Conformidade**: Aderência à notação iStar 2.0
- **Qualidade das Perguntas**: Relevância e utilidade das perguntas de clarificação

**Uso no Ciclo de Vida**:
- **Fase de Avaliação**: Calcular métricas automáticas
- **Fase de Análise**: Processar feedback de especialistas
- **Fase de Relatório**: Gerar visualizações e tabelas

---

### `/interface`
**Propósito**: Interface guiada para suportar o processo interativo de elicitação.

**Conteúdo**:
- Interface web ou CLI para interação com o usuário
- Fluxo de perguntas e respostas
- Visualização de modelos gerados
- Exportação de resultados

**Funcionalidades Principais**:
- Apresentar perguntas de clarificação do LLM
- Coletar respostas do usuário
- Exibir modelo gerado em formato legível
- Permitir edição e refinamento

**Uso no Ciclo de Vida**:
- **Fase de Design**: Prototipagem da interface
- **Fase de Teste**: Validação com usuários reais
- **Fase de Execução**: Suporte aos experimentos interativos

---

### `/docs`
**Propósito**: Documentação completa do projeto, metodologia e resultados.

**Conteúdo**:
- Relatório final de pesquisa
- Documentação da metodologia
- Análise detalhada dos resultados
- Referências bibliográficas
- Apresentações e materiais de divulgação

**Documentos Principais**:
- Metodologia detalhada
- Análise comparativa das abordagens
- Discussão sobre qualidade das perguntas
- Limitações e trabalhos futuros

**Uso no Ciclo de Vida**:
- **Fase de Planejamento**: Documentar metodologia
- **Fase de Execução**: Registrar decisões e observações
- **Fase Final**: Consolidar resultados e conclusões

---

### `/scenarios`
**Propósito**: Cenários de requisitos em linguagem natural usados nos experimentos.

**Conteúdo**:
- Cenários intencionalmente ambíguos para estimular clarificação
- Diferentes domínios (aplicativo de táxi, biblioteca, sistema médico, etc.)
- Versões anotadas com informações adicionais
- Metadados sobre cada cenário (complexidade, domínio, etc.)

**Estrutura Sugerida**:
- Um arquivo por cenário (`.txt` ou `.md`)
- Arquivo de metadados (`scenarios_metadata.json`)

**Uso no Ciclo de Vida**:
- **Fase de Preparação**: Seleção e preparação dos cenários
- **Fase de Execução**: Input para os experimentos
- **Fase de Análise**: Contexto para interpretação dos resultados

---

## 🔄 Ciclo de Vida do Projeto

### Fase 1: Preparação
- **Atividades**:
  - Criar cenários de requisitos (`/scenarios`)
  - Desenvolver prompts iniciais (`/prompts`)
  - Preparar modelos de referência (`/models`)

### Fase 2: Design e Implementação
- **Atividades**:
  - Refinar prompts baseado em testes iniciais (`/prompts`)
  - Desenvolver scripts de experimentação (`/experiments`)
  - Prototipar interface interativa (`/interface`)

### Fase 3: Execução
- **Atividades**:
  - Executar experimentos baseline (`/experiments`)
  - Executar experimentos interativos (`/experiments`, `/interface`)
  - Armazenar modelos gerados (`/models`)

### Fase 4: Avaliação
- **Atividades**:
  - Calcular métricas automáticas (`/evaluation`)
  - Coletar avaliação de especialistas (`/evaluation`)
  - Comparar abordagens (`/evaluation`)

### Fase 5: Análise e Relatório
- **Atividades**:
  - Analisar resultados (`/evaluation`)
  - Documentar metodologia e resultados (`/docs`)
  - Preparar visualizações e tabelas (`/docs`, `/evaluation`)

---

## 📊 Fluxo de Dados

```
/scenarios (input)
    ↓
/prompts (processamento)
    ↓
/experiments (execução)
    ↓
/models (output)
    ↓
/evaluation (análise)
    ↓
/docs (documentação)
```

**Interface Interativa** (`/interface`) atua como orquestrador durante a fase interativa, conectando prompts, experimentos e armazenamento de modelos.

---

## 🎓 Considerações Metodológicas

### Reprodutibilidade
- Todos os experimentos devem ser reproduzíveis
- Configurações salvas em `/experiments`
- Versões de prompts documentadas em `/prompts`

### Versionamento
- Modelos gerados com timestamps
- Prompts versionados
- Resultados de avaliação rastreáveis

### Validação
- Modelos de referência criados manualmente
- Múltiplos avaliadores para reduzir viés
- Métricas objetivas e subjetivas

---

## 📅 Próximos Passos

1. **Preparação de Cenários**: Criar 3-5 cenários de requisitos
2. **Desenvolvimento de Prompts**: Criar templates para ambas as abordagens
3. **Configuração de Ambiente**: Preparar scripts e dependências
4. **Testes Iniciais**: Validar pipeline com um cenário piloto
5. **Execução Completa**: Rodar todos os experimentos
6. **Avaliação**: Coletar métricas e feedback
7. **Documentação**: Consolidar resultados e escrever relatório

---

## 📝 Notas

- Este é um projeto de pesquisa, focado em metodologia e experimentação
- Não há necessidade de implementação de sistema de produção
- O foco está na comparação de abordagens de prompting
- Resultados serão documentados para publicação acadêmica




