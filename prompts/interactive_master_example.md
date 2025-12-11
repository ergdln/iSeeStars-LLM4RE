# Exemplo de Fluxo - Prompt Mestre Interativo

Este documento mostra um exemplo completo de como o prompt mestre interativo funciona na prática.

## Cenário de Exemplo

**Cenário**: "A mobile application that allows users to request taxi rides through their smartphones. Users can see available drivers nearby on a map and request a ride by selecting their pickup and destination locations. Drivers receive ride requests and can accept or decline them. The system tracks the ride in real-time, showing the driver's location to the user. When the ride is completed, the system processes payment and allows both users and drivers to rate each other."

---

## FASE 1: Primeira Rodada de Perguntas

### LLM (Engenheiro de Requisitos):

```
RODADA 1 DE PERGUNTAS

Baseado na análise do cenário, preciso clarificar alguns pontos:

Q1: Quem são os principais atores do sistema? Além de "users" e "drivers", há outros atores importantes (ex: sistema de pagamento, administradores)?

Q2: Quais são os objetivos principais do ator "user" (passageiro)? Quais são suas metas ao usar o aplicativo?

Q3: Quais são os objetivos principais do ator "driver" (motorista)? O que eles buscam alcançar?

Q4: Como funciona o processo de seleção de motorista? O sistema atribui automaticamente ao motorista mais próximo, ou o usuário pode escolher um motorista específico?

Q5: Quais são as tarefas específicas que o usuário deve realizar para solicitar uma corrida? (ex: selecionar origem, destino, confirmar)

Q6: Quais são as tarefas específicas que o motorista realiza? (ex: aceitar/recusar corrida, navegar até o passageiro, iniciar/finalizar corrida)

Q7: Como funciona o processamento de pagamento? Quais métodos de pagamento são aceitos? O pagamento é automático ou manual?

Q8: Existem critérios de qualidade importantes para o sistema? (ex: segurança, confiabilidade, tempo de resposta, usabilidade)

Por favor, responda cada pergunta numerada (A1, A2, A3, etc.).
```

### Usuário:

```
A1: Os principais atores são: usuário (passageiro), motorista, e o sistema do aplicativo. Não há administradores mencionados no escopo.

A2: Os objetivos principais do passageiro são: solicitar uma corrida de forma rápida e conveniente, acompanhar a localização do motorista em tempo real, e realizar o pagamento de forma segura.

A3: Os objetivos principais do motorista são: receber solicitações de corrida, aceitar corridas que sejam convenientes, e receber pagamento pelos serviços prestados.

A4: O sistema atribui automaticamente ao motorista mais próximo disponível. O usuário não escolhe o motorista.

A5: As tarefas do usuário são: abrir o aplicativo, selecionar localização de origem (ou usar GPS), selecionar destino, visualizar estimativa de preço e tempo, e confirmar a solicitação.

A6: As tarefas do motorista são: receber notificação de nova corrida, visualizar detalhes da corrida (origem, destino, distância), aceitar ou recusar a corrida, navegar até o passageiro, iniciar a corrida, navegar até o destino, e finalizar a corrida.

A7: O pagamento é processado automaticamente através de cartão de crédito cadastrado no aplicativo. Não há opção de pagamento em dinheiro.

A8: Os critérios de qualidade importantes são: segurança (dados pessoais e pagamento), confiabilidade (sistema sempre disponível), e tempo de resposta rápido para solicitações.
```

---

## FASE 2: Validação e Segunda Rodada

### LLM (Engenheiro de Requisitos):

```
VALIDAÇÃO DAS RESPOSTAS

Analisando suas respostas...

✓ Informações sobre atores estão claras
✓ Objetivos de passageiro e motorista estão bem definidos
✓ Tarefas estão detalhadas
✓ Processo de pagamento está claro

⚠ Preciso esclarecer alguns pontos sobre dependências e qualidades:

Q9: O passageiro depende do motorista para qual elemento específico? (um goal, task ou resource?)

Q10: O motorista depende do passageiro para qual elemento? (ex: receber pagamento, ter corridas disponíveis?)

Q11: Há alguma dependência do sistema de pagamento? Se sim, qual ator depende dele e para quê?

Q12: Os critérios de qualidade mencionados (segurança, confiabilidade, tempo de resposta) são importantes para qual ator? São softgoals do passageiro, motorista, ou do sistema?

Por favor, responda estas perguntas adicionais.
```

### Usuário:

```
A9: O passageiro depende do motorista para o goal "Receber transporte até o destino".

A10: O motorista depende do passageiro para o goal "Receber pagamento pelo serviço" e para o resource "Solicitação de corrida".

A11: Tanto o passageiro quanto o motorista dependem do sistema de pagamento para o task "Processar pagamento de forma segura". O passageiro também depende do sistema de pagamento para o quality "Segurança dos dados de pagamento".

A12: Segurança é um softgoal importante para o passageiro. Confiabilidade e tempo de resposta são softgoals do sistema (mas também importantes para passageiro e motorista).
```

---

## FASE 3: Geração do Modelo

### LLM (Engenheiro de Requisitos):

```
PRONTO PARA GERAR O MODELO

Tenho informações suficientes. Gerando modelo iStar 2.0...

{
  "actors": [
    {
      "id": "actor-passenger",
      "text": "Passenger",
      "type": "istar.Agent",
      "x": 100,
      "y": 100,
      "nodes": [
        {
          "id": "goal-request-ride",
          "text": "Request a ride quickly and conveniently",
          "type": "istar.Goal",
          "x": 0,
          "y": 0
        },
        {
          "id": "goal-track-driver",
          "text": "Track driver location in real-time",
          "type": "istar.Goal",
          "x": 0,
          "y": 50
        },
        {
          "id": "goal-pay-securely",
          "text": "Pay securely",
          "type": "istar.Goal",
          "x": 0,
          "y": 100
        },
        {
          "id": "quality-security",
          "text": "Security",
          "type": "istar.Quality",
          "x": 0,
          "y": 150
        },
        {
          "id": "task-select-origin",
          "text": "Select pickup location",
          "type": "istar.Task",
          "x": 0,
          "y": 200
        },
        {
          "id": "task-select-destination",
          "text": "Select destination",
          "type": "istar.Task",
          "x": 0,
          "y": 250
        },
        {
          "id": "task-confirm-request",
          "text": "Confirm ride request",
          "type": "istar.Task",
          "x": 0,
          "y": 300
        }
      ]
    },
    {
      "id": "actor-driver",
      "text": "Driver",
      "type": "istar.Agent",
      "x": 500,
      "y": 100,
      "nodes": [
        {
          "id": "goal-receive-requests",
          "text": "Receive ride requests",
          "type": "istar.Goal",
          "x": 0,
          "y": 0
        },
        {
          "id": "goal-receive-payment",
          "text": "Receive payment for service",
          "type": "istar.Goal",
          "x": 0,
          "y": 50
        },
        {
          "id": "task-accept-decline",
          "text": "Accept or decline ride request",
          "type": "istar.Task",
          "x": 0,
          "y": 100
        },
        {
          "id": "task-navigate-to-passenger",
          "text": "Navigate to passenger",
          "type": "istar.Task",
          "x": 0,
          "y": 150
        },
        {
          "id": "task-start-ride",
          "text": "Start ride",
          "type": "istar.Task",
          "x": 0,
          "y": 200
        },
        {
          "id": "task-navigate-to-destination",
          "text": "Navigate to destination",
          "type": "istar.Task",
          "x": 0,
          "y": 250
        },
        {
          "id": "task-end-ride",
          "text": "End ride",
          "type": "istar.Task",
          "x": 0,
          "y": 300
        },
        {
          "id": "resource-ride-request",
          "text": "Ride request",
          "type": "istar.Resource",
          "x": 0,
          "y": 350
        }
      ]
    },
    {
      "id": "actor-payment-system",
      "text": "Payment System",
      "type": "istar.Agent",
      "x": 300,
      "y": 300,
      "nodes": [
        {
          "id": "task-process-payment",
          "text": "Process payment securely",
          "type": "istar.Task",
          "x": 0,
          "y": 0
        },
        {
          "id": "quality-payment-security",
          "text": "Payment data security",
          "type": "istar.Quality",
          "x": 0,
          "y": 50
        }
      ]
    },
    {
      "id": "actor-app-system",
      "text": "App System",
      "type": "istar.Agent",
      "x": 300,
      "y": 100,
      "nodes": [
        {
          "id": "quality-reliability",
          "text": "Reliability",
          "type": "istar.Quality",
          "x": 0,
          "y": 0
        },
        {
          "id": "quality-response-time",
          "text": "Fast response time",
          "type": "istar.Quality",
          "x": 0,
          "y": 50
        }
      ]
    }
  ],
  "orphans": [],
  "dependencies": [
    {
      "id": "dep-passenger-driver-transport",
      "text": "Transportation to destination",
      "type": "istar.Goal",
      "x": 300,
      "y": 100,
      "source": "actor-passenger",
      "target": "actor-driver"
    },
    {
      "id": "dep-driver-passenger-payment",
      "text": "Payment for service",
      "type": "istar.Goal",
      "x": 300,
      "y": 150,
      "source": "actor-driver",
      "target": "actor-passenger"
    },
    {
      "id": "dep-driver-passenger-request",
      "text": "Ride request",
      "type": "istar.Resource",
      "x": 300,
      "y": 200,
      "source": "actor-driver",
      "target": "actor-passenger"
    },
    {
      "id": "dep-passenger-payment-process",
      "text": "Process payment securely",
      "type": "istar.Task",
      "x": 200,
      "y": 200,
      "source": "actor-passenger",
      "target": "actor-payment-system"
    },
    {
      "id": "dep-driver-payment-process",
      "text": "Process payment securely",
      "type": "istar.Task",
      "x": 400,
      "y": 200,
      "source": "actor-driver",
      "target": "actor-payment-system"
    },
    {
      "id": "dep-passenger-payment-security",
      "text": "Payment data security",
      "type": "istar.Quality",
      "x": 200,
      "y": 250,
      "source": "actor-passenger",
      "target": "actor-payment-system"
    }
  ],
  "links": [
    {
      "id": "link-request-refinement",
      "type": "istar.AndRefinementLink",
      "source": "goal-request-ride",
      "target": "task-select-origin",
      "label": ""
    },
    {
      "id": "link-request-refinement-2",
      "type": "istar.AndRefinementLink",
      "source": "goal-request-ride",
      "target": "task-select-destination",
      "label": ""
    },
    {
      "id": "link-request-refinement-3",
      "type": "istar.AndRefinementLink",
      "source": "goal-request-ride",
      "target": "task-confirm-request",
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

## Características do Fluxo

1. **Primeira Rodada**: 8 perguntas cobrindo todos os aspectos principais
2. **Validação**: LLM analisa respostas e identifica o que está completo
3. **Segunda Rodada**: 4 perguntas focadas em dependências e qualidades
4. **Geração Final**: Modelo completo incorporando todas as informações

## Vantagens desta Abordagem

- **Iterativa**: Múltiplas rodadas de perguntas
- **Validativa**: Verifica consistência das respostas
- **Completa**: Cobre todos os aspectos do modelo iStar
- **Adaptativa**: Faz perguntas de follow-up quando necessário
- **Estruturada**: Formato claro de comunicação

---

**Nota**: Este é um exemplo. O número e tipo de perguntas podem variar dependendo do cenário e das respostas do usuário.




