# 🚀 Como Usar o Projeto - Guia Rápido

## Teste Rápido (5 minutos)

### Passo 1: Instalar dependências

```bash
pip3 install openai
```

### Passo 2: Configurar sua chave de API

```bash
export OPENAI_API_KEY='sua-chave-aqui'
```

**⚠️ IMPORTANTE:** Substitua `'sua-chave-aqui'` pela sua chave real da OpenAI.

### Passo 3: Executar o teste

```bash
python3 test_project.py
```

### Passo 4: Ver o resultado

```bash
cat models/baseline/test_output.json
```

---

## O que o script faz?

1. ✅ Lê o prompt baseline (`prompts/baseline_final.txt`)
2. ✅ Lê o cenário de teste (`scenarios/scenario_001_taxi_app.md`)
3. ✅ Prepara o prompt completo
4. ✅ Envia para a API da OpenAI (GPT-4)
5. ✅ Recebe a resposta
6. ✅ Extrai e valida o JSON
7. ✅ Salva em `models/baseline/test_output.json`
8. ✅ Mostra estatísticas do modelo gerado

---

## Exemplo de Saída

```
============================================================
🔭 I SEE STARS - Teste do Projeto
============================================================

📝 Preparando prompt...
✅ Prompt preparado!
🤖 Enviando para GPT-4...
   (Isso pode levar alguns segundos...)
✅ Resposta recebida!

🔍 Extraindo JSON da resposta...
✅ Validando JSON...
✅ JSON válido!

💾 Salvo em: models/baseline/test_output.json

📊 Estatísticas do Modelo:
   Atores: 3
   Nodes (goals/tasks/qualities): 8
   Dependencies: 4
   Links: 2

✅ Validação:
   ✅ tool = pistar.2.0.0
   ✅ istar = 2.0

============================================================
✅ Teste concluído com sucesso!
============================================================

📁 Você pode ver o JSON gerado em:
   models/baseline/test_output.json
```

---

## Troubleshooting

### Erro: "openai não instalado"
```bash
pip3 install openai
```

### Erro: "OPENAI_API_KEY não configurada"
```bash
export OPENAI_API_KEY='sua-chave-aqui'
```

### Erro: "Arquivo não encontrado"
Certifique-se de estar na pasta correta:
```bash
pwd
# Deve mostrar: /Users/fernandapascoal/Desktop/iSeeStars-LLM4RE
```

### Erro: "JSON inválido"
O script mostra a resposta completa. Verifique se o LLM retornou JSON válido.

---

## Próximos Passos

Após o teste funcionar:

1. **Testar outros cenários:**
   - Edite `test_project.py` e mude `scenario_001_taxi_app.md` para `scenario_002_library_system.md`

2. **Testar validação:**
   - Use o JSON gerado com `prompts/json_validator.txt`

3. **Testar fluxo interativo:**
   - Use `prompts/interactive_master.txt` manualmente no ChatGPT/Claude

---

**Boa sorte! 🎉**




