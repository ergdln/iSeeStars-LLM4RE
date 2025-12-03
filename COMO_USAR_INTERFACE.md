# Como Usar a Interface Web Interativa

## 🚀 Iniciando o Servidor

### 1. Instalar Dependências

```bash
pip3 install -r requirements.txt
```

### 2. Configurar API Key

Certifique-se de que a variável de ambiente `OPENAI_API_KEY` está configurada:

```bash
export OPENAI_API_KEY='sua-chave-api'
```

### 3. Iniciar o Servidor

```bash
python3 app.py
```

O servidor iniciará em: **http://localhost:5000**

### 4. Abrir no Navegador

Abra seu navegador e acesse: **http://localhost:5000**

## 📝 Como Usar a Interface

### Etapa 1: Inserir Cenário

1. Na primeira tela, digite ou cole o cenário de requisitos que deseja modelar
2. Você pode clicar em "Carregar Exemplo" para ver um exemplo
3. Clique em "Iniciar Elicitação"

### Etapa 2: Responder Perguntas

1. A IA gerará 5-8 perguntas de clarificação
2. Responda cada pergunta no campo de texto correspondente
3. Todas as perguntas devem ser respondidas antes de continuar
4. Clique em "Gerar Modelo iStar" quando terminar

### Etapa 3: Visualizar e Baixar Modelo

1. O modelo iStar 2.0 será gerado automaticamente
2. Você verá estatísticas do modelo (atores, nodes, dependencies, links)
3. O JSON completo será exibido
4. Você pode:
   - **Copiar** o JSON para a área de transferência
   - **Baixar** o JSON como arquivo
   - **Validar** o JSON
   - **Iniciar Nova Sessão**

## 🔧 Configurações Opcionais

### Modelo do LLM

Por padrão, o sistema usa `gpt-4o-mini`. Para usar outro modelo:

```bash
export OPENAI_MODEL='gpt-4'
```

### Porta do Servidor

Para mudar a porta (padrão: 5000), edite o arquivo `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Mude 5000 para outra porta
```

## ⚠️ Solução de Problemas

### Erro: "OPENAI_API_KEY não configurada"

Certifique-se de exportar a variável de ambiente antes de iniciar o servidor:

```bash
export OPENAI_API_KEY='sua-chave'
python3 app.py
```

### Erro: "Prompt não encontrado"

Certifique-se de que os arquivos de prompt estão no diretório `prompts/`:
- `prompts/interactive_master.txt`
- `prompts/final_json_generation.txt`

### Erro ao gerar perguntas ou modelo

- Verifique sua conexão com a internet
- Verifique se sua API key tem créditos disponíveis
- Verifique os logs do servidor para mais detalhes

## 📋 Estrutura de Arquivos

```
iSeeStars-LLM4RE/
├── app.py                 # Servidor Flask
├── requirements.txt      # Dependências Python
├── templates/
│   └── index.html        # Interface HTML
├── static/
│   ├── style.css         # Estilos CSS
│   └── script.js          # JavaScript frontend
└── prompts/
    ├── interactive_master.txt
    └── final_json_generation.txt
```

## 🎯 Fluxo Completo

1. **Usuário insere cenário** → Interface envia para `/api/start`
2. **IA gera perguntas** → Interface chama `/api/generate-questions`
3. **Usuário responde** → Interface envia para `/api/submit-answer`
4. **IA gera modelo** → Interface chama `/api/generate-model`
5. **JSON corrigido** → Aplicado automaticamente pelo servidor
6. **Usuário baixa JSON** → Pronto para usar no iStar

## 💡 Dicas

- **Cenários detalhados** geram melhores modelos
- **Responda todas as perguntas** completamente para melhores resultados
- **Valide o JSON** antes de usar no iStar
- O JSON gerado já está corrigido e pronto para uso

