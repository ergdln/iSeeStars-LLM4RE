# 🎯 Diretório: Models

## Propósito

Este diretório armazena todos os modelos iStar 2.0 gerados durante os experimentos, incluindo modelos baseline, interativos e modelos de referência (gold standard).

## Estrutura Sugerida

```
models/
├── baseline/
│   ├── scenario_001_taxi_app_baseline_20241201.json
│   ├── scenario_002_library_baseline_20241201.json
│   └── ...
├── interactive/
│   ├── scenario_001_taxi_app_interactive_20241201.json
│   ├── scenario_002_library_interactive_20241201.json
│   └── ...
├── reference/
│   ├── scenario_001_taxi_app_gold_standard.json
│   ├── scenario_002_library_gold_standard.json
│   └── ...
└── metadata/
    └── models_index.json
```

## Uso no Ciclo de Vida do Projeto

### Fase 1: Preparação
- Criar modelos de referência manualmente (gold standard)
- Validar estrutura JSON dos modelos de referência
- Estabelecer nomenclatura consistente

### Fase 2: Geração
- Armazenar outputs dos experimentos baseline
- Armazenar outputs dos experimentos interativos
- Validar estrutura antes de salvar

### Fase 3: Análise
- Comparar modelos gerados com referência
- Identificar padrões e diferenças
- Preparar dados para avaliação

### Fase 4: Documentação
- Manter índice de todos os modelos
- Documentar versões e variações
- Preparar datasets para publicação

## Convenção de Nomenclatura

```
{scenario_id}_{scenario_name}_{approach}_{timestamp}.json
```

Exemplos:
- `scenario_001_taxi_app_baseline_20241201.json`
- `scenario_001_taxi_app_interactive_20241201.json`
- `scenario_001_taxi_app_gold_standard.json`

## Formato dos Modelos

Todos os modelos devem seguir o formato iStar 2.0 em JSON:

```json
{
  "model": {
    "name": "Model Name",
    "actors": [...],
    "goals": [...],
    "softgoals": [...],
    "tasks": [...],
    "dependencies": [...]
  },
  "metadata": {
    "generated_at": "2024-12-01T10:00:00Z",
    "approach": "baseline|interactive",
    "scenario_id": "scenario_001",
    "llm_model": "gpt-4",
    "prompt_version": "v1.0"
  }
}
```

## Validação

- Todos os modelos devem ser validados contra schema JSON
- Verificar integridade referencial (IDs válidos)
- Validar conformidade com notação iStar 2.0

## Metadados

Manter arquivo `models_index.json` com:
- Lista de todos os modelos
- Metadados de cada modelo
- Relações entre modelos (mesmo cenário, diferentes abordagens)

## Notas

- Modelos de referência são criados manualmente por especialistas
- Modelos gerados podem ter múltiplas versões (iterações)
- Manter backup de modelos importantes
- Considerar compressão para modelos grandes




