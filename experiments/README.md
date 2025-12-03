# 🧪 Diretório: Experiments

## Propósito

Este diretório contém scripts, configurações e pipelines para execução dos experimentos do projeto. Aqui estão os códigos que orquestram a interação com LLMs e processam os resultados.

## Estrutura Sugerida

```
experiments/
├── scripts/
│   ├── baseline_experiment.py
│   ├── interactive_experiment.py
│   ├── batch_processor.py
│   └── result_validator.py
├── config/
│   ├── llm_config.json
│   ├── experiment_params.yaml
│   └── api_keys.env.example
├── logs/
│   └── experiment_logs/
└── utils/
    ├── istar_validator.py
    └── json_parser.py
```

## Uso no Ciclo de Vida do Projeto

### Fase 1: Preparação
- Configurar ambiente e dependências
- Preparar scripts de processamento básico
- Testar conexão com APIs de LLM

### Fase 2: Desenvolvimento
- Implementar pipeline baseline
- Implementar pipeline interativo
- Criar utilitários de validação e parsing

### Fase 3: Execução
- Rodar experimentos com todos os cenários
- Registrar logs de execução
- Monitorar custos e performance

### Fase 4: Reprodução
- Garantir que experimentos são reproduzíveis
- Documentar dependências e versões
- Criar scripts de re-execução

## Componentes Principais

### Scripts de Experimentação
- **baseline_experiment.py**: Executa abordagem zero-shot
- **interactive_experiment.py**: Executa abordagem interativa completa
- **batch_processor.py**: Processa múltiplos cenários em lote

### Configurações
- Parâmetros do LLM (modelo, temperatura, max_tokens)
- Configurações de API (timeout, retry logic)
- Paths e diretórios

### Utilitários
- Validação de JSON iStar 2.0
- Parsing e normalização de outputs
- Geração de logs estruturados

## Boas Práticas

1. **Reprodutibilidade**
   - Usar seeds para aleatoriedade
   - Salvar todas as configurações
   - Versionar código e dependências

2. **Logging**
   - Registrar todas as chamadas de API
   - Salvar inputs e outputs completos
   - Timestamps e metadados

3. **Tratamento de Erros**
   - Retry logic para falhas de API
   - Validação de outputs antes de salvar
   - Fallbacks para casos de erro

4. **Segurança**
   - Nunca commitar API keys
   - Usar variáveis de ambiente
   - Exemplo de arquivo .env

## Dependências Sugeridas

- `openai` ou `anthropic`: Clientes de API
- `python-dotenv`: Gerenciamento de variáveis de ambiente
- `jsonschema`: Validação de JSON
- `pandas`: Processamento de dados
- `tqdm`: Barras de progresso

## Notas

- Todos os scripts devem ser documentados
- Configurações devem ser versionadas
- Logs devem ser mantidos para análise posterior

