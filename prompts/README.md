# 📝 Diretório: Prompts

## Propósito

Este diretório contém todos os templates e estratégias de prompts utilizados no projeto I See Stars. Os prompts são fundamentais para guiar o comportamento dos LLMs na transformação de requisitos em modelos iStar 2.0.

## Estrutura Sugerida

```
prompts/
├── baseline/
│   ├── zero_shot_template.md
│   └── domain_specific/
│       ├── taxi_app.md
│       └── library_system.md
├── interactive/
│   ├── question_generation_template.md
│   ├── model_generation_template.md
│   └── domain_specific/
│       └── ...
├── knowledge_base/
│   ├── istar_notation_explanation.md
│   └── domain_context_templates.md
└── variations/
    └── temperature_experiments/
```

## Uso no Ciclo de Vida do Projeto

### Fase 1: Design
- Criar templates iniciais baseados em literatura
- Incluir explicações sobre notação iStar 2.0
- Testar diferentes formulações

### Fase 2: Refinamento
- Iterar sobre prompts baseado em testes piloto
- Ajustar instruções para melhor conformidade
- Criar variações para diferentes domínios

### Fase 3: Experimentação
- Aplicar prompts nos experimentos
- Registrar versões utilizadas
- Documentar parâmetros (temperatura, tokens, etc.)

### Fase 4: Análise
- Comparar efetividade de diferentes prompts
- Identificar padrões de sucesso/falha
- Documentar lições aprendidas

## Componentes de um Prompt

1. **Contexto**: Explicação sobre iStar 2.0 e o domínio
2. **Instruções**: O que o LLM deve fazer
3. **Exemplos**: Casos de uso (few-shot, se aplicável)
4. **Formato de Saída**: Especificação do JSON esperado
5. **Constraints**: Limitações e regras a seguir

## Versionamento

- Usar nomenclatura clara: `v1.0`, `v1.1`, etc.
- Documentar mudanças entre versões
- Manter histórico de efetividade

## Notas

- Prompts devem ser versionados e testados
- Cada prompt deve incluir metadados (data, autor, propósito)
- Considerar diferentes modelos LLM podem precisar de ajustes

