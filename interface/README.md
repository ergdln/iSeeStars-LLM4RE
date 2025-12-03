# 🖥️ Diretório: Interface

## Propósito

Este diretório contém a implementação da interface guiada que suporta o processo interativo de elicitação de requisitos, permitindo que usuários respondam às perguntas de clarificação do LLM e visualizem os modelos gerados.

## Estrutura Sugerida

```
interface/
├── web/
│   ├── app.py (Streamlit/Gradio)
│   ├── components/
│   │   ├── question_display.py
│   │   ├── answer_input.py
│   │   └── model_visualizer.py
│   └── static/
│       └── styles.css
├── cli/
│   └── interactive_cli.py
├── api/
│   ├── routes.py
│   └── models.py
└── utils/
    ├── istar_renderer.py
    └── json_formatter.py
```

## Uso no Ciclo de Vida do Projeto

### Fase 1: Design
- Prototipar fluxo de interação
- Definir componentes da interface
- Criar mockups e wireframes

### Fase 2: Desenvolvimento
- Implementar interface básica
- Integrar com scripts de experimentação
- Adicionar visualização de modelos

### Fase 3: Teste
- Validar com usuários reais
- Coletar feedback sobre usabilidade
- Refinar baseado em testes

### Fase 4: Execução
- Usar interface nos experimentos interativos
- Registrar interações para análise
- Suportar múltiplos usuários/avaliadores

## Funcionalidades Principais

### 1. Apresentação de Cenário
- Exibir requisitos em linguagem natural
- Formatação legível
- Opção de download/upload

### 2. Processo Interativo
- **Fase de Perguntas**:
  - Exibir perguntas geradas pelo LLM
  - Campos de input para respostas
  - Validação de respostas obrigatórias
  - Opção de pular perguntas (se aplicável)

- **Fase de Geração**:
  - Indicador de progresso
  - Feedback visual durante processamento
  - Exibição de modelo gerado

### 3. Visualização de Modelos
- Renderização de modelo iStar 2.0
- Formato JSON formatado
- Opção de visualização gráfica (se implementada)
- Exportação para diferentes formatos

### 4. Gerenciamento
- Salvar/carregar sessões
- Histórico de interações
- Comparação de modelos (baseline vs. interativo)

## Opções de Implementação

### Opção 1: Interface Web (Streamlit/Gradio)
- **Vantagens**: Rápida de desenvolver, fácil de usar
- **Melhor para**: Prototipagem e testes iniciais

### Opção 2: Interface Web (Flask/FastAPI + React)
- **Vantagens**: Mais controle, melhor UX
- **Melhor para**: Versão final mais polida

### Opção 3: Interface CLI
- **Vantagens**: Simples, sem dependências web
- **Melhor para**: Automação e scripts

## Componentes Técnicos

### Question Display
- Renderização de perguntas numeradas
- Categorização visual (atores, metas, etc.)
- Formatação markdown

### Answer Input
- Campos de texto (curto/longo)
- Validação de input
- Auto-save de respostas

### Model Visualizer
- JSON formatter com syntax highlighting
- Renderização gráfica (opcional, usando bibliotecas como graphviz)
- Exportação (JSON, PDF, PNG)

### Session Management
- Salvar estado da sessão
- Carregar sessões anteriores
- Histórico de mudanças

## Fluxo de Interação

```
1. Usuário carrega/envia cenário
   ↓
2. Sistema envia para LLM (fase de perguntas)
   ↓
3. LLM retorna perguntas
   ↓
4. Interface exibe perguntas
   ↓
5. Usuário responde
   ↓
6. Sistema envia cenário + perguntas + respostas para LLM
   ↓
7. LLM gera modelo
   ↓
8. Interface exibe modelo
   ↓
9. Usuário pode exportar/salvar
```

## Considerações de UX

- **Feedback Visual**: Indicadores de progresso claros
- **Validação**: Feedback imediato sobre inputs
- **Ajuda Contextual**: Tooltips e explicações
- **Acessibilidade**: Suporte a leitores de tela (se web)
- **Responsividade**: Funciona em diferentes tamanhos de tela

## Dependências Sugeridas

- **Streamlit** ou **Gradio**: Interface web rápida
- **Flask/FastAPI**: Backend API (se necessário)
- **React/Vue**: Frontend (se necessário)
- **pygments**: Syntax highlighting para JSON
- **graphviz**: Visualização de modelos (opcional)

## Notas

- Interface deve ser intuitiva para não-especialistas
- Suportar tanto uso interativo quanto batch
- Registrar todas as interações para análise
- Considerar internacionalização (português/inglês)

