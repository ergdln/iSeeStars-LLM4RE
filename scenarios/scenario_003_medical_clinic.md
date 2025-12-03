# Cenário 003: Sistema de Agendamento de Clínica Médica

## Descrição

Um sistema online para uma clínica médica que permite aos pacientes agendar consultas com médicos. Os pacientes podem visualizar horários disponíveis, selecionar um médico e agendar uma consulta. O sistema envia mensagens de confirmação e lembretes aos pacientes. Os médicos podem visualizar sua agenda, ver informações dos pacientes e atualizar o status das consultas. A equipe da clínica pode gerenciar as agendas dos médicos, adicionar ou remover horários disponíveis e lidar com cancelamentos. Os pacientes também podem visualizar seu histórico de consultas e reagendar consultas se necessário.

## Ambiguidades Intencionais

### Ambiguidade 1: Tipos de Consulta e Duração
**Oculta**: O cenário não especifica quais tipos de consultas estão disponíveis (consulta, retorno, emergência, procedimento), quanto tempo as consultas duram, ou se diferentes tipos de consulta têm durações ou custos diferentes.

**Pode ser revelada perguntando**: "Quais tipos de consultas os pacientes podem agendar? Quanto tempo duram os diferentes tipos de consulta e eles têm custos diferentes?"

### Ambiguidade 2: Políticas de Cancelamento e Reagendamento
**Oculta**: O cenário menciona lidar com cancelamentos e reagendamentos mas não especifica limites de tempo (com quanta antecedência as consultas podem ser canceladas), taxas de cancelamento, quantas vezes um paciente pode reagendar, ou o que acontece com faltas.

**Pode ser revelada perguntando**: "Quais são as políticas de cancelamento e reagendamento? Existem limites de tempo, taxas ou restrições sobre a frequência com que os pacientes podem reagendar?"

### Ambiguidade 3: Seleção de Médico e Disponibilidade
**Oculta**: O cenário menciona selecionar um médico mas não especifica se os pacientes podem escolher qualquer médico, se são atribuídos a um médico de atenção primária, se especialistas requerem encaminhamentos, ou com quanta antecedência as consultas podem ser agendadas.

**Pode ser revelada perguntando**: "Os pacientes podem escolher qualquer médico, ou são atribuídos a um médico de atenção primária? Especialistas requerem encaminhamentos e com quanta antecedência as consultas podem ser agendadas?"

## Versão Mais Clara (Ainda Ambígua)

Um sistema online para uma clínica médica que permite aos pacientes agendar consultas com médicos. Os pacientes podem visualizar horários disponíveis, selecionar um médico de sua equipe de atenção primária atribuída ou solicitar um especialista (com encaminhamento), e agendar consultas com até 3 meses de antecedência. O sistema oferece diferentes tipos de consulta: consultas padrão (30 minutos), retornos (15 minutos) e procedimentos (60 minutos), cada um com custos diferentes. O sistema envia mensagens de confirmação via SMS e e-mail, e lembretes 24 horas antes da consulta. Os médicos podem visualizar sua agenda, ver informações dos pacientes e atualizar o status das consultas. A equipe da clínica pode gerenciar as agendas dos médicos, adicionar ou remover horários disponíveis e lidar com cancelamentos. Os pacientes podem cancelar consultas com até 24 horas de antecedência sem taxas, ou reagendar até 2 vezes por consulta. Os pacientes também podem visualizar seu histórico de consultas. Faltas resultam em uma taxa de R$ 25,00.

**Ambiguidades Restantes**:
- Ainda não especifica o que acontece se um paciente acumular múltiplas faltas
- Não esclarece disponibilidade de consultas de emergência ou políticas de atendimento sem agendamento
- Cobertura de seguro e detalhes de processamento de pagamento não são mencionados

---

**Domínio**: Saúde  
**Complexidade**: Média-Alta  
**Contagem de Palavras**: ~120 (original), ~200 (versão mais clara)  
**Criado**: 2024-12-01
