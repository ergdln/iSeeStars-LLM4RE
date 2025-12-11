# Fluxo da Interface Interativa - I See Stars

## 1. Visão Geral

Este documento descreve o fluxo completo da interface interativa para o processo de elicitação de requisitos guiada, onde o usuário interage com o sistema para responder perguntas de clarificação antes da geração do modelo iStar 2.0 final.

## 2. Arquitetura do Fluxo

### 2.1 Componentes Principais

1. **Interface de Entrada**: Coleta do cenário de requisitos
2. **Gerador de Perguntas**: LLM gera perguntas de clarificação
3. **Interface de Perguntas**: Apresenta perguntas ao usuário
4. **Coletor de Respostas**: Coleta respostas do usuário
5. **Gerador de Modelo**: LLM gera modelo final usando cenário + respostas
6. **Visualizador de Modelo**: Exibe modelo gerado
7. **Exportador**: Permite exportar modelo em diferentes formatos

### 2.2 Estados do Sistema

- **INICIAL**: Aguardando input do cenário
- **GERANDO_PERGUNTAS**: Processando geração de perguntas
- **APRESENTANDO_PERGUNTAS**: Exibindo perguntas ao usuário
- **COLETANDO_RESPOSTAS**: Coletando respostas do usuário
- **GERANDO_MODELO**: Processando geração do modelo
- **EXIBINDO_MODELO**: Modelo gerado e exibido
- **EXPORTANDO**: Exportando modelo

## 3. Fluxo Detalhado

### 3.1 Etapa 1: Entrada do Cenário

#### 3.1.1 Interface

```
┌─────────────────────────────────────────┐
│  I See Stars - Elicitação Interativa    │
├─────────────────────────────────────────┤
│                                         │
│  Insira o cenário de requisitos:        │
│  ┌───────────────────────────────────┐ │
│  │                                   │ │
│  │  [Área de texto para cenário]    │ │
│  │                                   │ │
│  │                                   │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Carregar arquivo] [Limpar] [Avançar] │
│                                         │
└─────────────────────────────────────────┘
```

#### 3.1.2 Validação

- [ ] Verificar que texto não está vazio
- [ ] Verificar tamanho mínimo (ex: 50 palavras)
- [ ] Verificar tamanho máximo (ex: 2000 palavras)
- [ ] Permitir carregar de arquivo (.txt, .md)

#### 3.1.3 Ações

- **Carregar Arquivo**: Upload de arquivo de texto
- **Limpar**: Limpar campo de texto
- **Avançar**: Validar e prosseguir para próxima etapa

### 3.2 Etapa 2: Geração de Perguntas

#### 3.2.1 Interface

```
┌─────────────────────────────────────────┐
│  Gerando perguntas de clarificação...  │
├─────────────────────────────────────────┤
│                                         │
│         [Indicador de progresso]       │
│                                         │
│  Analisando cenário...                 │
│  Identificando ambiguidades...         │
│  Gerando perguntas...                  │
│                                         │
│  [Cancelar]                            │
│                                         │
└─────────────────────────────────────────┘
```

#### 3.2.2 Processo

1. **Enviar para LLM**
   - Carregar prompt de geração de perguntas
   - Inserir cenário
   - Enviar para API do LLM

2. **Processar Resposta**
   - Extrair lista de perguntas
   - Validar formato (5-8 perguntas)
   - Categorizar perguntas

3. **Armazenar**
   - Salvar perguntas geradas
   - Registrar timestamp
   - Preparar para apresentação

#### 3.2.3 Tratamento de Erros

- **Timeout**: Exibir mensagem e permitir retry
- **Erro de API**: Exibir mensagem de erro
- **Perguntas Insuficientes**: Alertar e permitir regenerar
- **Cancelamento**: Retornar à etapa anterior

### 3.3 Etapa 3: Apresentação de Perguntas

#### 3.3.1 Interface

```
┌─────────────────────────────────────────┐
│  Perguntas de Clarificação              │
├─────────────────────────────────────────┤
│                                         │
│  Cenário: [Nome do cenário]            │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Q1: [Pergunta 1]                   │ │
│  │ Categoria: Atores                  │ │
│  │ ┌───────────────────────────────┐ │ │
│  │ │ [Campo de resposta]           │ │ │
│  │ └───────────────────────────────┘ │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Q2: [Pergunta 2]                   │ │
│  │ Categoria: Goals                   │ │
│  │ ┌───────────────────────────────┐ │ │
│  │ │ [Campo de resposta]           │ │ │
│  │ └───────────────────────────────┘ │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ... (mais perguntas)                   │
│                                         │
│  [Voltar] [Salvar Rascunho] [Avançar]  │
│                                         │
└─────────────────────────────────────────┘
```

#### 3.3.2 Funcionalidades

- **Exibição de Perguntas**:
  - Numeradas sequencialmente
  - Categoria visível (badge colorido)
  - Área de resposta para cada pergunta
  - Contador de caracteres (opcional)

- **Navegação**:
  - Scroll para ver todas as perguntas
  - Botão "Voltar" para editar cenário
  - Botão "Salvar Rascunho" para salvar progresso
  - Botão "Avançar" para validar e prosseguir

- **Validação**:
  - Verificar que todas as perguntas têm resposta
  - Alertar se alguma resposta está vazia
  - Permitir pular perguntas (com aviso)

#### 3.3.3 Melhorias de UX

- **Auto-save**: Salvar respostas automaticamente
- **Destaque**: Destacar perguntas não respondidas
- **Preview**: Mostrar resumo do cenário (colapsável)
- **Ajuda**: Tooltip explicando cada categoria

### 3.4 Etapa 4: Coleta de Respostas

#### 3.4.1 Validação

Antes de avançar:
- [ ] Verificar que todas as perguntas têm resposta
- [ ] Validar tamanho mínimo de respostas (se aplicável)
- [ ] Permitir revisão antes de finalizar

#### 3.4.2 Confirmação

```
┌─────────────────────────────────────────┐
│  Confirmar Respostas                    │
├─────────────────────────────────────────┤
│                                         │
│  Você respondeu a 8 perguntas.          │
│                                         │
│  Deseja revisar antes de gerar o modelo?│
│                                         │
│  [Revisar] [Confirmar e Gerar Modelo]  │
│                                         │
└─────────────────────────────────────────┘
```

### 3.5 Etapa 5: Geração do Modelo

#### 3.5.1 Interface

```
┌─────────────────────────────────────────┐
│  Gerando modelo iStar 2.0...           │
├─────────────────────────────────────────┤
│                                         │
│         [Indicador de progresso]       │
│                                         │
│  Processando cenário e respostas...     │
│  Identificando atores...                │
│  Identificando goals e tasks...         │
│  Criando dependências...                │
│  Validando estrutura...                 │
│                                         │
│  [Cancelar]                            │
│                                         │
└─────────────────────────────────────────┘
```

#### 3.5.2 Processo

1. **Preparar Prompt**
   - Carregar template de geração de modelo
   - Inserir cenário original
   - Inserir perguntas e respostas
   - Validar prompt completo

2. **Enviar para LLM**
   - Enviar prompt para API
   - Monitorar progresso
   - Aguardar resposta

3. **Processar Resposta**
   - Extrair JSON da resposta
   - Validar sintaxe JSON
   - Validar estrutura básica

4. **Armazenar**
   - Salvar modelo gerado
   - Adicionar metadados
   - Registrar timestamp

### 3.6 Etapa 6: Exibição do Modelo

#### 3.6.1 Interface

```
┌─────────────────────────────────────────┐
│  Modelo iStar 2.0 Gerado               │
├─────────────────────────────────────────┤
│                                         │
│  [Tabs: Visualização | JSON | Validação]│
│                                         │
│  ┌───────────────────────────────────┐ │
│  │                                     │ │
│  │  [Visualização do modelo]          │ │
│  │  (Diagrama ou árvore)              │ │
│  │                                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Status: ✓ Válido                       │
│  Atores: 3 | Goals: 5 | Tasks: 4        │
│                                         │
│  [Editar] [Regenerar] [Exportar]       │
│                                         │
└─────────────────────────────────────────┘
```

#### 3.6.2 Abas

**Aba Visualização**:
- Diagrama visual do modelo (se implementado)
- Árvore de elementos
- Navegação interativa

**Aba JSON**:
- JSON formatado com syntax highlighting
- Navegação por elementos
- Busca e filtros

**Aba Validação**:
- Resultado da validação
- Lista de erros (se houver)
- Sugestões de correção

#### 3.6.3 Ações

- **Editar**: Permitir edição manual do modelo
- **Regenerar**: Gerar novo modelo (voltar à etapa 5)
- **Exportar**: Exportar em diferentes formatos
- **Salvar**: Salvar modelo no sistema

### 3.7 Etapa 7: Exportação

#### 3.7.1 Formatos Disponíveis

- **JSON**: Formato Pistar 2.0.0 (padrão)
- **PDF**: Relatório do modelo
- **PNG/SVG**: Imagem do diagrama (se disponível)
- **TXT**: Texto formatado

#### 3.7.2 Interface

```
┌─────────────────────────────────────────┐
│  Exportar Modelo                        │
├─────────────────────────────────────────┤
│                                         │
│  Selecione o formato:                  │
│  ○ JSON (Pistar 2.0.0)                 │
│  ○ PDF                                  │
│  ○ PNG                                  │
│  ○ SVG                                  │
│  ○ TXT                                  │
│                                         │
│  Nome do arquivo: [modelo_001]          │
│                                         │
│  [Cancelar] [Exportar]                  │
│                                         │
└─────────────────────────────────────────┘
```

## 4. Fluxo de Navegação

### 4.1 Fluxo Principal

```
[Entrada Cenário] 
    ↓
[Geração Perguntas]
    ↓
[Apresentação Perguntas]
    ↓
[Coleta Respostas]
    ↓
[Geração Modelo]
    ↓
[Exibição Modelo]
    ↓
[Exportação]
```

### 4.2 Fluxos Alternativos

**Edição de Cenário**:
- Qualquer etapa → Voltar → Editar cenário → Reiniciar

**Regeneração de Perguntas**:
- Após geração de perguntas → Regenerar → Nova geração

**Edição de Respostas**:
- Durante coleta → Editar resposta → Continuar

**Regeneração de Modelo**:
- Após exibição → Regenerar → Nova geração (mantém respostas)

## 5. Gerenciamento de Estado

### 5.1 Dados Armazenados

- **Cenário Original**: Texto do cenário de requisitos
- **Perguntas Geradas**: Lista de perguntas com categorias
- **Respostas Coletadas**: Perguntas e respostas pareadas
- **Modelo Gerado**: JSON do modelo iStar 2.0
- **Metadados**: Timestamps, versões, configurações

### 5.2 Persistência

- **Auto-save**: Salvar progresso automaticamente
- **Rascunhos**: Permitir salvar e carregar rascunhos
- **Histórico**: Manter histórico de sessões

### 5.3 Sessões

- **Nova Sessão**: Começar do zero
- **Carregar Sessão**: Continuar sessão anterior
- **Salvar Sessão**: Salvar estado atual

## 6. Tratamento de Erros

### 6.1 Erros de API

- **Timeout**: Exibir mensagem, permitir retry
- **Rate Limit**: Exibir mensagem, sugerir aguardar
- **Erro de Autenticação**: Exibir mensagem, verificar chaves
- **Erro Genérico**: Exibir mensagem amigável, logar erro

### 6.2 Erros de Validação

- **JSON Inválido**: Tentar correção, exibir aviso
- **Estrutura Incorreta**: Exibir erros específicos
- **Referências Quebradas**: Listar referências inválidas

### 6.3 Erros de Interface

- **Campos Vazios**: Destacar campos obrigatórios
- **Formato Inválido**: Exibir mensagem de erro específica
- **Navegação**: Prevenir navegação inválida

## 7. Melhorias Futuras

### 7.1 Funcionalidades Avançadas

- **Visualização Gráfica**: Diagrama interativo do modelo
- **Edição Visual**: Editar modelo através de interface gráfica
- **Comparação**: Comparar múltiplos modelos
- **Templates**: Templates de cenários comuns

### 7.2 Colaboração

- **Múltiplos Usuários**: Permitir colaboração em tempo real
- **Comentários**: Adicionar comentários ao modelo
- **Versionamento**: Histórico de versões do modelo

### 7.3 Automação

- **Sugestões**: Sugerir melhorias no modelo
- **Validação em Tempo Real**: Validar enquanto usuário edita
- **Auto-complete**: Completar elementos automaticamente

---

**Documento criado em**: 2024-12-01  
**Versão**: 1.0  
**Status**: Especificação do fluxo da interface




