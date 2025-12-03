# Cenário 001: Sistema de Aplicativo de Táxi

## Descrição

Um aplicativo móvel que permite aos usuários solicitar corridas de táxi através de seus smartphones. Os usuários podem ver motoristas disponíveis próximos em um mapa e solicitar uma corrida selecionando seus locais de origem e destino. Os motoristas recebem solicitações de corrida e podem aceitar ou recusar. O sistema rastreia a corrida em tempo real, mostrando a localização do motorista ao usuário. Quando a corrida é concluída, o sistema processa o pagamento e permite que tanto usuários quanto motoristas se avaliem mutuamente. O aplicativo também fornece estimativas de tempo de chegada e tarifas antes de confirmar a corrida.

## Ambiguidades Intencionais

### Ambiguidade 1: Método de Pagamento
**Oculta**: O cenário não especifica como o pagamento é processado (cartão de crédito, dinheiro, carteira digital ou múltiplas opções). Não está claro se o pagamento é processado automaticamente ou manualmente, e quem é responsável pelo processamento do pagamento.

**Pode ser revelada perguntando**: "Quais métodos de pagamento estão disponíveis? O pagamento é processado automaticamente através do aplicativo ou os usuários podem pagar em dinheiro?"

### Ambiguidade 2: Processo de Seleção de Motorista
**Oculta**: O cenário menciona que motoristas podem "aceitar ou recusar" solicitações, mas não especifica se o sistema atribui automaticamente corridas ao motorista mais próximo, se os usuários podem escolher um motorista, ou se há um mecanismo de licitação/competição entre motoristas.

**Pode ser revelada perguntando**: "Como as corridas são atribuídas aos motoristas? O sistema atribui automaticamente ao motorista mais próximo, ou os usuários podem selecionar um motorista específico?"

### Ambiguidade 3: Critérios e Impacto das Avaliações
**Oculta**: O cenário menciona avaliação mas não especifica quais aspectos são avaliados (pontualidade, qualidade da direção, condição do veículo, comunicação), qual escala é usada (1-5 estrelas, positivo/negativo), ou o que acontece com avaliações baixas (suspensão do motorista, avisos ao usuário, etc.).

**Pode ser revelada perguntando**: "Quais aspectos específicos são avaliados no sistema? O que acontece se um motorista ou usuário receber avaliações consistentemente baixas?"

## Versão Mais Clara (Ainda Ambígua)

Um aplicativo móvel que permite aos usuários solicitar corridas de táxi através de seus smartphones. Os usuários podem ver motoristas disponíveis próximos em um mapa e solicitar uma corrida selecionando seus locais de origem e destino. O sistema combina automaticamente o usuário com o motorista disponível mais próximo. Os motoristas recebem solicitações de corrida e podem aceitar ou recusar dentro de 30 segundos. O sistema rastreia a corrida em tempo real usando GPS, mostrando a localização atual do motorista ao usuário. Quando a corrida é concluída, o sistema processa o pagamento automaticamente usando o cartão de crédito registrado na conta do usuário. Tanto usuários quanto motoristas podem se avaliar mutuamente em uma escala de 5 estrelas com base em pontualidade, qualidade da direção e comunicação. O aplicativo fornece estimativas de tempo de chegada e tarifas antes de confirmar a corrida. Motoristas com avaliação média abaixo de 3,5 estrelas podem ser temporariamente suspensos da plataforma.

**Ambiguidades Restantes**:
- Ainda não especifica se os usuários podem escolher um motorista específico ou se é sempre atribuição automática
- Não esclarece o que acontece com usuários com avaliações baixas
- Política de reembolso de pagamento em caso de problemas não é mencionada

---

**Domínio**: Transporte  
**Complexidade**: Média  
**Contagem de Palavras**: ~150 (original), ~200 (versão mais clara)  
**Criado**: 2024-12-01
