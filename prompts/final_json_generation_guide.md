# Guia de Uso - Prompt de Geração Final de JSON

## Visão Geral

Este prompt é usado na **ETAPA 9** da interface conversacional para gerar o modelo iStar 2.0 final em formato JSON após todo o processo de elicitação.

## Quando Usar

Use este prompt quando:
- ✅ Todas as etapas de elicitação foram completadas (Etapas 1-8)
- ✅ Todas as informações foram coletadas e validadas
- ✅ O usuário confirmou que está pronto para gerar o modelo
- ✅ Não há mais perguntas ou ajustes pendentes

## Como Preencher os Placeholders

### 1. Cenário Original
```
[CENÁRIO ORIGINAL]
```
**Substituir por:** O texto completo do cenário de requisitos fornecido pelo usuário na Etapa 1.

**Exemplo:**
```
A mobile application that allows users to request taxi rides through their 
smartphones. Users can see available drivers nearby on a map and request a 
ride by selecting their pickup and destination locations...
```

### 2. Lista de Atores
```
[LISTA DE ATORES]
```
**Substituir por:** Lista estruturada de todos os atores identificados, com seus tipos.

**Exemplo:**
```
- Passenger (istar.Agent): Usuário que solicita corridas
- Driver (istar.Agent): Motorista que fornece o serviço
- Payment System (istar.Agent): Sistema que processa pagamentos
- App System (istar.Agent): Sistema do aplicativo
```

### 3. Lista de Goals por Ator
```
[LISTA DE GOALS POR ATOR]
```
**Substituir por:** Goals organizados por ator.

**Exemplo:**
```
Passenger:
- Request a ride quickly and conveniently
- Track driver location in real-time
- Pay securely

Driver:
- Receive ride requests
- Receive payment for service
```

### 4. Lista de Tasks por Ator
```
[LISTA DE TASKS POR ATOR]
```
**Substituir por:** Tasks organizadas por ator.

**Exemplo:**
```
Passenger:
- Select pickup location
- Select destination
- Confirm ride request

Driver:
- Accept or decline ride request
- Navigate to passenger
- Start ride
- Navigate to destination
- End ride
```

### 5. Lista de Qualities por Ator
```
[LISTA DE QUALITIES POR ATOR]
```
**Substituir por:** Qualities organizadas por ator.

**Exemplo:**
```
Passenger:
- Security

App System:
- Reliability
- Fast response time
```

### 6. Lista de Resources por Ator
```
[LISTA DE RESOURCES POR ATOR]
```
**Substituir por:** Resources organizados por ator (se houver).

**Exemplo:**
```
Driver:
- Ride request
```

### 7. Lista de Dependencies
```
[LISTA DE DEPENDENCIES]
```
**Substituir por:** Todas as dependências identificadas.

**Exemplo:**
```
- Passenger depends on Driver for: Transportation to destination (Goal)
- Driver depends on Passenger for: Payment for service (Goal)
- Driver depends on Passenger for: Ride request (Resource)
- Passenger depends on Payment System for: Process payment securely (Task)
- Driver depends on Payment System for: Process payment securely (Task)
- Passenger depends on Payment System for: Payment data security (Quality)
```

### 8. Lista de Links
```
[LISTA DE LINKS]
```
**Substituir por:** Todos os links identificados (se houver).

**Exemplo:**
```
- goal-request-ride --AndRefinementLink--> task-select-origin
- goal-request-ride --AndRefinementLink--> task-select-destination
- goal-request-ride --AndRefinementLink--> task-confirm-request
```

### 9. Extensões Adicionais
```
[EXTENSÕES ADICIONAIS DO USUÁRIO - se houver]
[ELEMENTOS ADICIONAIS SOLICITADOS PELO USUÁRIO]
```
**Substituir por:** Qualquer elemento adicional solicitado pelo usuário na Etapa 8 ou 9.

**Exemplo:**
```
Usuário solicitou adicionar:
- Ator: Admin (para gerenciar o sistema)
- Goal do Admin: Monitor system performance
- Task do Admin: View system statistics
```

## Processo de Geração

### Passo 1: Coletar Todas as Informações
Antes de usar o prompt, certifique-se de ter:
- ✅ Cenário original completo
- ✅ Lista de todos os atores com tipos
- ✅ Goals organizados por ator
- ✅ Tasks organizadas por ator
- ✅ Qualities organizadas por ator
- ✅ Resources organizados por ator (se houver)
- ✅ Dependencies com source, target e tipo
- ✅ Links com source, target e tipo (se houver)
- ✅ Extensões adicionais (se houver)

### Passo 2: Preencher o Prompt
Substitua todos os placeholders `[PLACEHOLDER]` pelas informações coletadas.

### Passo 3: Enviar para o LLM
Envie o prompt completo para o LLM (GPT-4, Claude, etc.).

### Passo 4: Validar a Resposta
O LLM deve retornar APENAS o JSON. Valide:
- ✅ JSON é sintaticamente válido
- ✅ Todos os campos obrigatórios estão presentes
- ✅ tool = "pistar.2.0.0"
- ✅ istar = "2.0"
- ✅ Todos os IDs são únicos
- ✅ Todas as referências (source/target) são válidas

### Passo 5: Salvar o Modelo
Salve o JSON gerado em `/models/interactive/scenario_{id}_interactive_{timestamp}.json`

## Exemplo Completo de Prompt Preenchido

```
Você é um gerador especializado de modelos iStar 2.0 em formato JSON Pistar 2.0.0.

INFORMAÇÕES COLETADAS:
- Cenário original: A mobile application that allows users to request taxi rides...
- Atores identificados: Passenger (Agent), Driver (Agent), Payment System (Agent)
- Goals identificados: 
  Passenger: Request a ride, Track driver, Pay securely
  Driver: Receive requests, Receive payment
- Tasks identificadas:
  Passenger: Select pickup, Select destination, Confirm request
  Driver: Accept/decline, Navigate to passenger, Start ride, End ride
- Qualities identificadas:
  Passenger: Security
  App System: Reliability, Fast response time
- Dependencies identificadas:
  Passenger depends on Driver for: Transportation (Goal)
  Driver depends on Passenger for: Payment (Goal)
- Links identificados:
  goal-request-ride --AndRefinementLink--> task-select-origin

[Resto do prompt...]
```

## Tratamento de Erros

### Se o LLM retornar texto além do JSON:
- Extraia apenas a parte JSON
- Remova markdown code blocks se houver
- Valide a sintaxe JSON

### Se o JSON estiver inválido:
- Verifique sintaxe (vírgulas, chaves, aspas)
- Verifique se todos os campos obrigatórios estão presentes
- Verifique se tool e istar estão corretos
- Reenvie o prompt com instruções mais claras

### Se IDs estiverem duplicados:
- O prompt já instrui o LLM a gerar IDs únicos
- Se ainda houver duplicatas, corrija manualmente ou reenvie

## Validação Automática

Após receber o JSON, execute validação usando:
- Script: `/experiments/utils/validate_model.py`
- Schema: `/experiments/utils/istar_schema.json`

## Notas Importantes

1. **IDs Únicos**: O prompt instrui o LLM a gerar IDs únicos, mas sempre valide
2. **Estrutura Completa**: Certifique-se de que todos os elementos coletados estão no JSON
3. **Referências Válidas**: Valide que todos os source/target referem a IDs existentes
4. **Sem Texto Adicional**: O LLM deve retornar APENAS JSON, sem explicações

---

**Este prompt é usado na última etapa da interface conversacional para gerar o modelo final.**

