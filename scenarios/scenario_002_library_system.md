# Cenário 002: Sistema de Gerenciamento de Biblioteca

## Descrição

Um sistema digital para gerenciar uma biblioteca pública que permite aos membros pesquisar livros, reservar itens e fazer empréstimos online. A equipe da biblioteca pode adicionar novos livros ao catálogo, atualizar informações dos livros e gerenciar contas de membros. Os membros podem navegar pelo catálogo por título, autor ou assunto, ver o status de disponibilidade e colocar itens em espera que estão atualmente emprestados. O sistema rastreia datas de vencimento e envia lembretes aos membros. Quando os materiais são devolvidos, a equipe pode processar as devoluções e atualizar a disponibilidade. Os membros também podem renovar itens online se ninguém mais tiver colocado em espera.

## Ambiguidades Intencionais

### Ambiguidade 1: Registro de Membros e Níveis de Acesso
**Oculta**: O cenário não especifica quem pode se tornar membro (qualquer pessoa, apenas residentes, restrições de idade), quais informações são necessárias para registro, ou se há diferentes níveis de associação com privilégios diferentes (estudante, adulto, premium).

**Pode ser revelada perguntando**: "Quem pode se tornar membro da biblioteca? Existem diferentes tipos de associações com privilégios ou limites de empréstimo diferentes?"

### Ambiguidade 2: Limites de Reserva e Espera
**Oculta**: O cenário menciona colocar itens em espera mas não especifica quantos itens um membro pode reservar simultaneamente, por quanto tempo as reservas são válidas, ou o que acontece se um membro não retirar um item reservado dentro de um determinado prazo.

**Pode ser revelada perguntando**: "Quantos itens um membro pode reservar ao mesmo tempo? Por quanto tempo as reservas são válidas e o que acontece se um membro não retirar um item reservado?"

### Ambiguidade 3: Processamento de Devolução e Multas
**Oculta**: O cenário menciona processar devoluções mas não especifica se há multas por itens atrasados, como as multas são calculadas, se há períodos de carência, ou como o pagamento de multas é tratado (online, presencial, cobranças automáticas).

**Pode ser revelada perguntando**: "Existem multas por itens atrasados? Como são calculadas e como os membros podem pagá-las?"

## Versão Mais Clara (Ainda Ambígua)

Um sistema digital para gerenciar uma biblioteca pública que permite aos membros pesquisar livros, reservar itens e fazer empréstimos online. Qualquer pessoa pode se registrar como membro fornecendo identificação e informações de contato. A equipe da biblioteca pode adicionar novos livros ao catálogo, atualizar informações dos livros e gerenciar contas de membros. Os membros podem navegar pelo catálogo por título, autor ou assunto, ver o status de disponibilidade e colocar até 5 itens em espera que estão atualmente emprestados. As reservas são válidas por 7 dias após a notificação. O sistema rastreia datas de vencimento e envia lembretes por e-mail aos membros 3 dias antes dos itens vencerem. Quando os materiais são devolvidos, a equipe pode processar as devoluções e atualizar a disponibilidade. Se os itens forem devolvidos com atraso, o sistema calcula automaticamente multas de R$ 0,50 por dia por item, que podem ser pagas online ou presencialmente. Os membros podem renovar itens online até 2 vezes se ninguém mais tiver colocado em espera.

**Ambiguidades Restantes**:
- Ainda não especifica limites de empréstimo (quantos itens podem ser emprestados ao mesmo tempo)
- Não esclarece o que acontece se um membro não pagar multas
- Valor máximo de multa ou políticas de suspensão de conta não são mencionados

---

**Domínio**: Educação  
**Complexidade**: Média  
**Contagem de Palavras**: ~140 (original), ~190 (versão mais clara)  
**Criado**: 2024-12-01
