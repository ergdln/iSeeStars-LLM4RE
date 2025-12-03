# Estrutura JSON iStar 2.0 (Pistar 2.0.0)

## ⚠️ ESTRUTURA OFICIAL - NÃO MODIFICAR

Este documento define a estrutura JSON **EXATA** que deve ser usada para todos os modelos iStar 2.0 gerados, validados, convertidos ou revisados neste projeto.

**IMPORTANTE**: Esta estrutura deve ser usada SEMPRE, sem adicionar ou remover campos.

---

## 📐 Estrutura Raiz

```json
{
  "actors": [],
  "orphans": [],
  "dependencies": [],
  "links": [],
  "display": {},
  "tool": "pistar.2.0.0",
  "istar": "2.0",
  "saveDate": "",
  "diagram": {
    "width": 1700,
    "height": 1300,
    "name": "",
    "customProperties": {}
  }
}
```

---

## 🎭 Atores (actors)

Cada ator no array `actors` deve seguir esta estrutura:

```json
{
  "id": "uuid",
  "text": "Nome",
  "type": "istar.Actor | istar.Agent | istar.Role",
  "x": 0,
  "y": 0,
  "customProperties": {
    "Description": ""
  },
  "nodes": []
}
```

### Tipos de Atores
- `istar.Actor` - Ator genérico
- `istar.Agent` - Agente (pessoa física ou sistema)
- `istar.Role` - Papel desempenhado

### Nodes Internos
O array `nodes` contém elementos internos ao ator (goals, tasks, qualities, resources).

---

## 📦 Nodes Internos

Nodes são elementos dentro de um ator (dentro do array `nodes` de cada ator):

```json
{
  "id": "uuid",
  "text": "Nome",
  "type": "istar.Goal | istar.Task | istar.Quality | istar.Resource",
  "x": 0,
  "y": 0,
  "customProperties": {
    "Description": ""
  }
}
```

### Tipos de Nodes
- `istar.Goal` - Meta/Objetivo
- `istar.Task` - Tarefa
- `istar.Quality` - Softgoal/Critério de qualidade
- `istar.Resource` - Recurso

---

## 🔗 Dependências (dependencies)

Dependências entre atores:

```json
{
  "id": "uuid",
  "text": "Nome",
  "type": "istar.Goal | istar.Task | istar.Quality | istar.Resource",
  "x": 0,
  "y": 0,
  "customProperties": {
    "Description": ""
  },
  "source": "id-ator-depender",
  "target": "id-ator-dependee"
}
```

### Campos
- `source`: ID do ator que depende (depender)
- `target`: ID do ator do qual depende (dependee)
- `type`: Tipo do elemento dependido (Goal, Task, Quality, Resource)

---

## 🔌 Links

Links conectam elementos dentro do modelo:

```json
{
  "id": "uuid",
  "type": "istar.OrRefinementLink | istar.AndRefinementLink | istar.DependencyLink | istar.IsALink | istar.ParticipatesInLink | istar.ContributionLink | istar.QualificationLink | istar.NeededByLink",
  "source": "id-origem",
  "target": "id-destino",
  "label": "opcional"
}
```

### Tipos de Links
- `istar.OrRefinementLink` - Refinamento OR
- `istar.AndRefinementLink` - Refinamento AND
- `istar.DependencyLink` - Link de dependência
- `istar.IsALink` - Relação "é um"
- `istar.ParticipatesInLink` - Relação "participa em"
- `istar.ContributionLink` - Contribuição (para softgoals)
- `istar.QualificationLink` - Qualificação
- `istar.NeededByLink` - Necessário por

### Campos
- `source`: ID do elemento de origem
- `target`: ID do elemento de destino
- `label`: Texto opcional para o link

---

## 📋 Regras de Uso OBRIGATÓRIAS

### 1. Estrutura Fixa
- **NUNCA** invente novos campos ou estruturas
- **NUNCA** remova campos obrigatórios
- **SEMPRE** use exatamente esta estrutura

### 2. IDs
- IDs devem ser strings únicas (recomendado: UUID)
- Todos os IDs devem ser únicos no modelo completo
- `source` e `target` SEMPRE referem a IDs existentes

### 3. Organização
- Todos os atores devem estar dentro do array `actors`
- Nodes sempre dentro do array `nodes` de cada ator
- Dependências sempre no array `dependencies` (nível raiz)
- Links sempre no array `links` (nível raiz)

### 4. Campos Especiais
- `orphans`: Array vazio `[]` a menos que seja necessário
- `saveDate`: Deixar vazio `""` ou usar formato ISO (ex: "2024-12-01T10:00:00Z")
- `tool`: Sempre `"pistar.2.0.0"`
- `istar`: Sempre `"2.0"`
- `customProperties`: OBRIGATÓRIO em todos os atores, nodes e dependencies
  - Formato: `{"Description": ""}`
  - Pode estar vazio, mas o campo deve existir

### 5. Formato de Saída
- **SEMPRE** JSON válido
- **NUNCA** incluir comentários no JSON
- **SEMPRE** usar aspas duplas
- **SEMPRE** validar sintaxe antes de salvar

### 6. Coordenadas
- `x` e `y` são números (inteiros ou floats)
- Usar `0` como padrão se não houver posicionamento específico

---

## ✅ Exemplo Completo

```json
{
  "actors": [
    {
      "id": "85ce16fc-c33a-497e-800d-1cc8224ff716",
      "text": "Passenger",
      "type": "istar.Agent",
      "x": 100,
      "y": 100,
      "customProperties": {
        "Description": ""
      },
      "nodes": [
        {
          "id": "9dcc8e7e-502b-40c7-8305-d2b870813cd1",
          "text": "Request a ride",
          "type": "istar.Goal",
          "x": 0,
          "y": 0,
          "customProperties": {
            "Description": ""
          }
        },
        {
          "id": "84bb7ded-4d47-4847-92c2-9f7092b4e908",
          "text": "Select destination",
          "type": "istar.Task",
          "x": 0,
          "y": 50,
          "customProperties": {
            "Description": ""
          }
        }
      ]
    },
    {
      "id": "80e5bfdf-a31e-4c2e-8cac-184c1340dd99",
      "text": "Driver",
      "type": "istar.Agent",
      "x": 500,
      "y": 100,
      "customProperties": {
        "Description": ""
      },
      "nodes": [
        {
          "id": "56c7dbe4-cb52-4b91-8496-256dc4e8dfd4",
          "text": "Accept ride request",
          "type": "istar.Goal",
          "x": 0,
          "y": 0,
          "customProperties": {
            "Description": ""
          }
        }
      ]
    }
  ],
  "orphans": [],
  "dependencies": [
    {
      "id": "42231f6b-6c76-4982-a927-e62c53133744",
      "text": "Ride service",
      "type": "istar.Goal",
      "x": 300,
      "y": 100,
      "customProperties": {
        "Description": ""
      },
      "source": "85ce16fc-c33a-497e-800d-1cc8224ff716",
      "target": "80e5bfdf-a31e-4c2e-8cac-184c1340dd99"
    }
  ],
  "links": [
    {
      "id": "link-001",
      "type": "istar.AndRefinementLink",
      "source": "goal-001",
      "target": "task-001",
      "label": ""
    }
  ],
  "display": {},
  "tool": "pistar.2.0.0",
  "istar": "2.0",
  "saveDate": "",
  "diagram": {
    "width": 1700,
    "height": 1300,
    "name": "",
    "customProperties": {}
  }
}
```

---

## 🔍 Validação

Ao validar um modelo, verificar:

1. ✅ Estrutura raiz contém todos os campos obrigatórios
2. ✅ `tool` é exatamente `"pistar.2.0.0"`
3. ✅ `istar` é exatamente `"2.0"`
4. ✅ Todos os IDs são únicos
5. ✅ Todos os `source` e `target` referem a IDs existentes
6. ✅ Tipos de atores são válidos (`istar.Actor`, `istar.Agent`, `istar.Role`)
7. ✅ Tipos de nodes são válidos (`istar.Goal`, `istar.Task`, `istar.Quality`, `istar.Resource`)
8. ✅ Tipos de links são válidos
9. ✅ JSON é sintaticamente válido
10. ✅ Não há campos extras ou faltantes

---

## 📝 Notas de Implementação

- Esta estrutura é específica para **Pistar 2.0.0**
- Todos os modelos gerados devem seguir esta estrutura
- Scripts de validação devem verificar conformidade com esta estrutura
- Prompts devem instruir LLMs a usar exatamente esta estrutura
- Conversões de outros formatos devem mapear para esta estrutura

---

**Última atualização**: 2024-12-01  
**Versão da estrutura**: Pistar 2.0.0  
**Status**: OFICIAL - NÃO MODIFICAR

