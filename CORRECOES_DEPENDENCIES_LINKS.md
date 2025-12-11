# Correções: Dependencies e Links

## 🔧 Problema Identificado

Após carregar o JSON na ferramenta iStar, aparecia o erro:
```
Unknown element type: istar.DependencyLink. Your model will not load properly.
```

### Causas:

1. **Dependencies com tipo incorreto**: Dependencies estavam usando `type: "istar.DependencyLink"`, mas devem usar `"istar.Goal"`, `"istar.Task"`, `"istar.Quality"` ou `"istar.Resource"`.

2. **Links conectando atores diretamente**: Links estavam conectando atores diretamente, mas devem conectar **nodes** (elementos dentro de atores: goals, tasks, qualities, resources).

## ✅ Correções Implementadas

### 1. Atualização dos Prompts

Todos os prompts foram atualizados com regras explícitas:

**Para Dependencies:**
- `type` DEVE ser: `"istar.Goal"`, `"istar.Task"`, `"istar.Quality"` ou `"istar.Resource"`
- ⚠️ **NUNCA** use `"istar.DependencyLink"` como type de dependency!
- `source` e `target` são IDs de **ATORES** (não nodes)

**Para Links:**
- `source` e `target` são IDs de **NODES** (goals, tasks, qualities, resources)
- ⚠️ **NUNCA** conecte atores diretamente em links!
- Links conectam elementos dentro de atores

Arquivos atualizados:
- `prompts/baseline_final.txt`
- `prompts/interactive_master.txt`
- `prompts/final_json_generation.txt`

### 2. Script de Correção Atualizado

O `fix_json.py` agora:

1. **Corrige tipos de dependencies inválidos:**
   - Se encontrar `type: "istar.DependencyLink"` em uma dependency, muda para `"istar.Goal"` (padrão)

2. **Remove links inválidos:**
   - Remove links que conectam atores diretamente
   - Mantém apenas links que conectam nodes

**Uso:**
```bash
python3 fix_json.py models/baseline/test_output.json
```

### 3. Integração no Script de Teste

O `test_project.py` agora aplica automaticamente essas correções após gerar o JSON.

## 📋 Estrutura Correta

### Dependencies (conectam atores)
```json
{
  "id": "uuid",
  "text": "User depends on Driver for Ride",
  "type": "istar.Goal",  // ✅ Correto: Goal, Task, Quality ou Resource
  "x": 300,
  "y": 100,
  "customProperties": {
    "Description": ""
  },
  "source": "uuid-ator-user",      // ID do ator que depende
  "target": "uuid-ator-driver"     // ID do ator do qual depende
}
```

### Links (conectam nodes)
```json
{
  "id": "uuid",
  "type": "istar.AndRefinementLink",
  "source": "uuid-goal-request-ride",  // ✅ ID de um node (goal)
  "target": "uuid-task-select-dest",  // ✅ ID de um node (task)
  "label": ""
}
```

## ⚠️ Erros Comuns

### ❌ ERRADO - Dependency com tipo DependencyLink
```json
{
  "type": "istar.DependencyLink"  // ❌ ERRADO!
}
```

### ✅ CORRETO - Dependency com tipo Goal/Task/Quality/Resource
```json
{
  "type": "istar.Goal"  // ✅ CORRETO
}
```

### ❌ ERRADO - Link conectando atores
```json
{
  "source": "uuid-ator-user",     // ❌ ERRADO: ID de ator
  "target": "uuid-ator-driver"    // ❌ ERRADO: ID de ator
}
```

### ✅ CORRETO - Link conectando nodes
```json
{
  "source": "uuid-goal-request",  // ✅ CORRETO: ID de node
  "target": "uuid-task-select"     // ✅ CORRETO: ID de node
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

## ✅ Validação

O JSON corrigido deve ter:

- ✅ Dependencies com `type` = Goal, Task, Quality ou Resource (nunca DependencyLink)
- ✅ Links conectando apenas nodes (não atores)
- ✅ Todos os campos obrigatórios presentes
- ✅ Sem erros ao carregar na ferramenta iStar

## 📝 Notas

- **Dependencies** representam relações entre **atores** (um ator depende de outro)
- **Links** representam relações entre **elementos** dentro de atores (goals, tasks, etc)
- O tipo de dependency indica **o que** o ator depende (um Goal? uma Task? etc)
- O tipo de link indica **como** os elementos se relacionam (refinamento, contribuição, etc)




