# Guia de Experimentos - I See Stars

## 1. Visão Geral

Este documento descreve o processo completo de execução dos experimentos do projeto I See Stars, incluindo configurações, procedimentos e boas práticas.

## 2. Estrutura dos Experimentos

### 2.1 Tipos de Experimentos

#### Experimento Baseline (Zero-Shot)
- **Objetivo**: Gerar modelo iStar 2.0 diretamente do cenário
- **Interações**: 1 (geração do modelo)
- **Input**: Cenário de requisitos
- **Output**: Modelo iStar 2.0 em JSON

#### Experimento Interativo
- **Objetivo**: Gerar modelo através de processo de clarificação
- **Interações**: 2 (perguntas + modelo)
- **Input Fase 1**: Cenário de requisitos
- **Output Fase 1**: Lista de 5-8 perguntas
- **Input Fase 2**: Cenário + Perguntas + Respostas
- **Output Fase 2**: Modelo iStar 2.0 em JSON

### 2.2 Cenários de Teste

Cada experimento será executado com 3-5 cenários diferentes:
- Cenário 1: Sistema de aplicativo de táxi (domínio: transporte)
- Cenário 2: Sistema de biblioteca (domínio: educação)
- Cenário 3: Sistema de agendamento médico (domínio: saúde)
- Cenário 4: Plataforma e-commerce (domínio: comércio) [opcional]
- Cenário 5: Rede social (domínio: social) [opcional]

## 3. Configuração do Ambiente

### 3.1 Dependências de Software

```
Python 3.11+
openai>=1.3.0
anthropic>=0.7.0
jsonschema>=4.20.0
pandas>=2.1.0
python-dotenv>=1.0.0
```

### 3.2 Variáveis de Ambiente

Criar arquivo `.env`:
```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

**IMPORTANTE**: Nunca commitar chaves de API no repositório.

### 3.3 Estrutura de Diretórios

Garantir que os seguintes diretórios existam:
- `/experiments/logs/` - Logs de execução
- `/experiments/config/` - Arquivos de configuração
- `/models/baseline/` - Modelos baseline gerados
- `/models/interactive/` - Modelos interativos gerados
- `/models/reference/` - Modelos de referência

## 4. Configurações do LLM

### 4.1 Parâmetros Baseline

```json
{
  "model": "gpt-4",
  "temperature": 0.3,
  "max_tokens": 3000,
  "top_p": 1.0,
  "frequency_penalty": 0.0,
  "presence_penalty": 0.0
}
```

**Justificativa**:
- **Temperature 0.3**: Baixa para consistência e conformidade estrutural
- **Max tokens 3000**: Suficiente para modelos iStar 2.0 completos
- **Top_p 1.0**: Sem restrição de núcleo

### 4.2 Parâmetros Interativo - Fase 1 (Perguntas)

```json
{
  "model": "gpt-4",
  "temperature": 0.5,
  "max_tokens": 1500,
  "top_p": 1.0,
  "frequency_penalty": 0.0,
  "presence_penalty": 0.0
}
```

**Justificativa**:
- **Temperature 0.5**: Mais criativo para gerar perguntas variadas
- **Max tokens 1500**: Suficiente para 5-8 perguntas

### 4.3 Parâmetros Interativo - Fase 2 (Modelo)

```json
{
  "model": "gpt-4",
  "temperature": 0.3,
  "max_tokens": 3000,
  "top_p": 1.0,
  "frequency_penalty": 0.0,
  "presence_penalty": 0.0
}
```

**Justificativa**:
- **Temperature 0.3**: Baixa para consistência (igual ao baseline)
- **Max tokens 3000**: Suficiente para modelos completos

### 4.4 Versionamento de Configurações

- Salvar cada configuração em `/experiments/config/`
- Versionar configurações (v1.0, v1.1, etc.)
- Documentar mudanças entre versões

## 5. Processo de Execução - Baseline

### 5.1 Pré-Execução

1. **Verificar Ambiente**
   - [ ] Dependências instaladas
   - [ ] Variáveis de ambiente configuradas
   - [ ] Diretórios criados
   - [ ] Cenários carregados

2. **Preparar Prompt**
   - [ ] Carregar template baseline (`/prompts/baseline.txt`)
   - [ ] Inserir cenário de requisitos
   - [ ] Validar prompt completo

3. **Configurar LLM**
   - [ ] Carregar configuração de parâmetros
   - [ ] Verificar conexão com API
   - [ ] Testar com prompt simples

### 5.2 Execução

1. **Enviar Prompt**
   - [ ] Registrar timestamp de início
   - [ ] Enviar prompt para API do LLM
   - [ ] Aguardar resposta

2. **Processar Resposta**
   - [ ] Capturar resposta completa
   - [ ] Extrair JSON (pode estar em code blocks)
   - [ ] Validar sintaxe JSON básica
   - [ ] Registrar timestamp de fim

3. **Armazenar Resultado**
   - [ ] Salvar modelo em `/models/baseline/scenario_{id}_baseline_{timestamp}.json`
   - [ ] Adicionar metadados:
     ```json
     {
       "metadata": {
         "generated_at": "2024-12-01T10:00:00Z",
         "approach": "baseline",
         "scenario_id": "scenario_001",
         "llm_model": "gpt-4",
         "temperature": 0.3,
         "max_tokens": 3000,
         "prompt_version": "v1.0",
         "execution_time_seconds": 5.2
       }
     }
     ```

4. **Registrar Log**
   - [ ] Salvar log em `/experiments/logs/baseline_{scenario_id}_{timestamp}.log`
   - [ ] Incluir: prompt, resposta, metadados, erros (se houver)

### 5.3 Pós-Execução

1. **Validação Inicial**
   - [ ] Validar estrutura JSON (ver `ISTAR_2_0_JSON_STRUCTURE.md`)
   - [ ] Verificar campos obrigatórios
   - [ ] Classificar: válido, parcialmente válido, inválido

2. **Documentação**
   - [ ] Atualizar índice de modelos
   - [ ] Registrar observações
   - [ ] Documentar problemas encontrados

## 6. Processo de Execução - Interativo

### 6.1 Fase 1: Geração de Perguntas

#### Pré-Execução
1. **Preparar Prompt de Perguntas**
   - [ ] Carregar template (`/prompts/interactive-elicitation.txt`)
   - [ ] Inserir cenário de requisitos
   - [ ] Validar prompt completo

#### Execução
1. **Enviar Prompt**
   - [ ] Registrar timestamp
   - [ ] Enviar para API do LLM
   - [ ] Aguardar resposta

2. **Processar Resposta**
   - [ ] Capturar lista de perguntas
   - [ ] Extrair perguntas (pode estar numerada ou em lista)
   - [ ] Validar que há 5-8 perguntas
   - [ ] Categorizar perguntas (atores, goals, etc.)

3. **Armazenar**
   - [ ] Salvar perguntas em `/experiments/interactive/questions_{scenario_id}_{timestamp}.json`
   - [ ] Registrar log

#### Pós-Execução
- [ ] Validar qualidade das perguntas (relevância, especificidade)
- [ ] Documentar categorização

### 6.2 Fase 2: Coletar Respostas

#### Processo Manual (Inicial)
1. **Apresentar Perguntas**
   - [ ] Exibir perguntas numeradas
   - [ ] Fornecer contexto do cenário

2. **Coletar Respostas**
   - [ ] Para cada pergunta, coletar resposta
   - [ ] Validar que respostas não estão vazias
   - [ ] Permitir revisão antes de finalizar

3. **Armazenar**
   - [ ] Salvar perguntas e respostas pareadas
   - [ ] Formato:
     ```json
     {
       "scenario_id": "scenario_001",
       "questions": [
         {
           "id": 1,
           "text": "Quem são os principais atores do sistema?",
           "category": "actors",
           "answer": "Os principais atores são..."
         }
       ]
     }
     ```

#### Processo Automatizado (Futuro)
- Interface web para coleta de respostas
- Validação automática de respostas
- Exportação para formato padronizado

### 6.3 Fase 3: Geração do Modelo

#### Pré-Execução
1. **Preparar Prompt Final**
   - [ ] Carregar template (`/prompts/model-generation.txt`)
   - [ ] Inserir cenário original
   - [ ] Inserir perguntas e respostas
   - [ ] Validar prompt completo

#### Execução
1. **Enviar Prompt**
   - [ ] Registrar timestamp
   - [ ] Enviar para API do LLM
   - [ ] Aguardar resposta

2. **Processar Resposta**
   - [ ] Capturar resposta completa
   - [ ] Extrair JSON
   - [ ] Validar sintaxe JSON básica

3. **Armazenar Resultado**
   - [ ] Salvar modelo em `/models/interactive/scenario_{id}_interactive_{timestamp}.json`
   - [ ] Adicionar metadados incluindo perguntas e respostas
   - [ ] Registrar log completo

#### Pós-Execução
- [ ] Validação inicial (igual ao baseline)
- [ ] Comparar com modelo baseline (mesmo cenário)
- [ ] Documentar observações

## 7. Tratamento de Erros

### 7.1 Erros de API

- **Timeout**: Retry com backoff exponencial (máx 3 tentativas)
- **Rate Limit**: Aguardar e retry
- **Erro de Autenticação**: Verificar chaves de API
- **Erro de Modelo**: Registrar e tentar modelo alternativo

### 7.2 Erros de Parsing

- **JSON Inválido**: Tentar extrair de code blocks
- **JSON Malformado**: Tentar correção automática (se possível)
- **Estrutura Incorreta**: Registrar erro e classificar como inválido

### 7.3 Erros de Validação

- **Campos Faltantes**: Registrar quais campos estão faltando
- **IDs Duplicados**: Tentar correção automática
- **Referências Inválidas**: Registrar referências quebradas

## 8. Logs e Rastreabilidade

### 8.1 Informações a Registrar

Para cada execução:
- **Timestamp**: Início e fim
- **Prompt Completo**: Texto exato enviado
- **Resposta Completa**: Texto exato recebido
- **Parâmetros**: Modelo, temperatura, tokens, etc.
- **Metadados**: Cenário, abordagem, versão de prompt
- **Erros**: Qualquer erro ou warning
- **Custos**: Tokens usados, custo estimado (se disponível)

### 8.2 Formato de Logs

```json
{
  "experiment_id": "exp_001",
  "timestamp": "2024-12-01T10:00:00Z",
  "approach": "baseline",
  "scenario_id": "scenario_001",
  "prompt_version": "v1.0",
  "llm_config": {
    "model": "gpt-4",
    "temperature": 0.3,
    "max_tokens": 3000
  },
  "prompt": "...",
  "response": "...",
  "execution_time_seconds": 5.2,
  "tokens_used": {
    "prompt": 500,
    "completion": 1200,
    "total": 1700
  },
  "errors": [],
  "warnings": []
}
```

## 9. Reprodutibilidade

### 9.1 Seeds e Aleatoriedade

- Definir seed fixo para qualquer aleatoriedade
- Documentar seed usado
- Se LLM suporta seed, configurar seed fixo

### 9.2 Versionamento

- Versionar todos os prompts
- Versionar todas as configurações
- Manter histórico de mudanças
- Tags Git para versões importantes

### 9.3 Documentação

- Documentar todas as decisões
- Registrar desvios do plano
- Manter changelog de experimentos

## 10. Monitoramento de Custos

### 10.1 Métricas

- Tokens usados por experimento
- Custo estimado por experimento
- Custo total acumulado

### 10.2 Controle

- Estabelecer limite de custo por experimento
- Alertar se custo exceder orçamento
- Registrar custos em logs

## 11. Checklist de Execução

### Antes de Iniciar
- [ ] Ambiente configurado
- [ ] Dependências instaladas
- [ ] Chaves de API configuradas
- [ ] Diretórios criados
- [ ] Cenários preparados
- [ ] Prompts versionados
- [ ] Configurações salvas

### Durante Execução
- [ ] Logs sendo gerados
- [ ] Modelos sendo salvos
- [ ] Erros sendo registrados
- [ ] Custos sendo monitorados

### Após Execução
- [ ] Todos os modelos validados
- [ ] Logs completos
- [ ] Metadados atualizados
- [ ] Índice de modelos atualizado
- [ ] Observações documentadas

---

**Documento criado em**: 2024-12-01  
**Versão**: 1.0  
**Status**: Guia de execução de experimentos




