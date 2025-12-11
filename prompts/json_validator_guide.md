# Guia de Uso - Prompt de Validação de JSON

## Visão Geral

Este prompt valida modelos iStar 2.0 em formato JSON Pistar 2.0.0, identificando problemas e sugerindo correções.

## Quando Usar

Use este prompt quando:
- ✅ Um modelo JSON foi gerado (Etapa 9 da interface)
- ✅ Precisa validar a qualidade e conformidade do modelo
- ✅ Encontrou erros ao tentar usar o modelo
- ✅ Quer garantir que o modelo está correto antes de salvar

## Como Usar

### Passo 1: Obter o JSON
Tenha o JSON do modelo que deseja validar.

### Passo 2: Preencher o Prompt
Substitua `[JSON DO MODELO AQUI]` pelo JSON completo.

### Passo 3: Enviar para o LLM
Envie o prompt preenchido para o LLM (GPT-4, Claude, etc.).

### Passo 4: Analisar o Relatório
O LLM retornará um relatório detalhado com:
- Status geral (Válido/Parcialmente Válido/Inválido)
- Lista de problemas encontrados
- Sugestões de correção
- Estatísticas do modelo

### Passo 5: Aplicar Correções
Use as sugestões para corrigir o JSON.

## Validações Realizadas

### 1. Validação Estrutural
- ✅ JSON sintaticamente válido
- ✅ Campos obrigatórios presentes
- ✅ tool = "pistar.2.0.0"
- ✅ istar = "2.0"

### 2. IDs Únicos
- ✅ Todos os IDs são únicos
- ✅ Não há duplicatas
- ✅ IDs são strings válidas

### 3. Tipos Válidos
- ✅ Tipos de atores válidos
- ✅ Tipos de nodes válidos
- ✅ Tipos de dependencies válidos
- ✅ Tipos de links válidos

### 4. Referências Válidas
- ✅ source/target em dependencies referem a atores existentes
- ✅ source/target em links referem a elementos existentes
- ✅ Não há referências quebradas

### 5. Compatibilidade iStar 2.0
- ✅ Estrutura segue especificação
- ✅ Relações válidas
- ✅ Elementos corretamente organizados

## Exemplo de Uso

### Input (Prompt Preenchido)

```
Você é um validador especializado em modelos iStar 2.0...

MODELO JSON A VALIDAR:

{
  "actors": [
    {
      "id": "actor-passenger",
      "text": "Passenger",
      "type": "istar.Agent",
      "x": 0,
      "y": 0,
      "nodes": [...]
    }
  ],
  ...
}
```

### Output Esperado

```
STATUS GERAL: VÁLIDO

RESUMO:
- Total de problemas encontrados: 0
- Problemas críticos: 0
- Problemas de aviso: 0

PROBLEMAS ENCONTRADOS:
Nenhum problema encontrado.

VALIDAÇÕES REALIZADAS:
✓ JSON sintaticamente válido
✓ Todos os IDs são únicos
✓ Tipos válidos
✓ Referências válidas
✓ Compatibilidade iStar 2.0

ESTATÍSTICAS:
- Total de atores: 3
- Total de nodes: 8
- IDs únicos: sim
- Referências válidas: sim
```

## Exemplo com Erros

### Input (JSON com Erros)

```json
{
  "actors": [
    {
      "id": "actor-001",
      "text": "Passenger",
      "type": "Agent",  // ERRO: deveria ser "istar.Agent"
      ...
    },
    {
      "id": "actor-001",  // ERRO: ID duplicado
      ...
    }
  ],
  "dependencies": [
    {
      "source": "actor-xyz",  // ERRO: ator não existe
      ...
    }
  ]
}
```

### Output Esperado

```
STATUS GERAL: INVÁLIDO

PROBLEMAS ENCONTRADOS:

1. TIPO INVÁLIDO: Ator tem type = "Agent"
   Localização: actors[0].type
   Severidade: ALTO
   Correção: Alterar para "istar.Agent"

2. ID DUPLICADO: Dois atores têm o mesmo ID "actor-001"
   Localização: actors[0].id e actors[1].id
   Severidade: CRÍTICO
   Correção: Alterar um dos IDs para "actor-002"

3. REFERÊNCIA QUEBRADA: Dependency referencia ator inexistente
   Localização: dependencies[0].source
   Severidade: CRÍTICO
   Correção: Verificar ID do ator ou criar o ator faltante
```

## Classificação de Severidade

### CRÍTICO
Problemas que tornam o JSON inválido:
- JSON sintaticamente inválido
- IDs duplicados
- Referências quebradas
- Campos obrigatórios faltando

### ALTO
Problemas que afetam a estrutura:
- Tipos inválidos
- Estrutura incorreta
- Campos obrigatórios de elementos faltando

### MÉDIO
Problemas que podem causar problemas:
- Tipos malformados
- Valores inválidos

### BAIXO
Problemas menores:
- Valores padrão que poderiam ser melhorados
- Otimizações sugeridas

## Integração com Workflow

### Após Geração (Etapa 9)
1. Gerar JSON usando `final_json_generation.txt`
2. Validar usando `json_validator.txt`
3. Aplicar correções se necessário
4. Salvar modelo validado

### Validação Automática
O prompt pode ser usado em scripts de validação automática:
- Após cada geração de modelo
- Antes de salvar modelos
- Em pipelines de validação

## Dicas de Uso

1. **Sempre valide após gerar**: Não assuma que o JSON está correto
2. **Aplique correções sugeridas**: As sugestões são práticas e acionáveis
3. **Valide novamente após correções**: Garanta que as correções não introduziram novos erros
4. **Use em conjunto com validação programática**: Complemente com scripts de validação

## Limitações

- O prompt valida estrutura e conformidade, não valida semântica
- Não valida se o modelo faz sentido do ponto de vista de requisitos
- Foca em conformidade técnica com Pistar 2.0.0

## Troubleshooting

### Se o LLM não encontrar problemas óbvios:
- Verifique se o JSON foi copiado corretamente
- Tente a versão compacta do prompt
- Reformule a solicitação

### Se as sugestões não forem claras:
- Peça exemplos específicos de correção
- Solicite JSON corrigido completo
- Peça explicações mais detalhadas

---

**Use este prompt para garantir qualidade e conformidade dos modelos gerados.**




