# 📖 Diretório: Scenarios

## Propósito

Este diretório contém os cenários de requisitos em linguagem natural que serão utilizados como input para os experimentos. Estes cenários são intencionalmente ambíguos para estimular o processo de clarificação na abordagem interativa.

## Estrutura Sugerida

```
scenarios/
├── scenario_001_taxi_app.md
├── scenario_002_library_system.md
├── scenario_003_medical_booking.md
├── scenario_004_ecommerce.md
├── scenario_005_social_network.md
├── metadata/
│   └── scenarios_metadata.json
└── annotated/
    └── scenario_001_taxi_app_annotated.md
```

## Uso no Ciclo de Vida do Projeto

### Fase 1: Preparação
- Criar ou selecionar cenários de requisitos
- Identificar ambiguidades intencionais
- Documentar metadados de cada cenário

### Fase 2: Validação
- Revisar cenários com especialistas
- Garantir que ambiguidades são apropriadas
- Validar que cenários são representativos

### Fase 3: Execução
- Usar cenários como input para experimentos
- Manter versões originais intactas
- Registrar variações se necessário

### Fase 4: Análise
- Referenciar cenários na análise de resultados
- Comparar como diferentes cenários performam
- Documentar padrões por domínio

## Características dos Cenários

### 1. Ambiguidade Intencional
Cenários devem conter ambiguidades que estimulem perguntas de clarificação:
- Atores não explicitamente definidos
- Metas implícitas ou vagas
- Processos incompletos
- Dependências não claras

### 2. Variedade de Domínios
Incluir diferentes domínios para generalização:
- **Transporte**: Aplicativo de táxi
- **Educação**: Sistema de biblioteca
- **Saúde**: Sistema de agendamento médico
- **Comércio**: Plataforma e-commerce
- **Social**: Rede social

### 3. Níveis de Complexidade
Variar complexidade:
- **Simples**: Poucos atores, metas claras
- **Médio**: Múltiplos atores, algumas ambiguidades
- **Complexo**: Muitos atores, alta ambiguidade

## Formato dos Cenários

### Estrutura Básica
```markdown
# Scenario 001: Taxi App System

## Description
[Descrição do sistema em linguagem natural]

## Context
[Contexto adicional se necessário]

## Requirements
[Lista de requisitos informais]
```

### Exemplo
```markdown
# Scenario 001: Taxi App System

## Description
A system that allows users to request taxi rides through a mobile application. 
Users can see available drivers and track their ride in real-time. Drivers 
receive ride requests and can accept or decline them. The system handles 
payments and ratings.

## Requirements
- Users need to be able to request rides
- Drivers should be able to see ride requests
- The system should track ride location
- Payments need to be processed
- Users and drivers can rate each other
```

## Metadados dos Cenários

Arquivo `scenarios_metadata.json` deve conter:

```json
{
  "scenario_001": {
    "id": "scenario_001",
    "name": "Taxi App System",
    "domain": "transportation",
    "complexity": "medium",
    "word_count": 250,
    "intentional_ambiguities": [
      "Payment method not specified",
      "Rating criteria unclear",
      "Driver selection process ambiguous"
    ],
    "expected_actors": ["passenger", "driver", "system"],
    "expected_goals": 5,
    "created_at": "2024-12-01",
    "author": "Research Team"
  }
}
```

## Versões Anotadas

Alguns cenários podem ter versões anotadas com:
- Elementos esperados (atores, metas, etc.)
- Perguntas de clarificação sugeridas
- Notas sobre ambiguidades
- Referências a modelos gold standard

## Critérios de Seleção

Cenários devem:
1. Ser representativos de problemas reais
2. Ter ambiguidades apropriadas (não excessivas)
3. Ser compreensíveis para avaliadores
4. Variar em domínio e complexidade
5. Ser de tamanho gerenciável (200-500 palavras)

## Boas Práticas

1. **Clareza Base**: Apesar das ambiguidades, o cenário deve ser compreensível
2. **Realismo**: Baseados em sistemas reais ou plausíveis
3. **Consistência**: Formato e estrutura consistentes
4. **Versionamento**: Manter histórico de mudanças
5. **Validação**: Revisar com especialistas antes de usar

## Notas

- Cenários são inputs críticos - qualidade afeta resultados
- Ambiguidades devem ser intencionais, não acidentais
- Considerar criar cenários em múltiplos idiomas (se aplicável)
- Manter versões originais para reprodutibilidade




