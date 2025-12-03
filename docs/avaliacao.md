# Guia de Avaliação - I See Stars

## 1. Visão Geral

Este documento descreve o processo completo de avaliação dos modelos iStar 2.0 gerados no projeto I See Stars, incluindo métricas, critérios e procedimentos de avaliação.

## 2. Objetivos da Avaliação

### 2.1 Objetivos Principais

1. **Comparar Abordagens**: Avaliar diferenças entre abordagens baseline e interativa
2. **Medir Qualidade**: Quantificar qualidade dos modelos gerados
3. **Identificar Padrões**: Descobrir padrões de sucesso e falha
4. **Validar Hipóteses**: Testar hipóteses sobre efetividade da abordagem interativa

### 2.2 Critérios de Avaliação

- **Completude**: Modelo captura todos os elementos esperados?
- **Clareza**: Elementos são claros e bem definidos?
- **Conformidade**: Modelo segue notação iStar 2.0 corretamente?
- **Qualidade das Perguntas**: Perguntas são relevantes e úteis? (apenas interativo)

## 3. Métricas de Avaliação

### 3.1 Métrica 1: Completude

#### 3.1.1 Definição

Completude mede a extensão em que o modelo gerado captura todos os elementos esperados do modelo de referência (gold standard).

#### 3.1.2 Elementos Avaliados

- **Atores (Actors)**: Agentes identificados no modelo
- **Metas (Goals)**: Objetivos identificados
- **Softgoals/Qualities**: Critérios de qualidade identificados
- **Tarefas (Tasks)**: Atividades identificadas
- **Recursos (Resources)**: Recursos identificados
- **Dependências (Dependencies)**: Relações de dependência identificadas
- **Links**: Conexões entre elementos identificadas

#### 3.1.3 Cálculo

Para cada tipo de elemento:

```
Completude_Elemento = (Elementos_Corretos_Identificados / Elementos_Esperados) × 100%
```

**Elementos Corretos**: Elementos do modelo gerado que correspondem a elementos do modelo de referência.

**Matching de Elementos**:
- **Match Exato**: Nome/id idêntico
- **Match Semântico**: Significado equivalente (avaliação manual)

**Completude Geral**:
```
Completude_Geral = Média(Completude_Atores, Completude_Goals, Completude_Softgoals, Completude_Tasks, Completude_Dependencies, Completude_Links)
```

#### 3.1.4 Exemplo

**Modelo de Referência**:
- Atores: 3 (passenger, driver, system)
- Goals: 5
- Softgoals: 2
- Tasks: 4
- Dependencies: 3

**Modelo Gerado**:
- Atores: 2 (passenger, driver) → Completude: 2/3 = 66.7%
- Goals: 4 → Completude: 4/5 = 80%
- Softgoals: 1 → Completude: 1/2 = 50%
- Tasks: 3 → Completude: 3/4 = 75%
- Dependencies: 2 → Completude: 2/3 = 66.7%

**Completude Geral**: (66.7 + 80 + 50 + 75 + 66.7) / 5 = 67.7%

#### 3.1.5 Implementação

- Script: `/evaluation/metrics/completeness_calculator.py`
- Input: Modelo gerado + Modelo de referência
- Output: Completude por elemento + Completude geral
- Salvar em: `/evaluation/results/completeness_{scenario_id}_{approach}.json`

### 3.2 Métrica 2: Clareza

#### 3.2.1 Definição

Clareza mede quão claros e bem definidos são os elementos do modelo, avaliando se são compreensíveis e não ambíguos.

#### 3.2.2 Aspectos Avaliados

- **Nomes de Elementos**: Claros e descritivos?
- **Relações**: Bem definidas e compreensíveis?
- **Estrutura**: Organizada e lógica?
- **Contexto**: Suficiente para compreensão?

#### 3.2.3 Processo de Avaliação

**Avaliação por Especialistas**:

1. **Preparação**
   - Modelo gerado apresentado a especialistas
   - Modelo de referência disponível para comparação
   - Formulário de avaliação preparado

2. **Avaliação Individual**
   - Cada especialista avalia independentemente
   - Escala Likert (1-5) para cada aspecto:
     - **Nomes**: 1=confusos, 5=muito claros
     - **Relações**: 1=ambíguas, 5=muito claras
     - **Estrutura**: 1=confusa, 5=muito lógica
     - **Contexto**: 1=insuficiente, 5=suficiente

3. **Agregação**
   - Calcular média das avaliações
   - Calcular inter-avaliador agreement (se múltiplos avaliadores)
   - Identificar consenso e divergências

#### 3.2.4 Cálculo

```
Score_Clareza = Média(Avaliação_Nomes, Avaliação_Relações, Avaliação_Estrutura, Avaliação_Contexto)
```

**Score Final**: Média dos scores de todos os especialistas

#### 3.2.5 Análise Qualitativa

- Coletar comentários qualitativos dos especialistas
- Identificar padrões de problemas de clareza
- Categorizar tipos de ambiguidade encontrados
- Documentar exemplos de elementos claros e confusos

#### 3.2.6 Implementação

- Formulário: `/evaluation/expert_evaluations/clarity_form.md`
- Script: `/evaluation/metrics/clarity_analyzer.py`
- Salvar em: `/evaluation/results/clarity_{scenario_id}_{approach}.json`

### 3.3 Métrica 3: Conformidade com iStar 2.0

#### 3.3.1 Definição

Conformidade mede a aderência do modelo à especificação da notação iStar 2.0 (Pistar 2.0.0).

#### 3.3.2 Aspectos Avaliados

- **Estrutura JSON**: Conforme schema Pistar 2.0.0?
- **Tipos de Elementos**: Tipos válidos?
- **Integridade Referencial**: IDs válidos e referências corretas?
- **Regras da Notação**: Segue regras do iStar 2.0?

#### 3.3.3 Validação Estrutural

**Campos Obrigatórios**:
- [ ] `actors` (array)
- [ ] `orphans` (array)
- [ ] `dependencies` (array)
- [ ] `links` (array)
- [ ] `display` (object)
- [ ] `tool` = `"pistar.2.0.0"`
- [ ] `istar` = `"2.0"`
- [ ] `saveDate` (string)
- [ ] `diagram` (object)

**Estrutura de Atores**:
- [ ] `id` (string, único)
- [ ] `text` (string)
- [ ] `type` (`istar.Actor` | `istar.Agent` | `istar.Role`)
- [ ] `x`, `y` (numbers)
- [ ] `nodes` (array)

**Estrutura de Nodes**:
- [ ] `id` (string, único)
- [ ] `text` (string)
- [ ] `type` (`istar.Goal` | `istar.Task` | `istar.Quality` | `istar.Resource`)
- [ ] `x`, `y` (numbers)

**Estrutura de Dependencies**:
- [ ] `id` (string, único)
- [ ] `text` (string)
- [ ] `type` (válido)
- [ ] `x`, `y` (numbers)
- [ ] `source` (ID de ator existente)
- [ ] `target` (ID de ator existente)

**Estrutura de Links**:
- [ ] `id` (string, único)
- [ ] `type` (tipo válido)
- [ ] `source` (ID existente)
- [ ] `target` (ID existente)
- [ ] `label` (opcional)

#### 3.3.4 Validação de Integridade Referencial

- [ ] Todos os IDs são únicos
- [ ] Todos os `source` e `target` em dependencies referem a IDs de atores existentes
- [ ] Todos os `source` e `target` em links referem a IDs existentes
- [ ] Todos os nodes estão dentro de atores (não em orphans, a menos que necessário)

#### 3.3.5 Validação de Regras iStar 2.0

- [ ] Tipos de atores são válidos
- [ ] Tipos de nodes são válidos
- [ ] Tipos de links são válidos
- [ ] Dependencies conectam atores corretamente
- [ ] Links conectam elementos corretamente

#### 3.3.6 Cálculo

```
Conformidade = (Regras_Válidas / Total_de_Regras) × 100%
```

**Classificação**:
- **Válido**: 100% de conformidade
- **Parcialmente Válido**: 80-99% de conformidade
- **Inválido**: < 80% de conformidade

#### 3.3.7 Implementação

- Script: `/evaluation/metrics/conformance_validator.py`
- Schema: `/experiments/utils/istar_schema.json`
- Salvar em: `/evaluation/results/conformance_{scenario_id}_{approach}.json`

### 3.4 Métrica 4: Qualidade das Perguntas (Apenas Interativo)

#### 3.4.1 Definição

Avalia a relevância e utilidade das perguntas geradas na abordagem interativa.

#### 3.4.2 Aspectos Avaliados

- **Relevância**: Pergunta é relevante para o modelo?
- **Especificidade**: Pergunta é específica o suficiente?
- **Utilidade**: Resposta ajudou a melhorar o modelo?

#### 3.4.3 Categorização

Categorizar cada pergunta por tipo:
- **Atores**: Perguntas sobre atores do sistema
- **Goals**: Perguntas sobre objetivos
- **Softgoals**: Perguntas sobre critérios de qualidade
- **Tasks**: Perguntas sobre tarefas
- **Dependencies**: Perguntas sobre dependências
- **Outras**: Perguntas não categorizadas

#### 3.4.4 Avaliação por Especialistas

Especialistas avaliam cada pergunta em escala Likert (1-5):

- **Relevância**: 1=irrelevante, 5=muito relevante
- **Especificidade**: 1=vaga, 5=muito específica
- **Utilidade**: 1=não útil, 5=muito útil

#### 3.4.5 Análise de Impacto

- Comparar modelo gerado com e sem respostas
- Identificar quais perguntas levaram a melhorias no modelo
- Calcular correlação entre qualidade da pergunta e melhoria do modelo

#### 3.4.6 Cálculo

```
Score_Qualidade_Pergunta = Média(Relevância, Especificidade, Utilidade)
Score_Geral_Perguntas = Média(Scores de todas as perguntas)
```

#### 3.4.7 Implementação

- Script: `/evaluation/metrics/question_quality_analyzer.py`
- Salvar em: `/evaluation/results/question_quality_{scenario_id}.json`

## 4. Comparação de Abordagens

### 4.1 Comparação Quantitativa

#### 4.1.1 Completude

- Calcular completude de baseline vs. referência
- Calcular completude de interativo vs. referência
- Calcular diferença: `Completude_Interativo - Completude_Baseline`
- Testar significância estatística (se aplicável)

#### 4.1.2 Número de Elementos

- Contar elementos em cada modelo
- Calcular diferenças absolutas e percentuais
- Identificar quais tipos de elementos têm maior diferença

#### 4.1.3 Conformidade

- Comparar scores de conformidade
- Identificar tipos de erros mais comuns em cada abordagem
- Calcular taxa de modelos válidos vs. inválidos

### 4.2 Comparação Qualitativa

#### 4.2.1 Elementos Faltantes

- Identificar elementos no referência que estão:
  - Presentes em ambos (baseline e interativo)
  - Presentes apenas no interativo
  - Presentes apenas no baseline
  - Ausentes em ambos

#### 4.2.2 Elementos Incorretos

- Identificar elementos incorretos ou mal definidos
- Comparar frequência entre abordagens
- Categorizar tipos de erros

#### 4.2.3 Clareza

- Comparar scores de clareza
- Identificar padrões de problemas
- Analisar comentários qualitativos

### 4.3 Análise Estatística

#### 4.3.1 Estatísticas Descritivas

Para cada métrica:
- Média
- Mediana
- Desvio padrão
- Mínimo e máximo
- Separar por abordagem

#### 4.3.2 Testes Estatísticos

Se múltiplos cenários:
- Teste t de Student (se distribuição normal)
- Teste de Wilcoxon (se não normal)
- Análise de variância (ANOVA) se múltiplos fatores
- Calcular tamanho do efeito (Cohen's d)

### 4.4 Análise por Cenário

- Para cada cenário individualmente:
  - Comparar métricas
  - Identificar padrões específicos
  - Documentar observações
- Identificar se há diferenças por domínio ou complexidade

## 5. Processo de Avaliação

### 5.1 Fase 1: Avaliação Automática

1. **Validação Estrutural**
   - Validar JSON contra schema
   - Verificar campos obrigatórios
   - Classificar: válido, parcialmente válido, inválido

2. **Cálculo de Métricas Quantitativas**
   - Completude
   - Conformidade
   - Número de elementos

3. **Geração de Relatórios**
   - Relatório por modelo
   - Relatório comparativo
   - Identificação de problemas

### 5.2 Fase 2: Avaliação por Especialistas

1. **Preparação**
   - Selecionar especialistas (mínimo 2)
   - Preparar materiais (modelos, formulários)
   - Agendar sessões de avaliação

2. **Avaliação**
   - Especialistas avaliam modelos cegamente (sem saber abordagem)
   - Avaliam em escala Likert
   - Fornecem comentários qualitativos

3. **Agregação**
   - Calcular médias
   - Calcular inter-avaliador agreement
   - Identificar consenso e divergências

### 5.3 Fase 3: Análise Comparativa

1. **Comparação de Métricas**
   - Comparar baseline vs. interativo
   - Identificar diferenças significativas
   - Calcular melhorias percentuais

2. **Análise de Padrões**
   - Identificar padrões de sucesso
   - Identificar padrões de falha
   - Categorizar tipos de problemas

3. **Interpretação**
   - Interpretar resultados
   - Relacionar com hipóteses
   - Identificar limitações

## 6. Critérios de Sucesso

### 6.1 Critérios Quantitativos

- **Completude**: Interativo tem ≥ 10% mais completude que baseline
- **Conformidade**: ≥ 95% dos modelos passam validação estrutural
- **Clareza**: Interativo tem score ≥ 0.5 pontos maior (escala 1-5)

### 6.2 Critérios Qualitativos

- **Consenso**: Especialistas preferem interativo em ≥ 70% dos casos
- **Utilidade**: Perguntas são avaliadas como relevantes (≥ 4.0 em escala 1-5)
- **Melhoria**: Modelos interativos são consistentemente melhores

## 7. Visualizações

### 7.1 Gráficos Comparativos

- Gráfico de barras: Completude (baseline vs. interativo)
- Gráfico de barras: Clareza (baseline vs. interativo)
- Gráfico de barras: Conformidade (baseline vs. interativo)
- Gráfico de linha: Completude por tipo de elemento

### 7.2 Heatmaps

- Heatmap: Métricas por cenário
- Heatmap: Diferenças por tipo de elemento

### 7.3 Distribuições

- Box plot: Distribuição de métricas
- Histograma: Distribuição de scores

## 8. Relatórios

### 8.1 Relatório por Modelo

- Métricas calculadas
- Problemas identificados
- Classificação (válido/parcial/inválido)

### 8.2 Relatório Comparativo

- Comparação de abordagens
- Análise estatística
- Interpretação de resultados

### 8.3 Relatório Final

- Resumo executivo
- Resultados detalhados
- Discussão
- Conclusões

---

**Documento criado em**: 2024-12-01  
**Versão**: 1.0  
**Status**: Guia de avaliação completo

