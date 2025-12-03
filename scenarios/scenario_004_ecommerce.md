# Cenário 004: Plataforma de E-commerce Simples

## Descrição

Uma loja online onde clientes podem navegar por produtos, adicionar itens a um carrinho de compras e comprá-los. Vendedores podem listar produtos com descrições, preços e imagens. Os clientes podem pesquisar produtos por categoria ou palavras-chave, visualizar detalhes dos produtos e ver avaliações de outros clientes. Quando prontos para comprar, os clientes prosseguem para o checkout onde inserem informações de envio e detalhes de pagamento. O sistema processa pedidos e envia e-mails de confirmação. Vendedores recebem notificações quando pedidos são feitos e podem atualizar o status do pedido conforme preparam e enviam os itens. Os clientes podem rastrear seus pedidos e deixar avaliações após receber os produtos.

## Ambiguidades Intencionais

### Ambiguidade 1: Processamento de Pagamento e Segurança
**Oculta**: O cenário menciona inserir detalhes de pagamento mas não especifica quais métodos de pagamento são aceitos (cartões de crédito, PayPal, transferência bancária), como o pagamento é processado (gateway de terceiros, processamento direto), ou quais medidas de segurança estão em vigor para informações de pagamento.

**Pode ser revelada perguntando**: "Quais métodos de pagamento são aceitos? Como as informações de pagamento são protegidas e processadas?"

### Ambiguidade 2: Opções de Envio e Entrega
**Oculta**: O cenário menciona informações de envio mas não especifica métodos de envio disponíveis (padrão, expresso, noturno), custos de envio, prazos de entrega, ou se há opções de frete grátis ou requisitos de compra mínima.

**Pode ser revelada perguntando**: "Quais opções de envio estão disponíveis? Quais são os custos e prazos de entrega para cada opção?"

### Ambiguidade 3: Política de Devolução e Reembolso
**Oculta**: O cenário não menciona devoluções, reembolsos ou trocas. Não está claro se os clientes podem devolver itens, sob quais condições, qual é o prazo, quem paga pelo frete de devolução, ou como os reembolsos são processados.

**Pode ser revelada perguntando**: "Qual é a política de devolução e reembolso? Os clientes podem devolver itens e, se sim, quais são as condições, prazos e processo?"

## Versão Mais Clara (Ainda Ambígua)

Uma loja online onde clientes podem navegar por produtos, adicionar itens a um carrinho de compras e comprá-los. Vendedores podem listar produtos com descrições, preços e imagens. Os clientes podem pesquisar produtos por categoria ou palavras-chave, visualizar detalhes dos produtos e ver avaliações de outros clientes. A plataforma aceita pagamentos com cartão de crédito e PayPal, processados através de um gateway de pagamento seguro de terceiros. Quando prontos para comprar, os clientes prosseguem para o checkout onde inserem informações de envio e detalhes de pagamento. As opções de envio incluem padrão (5-7 dias úteis, R$ 5,99), expresso (2-3 dias úteis, R$ 12,99) e frete grátis para pedidos acima de R$ 50,00. O sistema processa pedidos e envia e-mails de confirmação. Vendedores recebem notificações quando pedidos são feitos e podem atualizar o status do pedido conforme preparam e enviam os itens. Os clientes podem rastrear seus pedidos e deixar avaliações após receber os produtos. Devoluções são aceitas dentro de 30 dias após a entrega para itens não utilizados na embalagem original, com reembolsos processados para o método de pagamento original.

**Ambiguidades Restantes**:
- Ainda não especifica quem paga pelos custos de frete de devolução
- Não esclarece o que acontece com itens defeituosos ou danificados
- Política de troca (trocar por tamanho/cor diferente) não é mencionada

---

**Domínio**: Comércio  
**Complexidade**: Média  
**Contagem de Palavras**: ~140 (original), ~220 (versão mais clara)  
**Criado**: 2024-12-01
