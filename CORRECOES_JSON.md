# Correções para Compatibilidade com Ferramenta iStar

## 🔧 Problema Identificado

O JSON gerado pelo LLM não estava carregando na ferramenta iStar porque faltavam campos obrigatórios:

1. **`customProperties`** ausente em atores, nodes e dependencies
2. **IDs** não estavam no formato UUID
3. Campos obrigatórios não estavam sendo gerados corretamente

## ✅ Correções Implementadas

### 1. Atualização dos Prompts

Todos os prompts foram atualizados para incluir:

- **`customProperties`** obrigatório em todos os atores, nodes e dependencies
- **UUIDs** como formato obrigatório para todos os IDs
- Instruções explícitas sobre esses campos

Arquivos atualizados:
- `prompts/baseline_final.txt`
- `prompts/interactive_master.txt`
- `prompts/final_json_generation.txt`
- `prompts/json_validator.txt`

### 2. Atualização da Estrutura JSON

O documento `ISTAR_2_0_JSON_STRUCTURE.md` foi atualizado para refletir:

- Campo `customProperties` obrigatório em todos os elementos
- Formato UUID para IDs
- Exemplos atualizados

### 3. Script de Correção Automática

Criado `fix_json.py` que:

- Converte IDs simples para UUIDs
- Adiciona `customProperties` onde faltar
- Mantém referências (source/target) corretas
- Garante todos os campos obrigatórios

**Uso:**
```bash
python3 fix_json.py <arquivo.json> [arquivo_saida.json]
```

**Exemplo:**
```bash
python3 fix_json.py models/baseline/test_output.json
```

### 4. Integração no Script de Teste

O `test_project.py` agora:

- Corrige automaticamente o JSON após gerar
- Adiciona `customProperties` e converte IDs para UUIDs
- Garante compatibilidade com a ferramenta iStar

## 📋 Estrutura JSON Corrigida

### Atores
```json
{
  "id": "uuid-v4",
  "text": "Nome",
  "type": "istar.Agent",
  "x": 100,
  "y": 100,
  "customProperties": {
    "Description": ""
  },
  "nodes": [...]
}
```

### Nodes
```json
{
  "id": "uuid-v4",
  "text": "Nome",
  "type": "istar.Goal",
  "x": 0,
  "y": 0,
  "customProperties": {
    "Description": ""
  }
}
```

### Dependencies
```json
{
  "id": "uuid-v4",
  "text": "Nome",
  "type": "istar.Goal",
  "x": 300,
  "y": 100,
  "customProperties": {
    "Description": ""
  },
  "source": "uuid-ator-depender",
  "target": "uuid-ator-dependee"
}
```

## 🚀 Como Usar

### Opção 1: Teste Automático (Recomendado)

O script `test_project.py` já corrige automaticamente:

```bash
python3 test_project.py
```

### Opção 2: Correção Manual

Se você já tem um JSON gerado:

```bash
python3 fix_json.py models/baseline/test_output.json
```

Isso criará `models/baseline/test_output_fixed.json` com todas as correções.

### Opção 3: Usar JSON Corrigido

O JSON corrigido deve carregar corretamente na ferramenta iStar.

## ✅ Validação

O JSON corrigido deve ter:

- ✅ Todos os atores com `customProperties`
- ✅ Todos os nodes com `customProperties`
- ✅ Todos os dependencies com `customProperties`
- ✅ Todos os IDs no formato UUID
- ✅ `tool = "pistar.2.0.0"`
- ✅ `istar = "2.0"`
- ✅ Referências (source/target) válidas

## 📝 Notas

- O campo `customProperties` pode estar vazio (`{"Description": ""}`), mas deve existir
- IDs devem ser UUIDs v4 no formato: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- O script de correção mantém todas as referências entre elementos




