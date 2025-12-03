# Cenário 005: Aplicativo de Descoberta e Reserva de Eventos

## Descrição

Um aplicativo móvel que ajuda os usuários a descobrir eventos locais acontecendo em sua área. Os usuários podem navegar por eventos por categoria, data ou localização, e ver detalhes do evento incluindo descrição, horário, local e preços dos ingressos. Os usuários podem salvar eventos em uma lista de favoritos e compartilhar eventos com amigos. Quando interessados em participar, os usuários podem comprar ingressos diretamente através do aplicativo. Organizadores de eventos podem criar e gerenciar seus eventos, definir preços de ingressos e ver quantos ingressos foram vendidos. O aplicativo envia notificações sobre eventos futuros que os usuários salvaram ou compraram ingressos, e fornece direções para os locais dos eventos.

## Ambiguidades Intencionais

### Ambiguidade 1: Tipos de Ingresso e Preços
**Oculta**: O cenário menciona preços de ingressos mas não especifica se há diferentes tipos de ingresso (entrada geral, VIP, antecipado), se os preços variam por data ou disponibilidade, se há taxas de serviço, ou se organizadores podem oferecer descontos ou códigos promocionais.

**Pode ser revelada perguntando**: "Existem diferentes tipos de ingressos disponíveis para eventos? Organizadores podem definir múltiplos níveis de preço, descontos ou códigos promocionais?"

### Ambiguidade 2: Processo de Criação e Aprovação de Eventos
**Oculta**: O cenário menciona que organizadores podem criar eventos mas não especifica se há um processo de aprovação, se qualquer pessoa pode criar eventos ou se verificação é necessária, quais informações são obrigatórias, ou se há taxas para listar eventos.

**Pode ser revelada perguntando**: "Quem pode criar eventos? Existe um processo de aprovação ou verificação, e há taxas ou requisitos para listar eventos?"

### Ambiguidade 3: Transferência e Cancelamento de Ingressos
**Oculta**: O cenário não menciona o que acontece se os usuários não puderem comparecer aos eventos, se os ingressos podem ser transferidos para outros usuários, se há políticas de reembolso, se eventos podem ser cancelados por organizadores, ou o que acontece com ingressos comprados em caso de cancelamento.

**Pode ser revelada perguntando**: "Os usuários podem transferir ingressos para outros ou obter reembolsos? O que acontece se um evento for cancelado pelo organizador?"

## Versão Mais Clara (Ainda Ambígua)

Um aplicativo móvel que ajuda os usuários a descobrir eventos locais acontecendo em sua área. Os usuários podem navegar por eventos por categoria, data ou localização, e ver detalhes do evento incluindo descrição, horário, local e preços dos ingressos. Qualquer pessoa pode criar um evento após verificação de e-mail, com uma taxa de comissão de 5% sobre as vendas de ingressos. Organizadores podem definir múltiplos tipos de ingresso (entrada geral, VIP, antecipado) com preços diferentes e podem criar códigos promocionais para descontos. Os usuários podem salvar eventos em uma lista de favoritos e compartilhar eventos com amigos. Quando interessados em participar, os usuários podem comprar ingressos diretamente através do aplicativo, com uma taxa de serviço de R$ 2,50 por ingresso. Ingressos podem ser transferidos para outros usuários até 24 horas antes do evento. Organizadores de eventos podem criar e gerenciar seus eventos, definir preços de ingressos e ver quantos ingressos foram vendidos. O aplicativo envia notificações sobre eventos futuros que os usuários salvaram ou compraram ingressos, e fornece direções para os locais dos eventos. Se um evento for cancelado pelo organizador, reembolsos completos são processados automaticamente.

**Ambiguidades Restantes**:
- Ainda não especifica se os usuários podem obter reembolsos por motivos pessoais (não podem comparecer)
- Não esclarece o que acontece se um evento for cancelado pelo local (não pelo organizador)
- Cancelamentos relacionados ao clima e políticas não são mencionados

---

**Domínio**: Social/Entretenimento  
**Complexidade**: Média  
**Contagem de Palavras**: ~150 (original), ~220 (versão mais clara)  
**Criado**: 2024-12-01
