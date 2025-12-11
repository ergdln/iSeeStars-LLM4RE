# Resumo do Fluxo Conversacional - Interface Textual

## Estrutura Geral

```
ETAPA 1: Receber Cenário
    ↓
ETAPA 2: Fazer Perguntas de Elicitação (5-10 perguntas)
    ↓
ETAPA 3: Validar e Refinar ("isso faz sentido?")
    ↓
ETAPA 4: Confirmar Estrutura Final dos Atores
    ↓
ETAPA 5: Confirmar Tarefas
    ↓
ETAPA 6: Confirmar Goals
    ↓
ETAPA 7: Confirmar Qualidades
    ↓
ETAPA 8: Segunda Rodada de Verificação ("faltou algo?")
    ↓
ETAPA 9: Gerar JSON iStar Estruturado
    ↓
ETAPA 10: Perguntar se Deseja Visualizar em Estilo PiStar
```

## Template de Mensagens por Etapa

### ETAPA 1: Receber Cenário

**IA:** Boas-vindas + Solicitação do cenário
**Usuário:** [Cenário de requisitos]
**IA:** Confirmação do entendimento
**Usuário:** "sim" / correções

### ETAPA 2: Fazer Perguntas de Elicitação

**IA:** Introdução + Q1
**Usuário:** [Resposta Q1]
**IA:** Q2
**Usuário:** [Resposta Q2]
**IA:** Q3
**Usuário:** [Resposta Q3]
... (até Q5-Q10)
**IA:** Confirmação de recebimento

### ETAPA 3: Validar e Refinar

**IA:** Resumo do entendido + "Isso faz sentido?"
**Usuário:** "sim" / correções
**IA:** [Se correções] Aplicar ajustes + "Agora está correto?"
**Usuário:** "sim" / mais correções

### ETAPA 4: Confirmar Atores

**IA:** Lista de atores identificados + "Estes atores estão corretos?"
**Usuário:** "sim" / lista corrigida

### ETAPA 5: Confirmar Tarefas

**IA:** Lista de tarefas por ator + "Estas tarefas estão corretas?"
**Usuário:** "sim" / lista corrigida

### ETAPA 6: Confirmar Goals

**IA:** Lista de goals por ator + "Estes goals estão corretos?"
**Usuário:** "sim" / lista corrigida

### ETAPA 7: Confirmar Qualidades

**IA:** Lista de qualidades por ator + "Estas qualidades estão corretas?"
**Usuário:** "sim" / lista corrigida

### ETAPA 8: Segunda Rodada de Verificação

**IA:** Resumo completo + 5 perguntas de verificação
**Usuário:** "está completo" / itens faltantes
**IA:** [Se faltantes] Adicionar + "Agora está completo?"
**Usuário:** "sim" / mais itens

### ETAPA 9: Gerar JSON

**IA:** "Gerando modelo..." + JSON completo
**Usuário:** "está bom" / pedido de ajuste
**IA:** [Se ajuste] Aplicar + "Está correto agora?"
**Usuário:** "sim" / mais ajustes

### ETAPA 10: Visualização PiStar

**IA:** "Deseja visualizar em estilo PiStar?"
**Usuário:** "sim" / "não"
**IA:** [Se sim] Visualização textual / [Se não] Mensagem final

## Elementos Visuais

### Separadores
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Emojis por Etapa
- 🔭 Etapa 1 (Receber cenário)
- 📋 Etapa 2 (Perguntas)
- ✅ Etapa 3 (Validação)
- 🎭 Etapa 4 (Atores)
- 📋 Etapa 5 (Tarefas)
- 🎯 Etapa 6 (Goals)
- ⭐ Etapa 7 (Qualidades)
- 🔍 Etapa 8 (Verificação)
- 🎯 Etapa 9 (Geração)
- 📊 Etapa 10 (Visualização)

## Padrões de Resposta do Usuário

### Confirmações
- "sim"
- "correto"
- "está correto"
- "está completo"
- "não falta nada"
- "está bom"

### Correções
- Lista de itens corrigidos
- Descrição do que precisa mudar
- "Não, deveria ser..."

### Continuidade
- "sim, continue"
- "próximo"
- "avançar"

## Tratamento de Erros

### Respostas Ambíguas
**IA:** "Não entendi completamente. Você poderia reformular?"

### Respostas Incompletas
**IA:** "Parece que a resposta está incompleta. Poderia detalhar mais?"

### Contradições
**IA:** "Notei uma possível contradição: [X] e [Y]. Poderia esclarecer?"

## Fluxos Alternativos

### Usuário Quer Voltar
**Usuário:** "voltar" / "anterior"
**IA:** "Para qual etapa você gostaria de voltar?"

### Usuário Quer Cancelar
**Usuário:** "cancelar" / "sair"
**IA:** "Tem certeza? Todo o progresso será perdido. (sim/não)"

### Usuário Quer Salvar
**Usuário:** "salvar"
**IA:** "Salvando progresso... [confirmação]"

## Variáveis Dinâmicas

As mensagens devem incluir:
- `[Nome do Ator]` - Nomes dos atores identificados
- `[Goal X]` - Goals identificados
- `[Task X]` - Tasks identificadas
- `[Quality X]` - Qualities identificadas
- `[Número]` - Contadores dinâmicos
- `[Descrição]` - Descrições dos elementos

## Implementação

Cada etapa deve:
1. Exibir mensagem da IA
2. Aguardar resposta do usuário
3. Processar resposta
4. Validar resposta
5. Avançar para próxima etapa ou fazer follow-up

## Exemplo de Implementação Python (Pseudo-código)

```python
def etapa_1_receber_cenario():
    print(mensagem_boas_vindas)
    cenario = input("> ")
    print(mensagem_confirmacao.format(cenario))
    confirmacao = input("> ")
    if confirmacao.lower() in ["sim", "correto", "s"]:
        return etapa_2_perguntas_elicitação(cenario)
    else:
        return etapa_1_receber_cenario()  # Loop até confirmação

def etapa_2_perguntas_elicitação(cenario):
    perguntas = gerar_perguntas(cenario)
    respostas = {}
    for i, pergunta in enumerate(perguntas, 1):
        print(f"Q{i}: {pergunta}")
        resposta = input("> ")
        respostas[f"Q{i}"] = resposta
    return etapa_3_validar_refinar(cenario, respostas)
```

---

**Documento de referência rápida para implementação da interface conversacional**




