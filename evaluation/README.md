# 📊 Diretório: Evaluation

## Propósito

Este diretório contém scripts, métricas e análises para avaliar a qualidade dos modelos gerados, comparando abordagens baseline e interativa.

## Estrutura Sugerida

```
evaluation/
├── metrics/
│   ├── completeness_calculator.py
│   ├── conformance_validator.py
│   └── question_quality_analyzer.py
├── results/
│   ├── quantitative_results.csv
│   ├── qualitative_results.json
│   └── comparison_tables/
├── visualizations/
│   ├── completeness_comparison.png
│   ├── conformance_scores.png
│   └── question_analysis.png
├── expert_evaluations/
│   ├── evaluator_1_results.json
│   ├── evaluator_2_results.json
│   └── consensus_analysis.json
└── reports/
    └── evaluation_summary.md
```

## Uso no Ciclo de Vida do Projeto

### Fase 1: Preparação
- Definir métricas a serem calculadas
- Criar scripts de cálculo automático
- Preparar formulários para avaliação de especialistas

### Fase 2: Execução
- Calcular métricas quantitativas
- Coletar avaliações de especialistas
- Processar dados brutos

### Fase 3: Análise
- Comparar abordagens baseline vs. interativa
- Identificar padrões e correlações
- Gerar visualizações

### Fase 4: Consolidação
- Criar tabelas comparativas
- Preparar relatório de avaliação
- Documentar conclusões

## Métricas Implementadas

### 1. Completude (Completeness)
- **Cobertura de Atores**: % de atores identificados vs. esperado
- **Cobertura de Metas**: % de metas identificadas vs. esperado
- **Cobertura de Softgoals**: % de softgoals identificados vs. esperado
- **Cobertura de Tarefas**: % de tarefas identificadas vs. esperado
- **Cobertura de Dependências**: % de dependências identificadas vs. esperado

### 2. Conformidade (Conformance)
- **Validação Estrutural**: Conformidade com schema JSON
- **Validação de Tipos**: Tipos corretos de elementos
- **Integridade Referencial**: IDs válidos e referências corretas
- **Conformidade iStar 2.0**: Aderência à especificação da notação

### 3. Qualidade das Perguntas (Interactive Only)
- **Número de Perguntas**: Quantidade gerada
- **Categorização**: Distribuição por tipo (atores, metas, etc.)
- **Relevância**: Avaliação manual de utilidade
- **Especificidade**: Quão específicas são as perguntas

## Avaliação por Especialistas

### Critérios Qualitativos
1. **Completude Percebida**: O modelo captura todos os elementos importantes?
2. **Correção**: Os elementos estão corretos e bem definidos?
3. **Clareza**: O modelo é fácil de entender?
4. **Utilidade das Perguntas**: As perguntas ajudaram a melhorar o modelo?

### Processo
1. Especialistas avaliam modelos cegamente (sem saber a abordagem)
2. Avaliam em escala Likert (1-5)
3. Fornecem comentários qualitativos
4. Consenso é calculado quando múltiplos avaliadores

## Scripts de Análise

### Cálculo Automático
- Comparação de modelos gerados vs. gold standard
- Cálculo de métricas de completude
- Validação de conformidade estrutural

### Análise Comparativa
- Estatísticas descritivas (média, desvio padrão)
- Testes estatísticos (se aplicável)
- Visualizações comparativas

### Processamento de Avaliações
- Agregação de avaliações de especialistas
- Cálculo de inter-avaliador agreement
- Análise de consenso

## Visualizações

- Gráficos de barras comparativos
- Heatmaps de completude
- Distribuições de scores
- Análise de correlações

## Notas

- Métricas quantitativas são objetivas e reproduzíveis
- Avaliações qualitativas requerem múltiplos avaliadores
- Resultados devem ser estatisticamente significativos (se possível)
- Documentar limitações das métricas

