#!/usr/bin/env python3
"""
Script para testar o projeto I See Stars
Gera um modelo iStar 2.0 a partir de um cenário
"""

import os
import json
from pathlib import Path

# Verificar se openai está instalado
try:
    from openai import OpenAI
except ImportError:
    print("❌ Erro: biblioteca 'openai' não instalada")
    print("   Execute: pip3 install openai")
    exit(1)

def ler_arquivo(caminho):
    """Lê um arquivo e retorna o conteúdo"""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho}")
        return None

def extrair_descricao_cenario(arquivo_cenario):
    """Extrai apenas a descrição do cenário"""
    conteudo = ler_arquivo(arquivo_cenario)
    if not conteudo:
        return None
    
    linhas = conteudo.split('\n')
    descricao = []
    dentro_descricao = False
    
    for linha in linhas:
        if linha.strip() == "## Description":
            dentro_descricao = True
            continue
        if dentro_descricao and linha.strip().startswith("##"):
            break
        if dentro_descricao:
            linha_limpa = linha.strip()
            if linha_limpa:
                descricao.append(linha_limpa)
    
    return ' '.join(descricao)

def preparar_prompt():
    """Prepara o prompt completo com o cenário"""
    print("📝 Preparando prompt...")
    
    # Ler o prompt baseline
    prompt_template = ler_arquivo('prompts/baseline_final.txt')
    if not prompt_template:
        return None
    
    # Ler e extrair o cenário
    cenario = extrair_descricao_cenario('scenarios/scenario_001_taxi_app.md')
    if not cenario:
        return None
    
    # Substituir o placeholder
    prompt_completo = prompt_template.replace('[INSERIR CENÁRIO AQUI]', cenario)
    
    print("✅ Prompt preparado!")
    return prompt_completo

def chamar_api(prompt_texto):
    """Chama a API da OpenAI"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Erro: OPENAI_API_KEY não configurada")
        print("   Execute: export OPENAI_API_KEY='sua-chave'")
        return None
    
    print("🤖 Enviando para GPT-4...")
    print("   (Isso pode levar alguns segundos...)")
    
    try:
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            #model="gpt-3.5-turbo",
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt_texto}
            ],
            temperature=0.3,
            max_tokens=3000
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"❌ Erro ao chamar API: {e}")
        return None

def extrair_json(resposta):
    """Extrai JSON da resposta, mesmo se estiver em code blocks"""
    # Tentar encontrar JSON em code blocks
    if "```json" in resposta:
        inicio = resposta.find("```json") + 7
        fim = resposta.find("```", inicio)
        json_texto = resposta[inicio:fim].strip()
    elif "```" in resposta:
        inicio = resposta.find("```") + 3
        fim = resposta.find("```", inicio)
        json_texto = resposta[inicio:fim].strip()
    else:
        # Tentar encontrar JSON direto
        inicio = resposta.find("{")
        fim = resposta.rfind("}") + 1
        if inicio >= 0 and fim > inicio:
            json_texto = resposta[inicio:fim]
        else:
            json_texto = resposta
    
    return json_texto

def validar_json(json_texto):
    """Valida se o texto é JSON válido"""
    try:
        dados = json.loads(json_texto)
        return True, dados
    except json.JSONDecodeError as e:
        return False, str(e)

def salvar_resultado(dados_json, caminho):
    """Salva o JSON em arquivo"""
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados_json, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Salvo em: {caminho}")

def mostrar_estatisticas(dados):
    """Mostra estatísticas do modelo gerado"""
    atores = len(dados.get('actors', []))
    nodes_total = sum(len(ator.get('nodes', [])) for ator in dados.get('actors', []))
    dependencies = len(dados.get('dependencies', []))
    links = len(dados.get('links', []))
    
    print("\n📊 Estatísticas do Modelo:")
    print(f"   Atores: {atores}")
    print(f"   Nodes (goals/tasks/qualities): {nodes_total}")
    print(f"   Dependencies: {dependencies}")
    print(f"   Links: {links}")
    
    # Verificar campos obrigatórios
    tool = dados.get('tool', 'N/A')
    istar = dados.get('istar', 'N/A')
    
    print(f"\n✅ Validação:")
    if tool == "pistar.2.0.0":
        print(f"   ✅ tool = {tool}")
    else:
        print(f"   ❌ tool = {tool} (deveria ser 'pistar.2.0.0')")
    
    if istar == "2.0":
        print(f"   ✅ istar = {istar}")
    else:
        print(f"   ❌ istar = {istar} (deveria ser '2.0')")

def main():
    print("=" * 60)
    print("🔭 I SEE STARS - Teste do Projeto")
    print("=" * 60)
    print()
    
    # 1. Preparar prompt
    prompt = preparar_prompt()
    if not prompt:
        print("❌ Não foi possível preparar o prompt")
        return
    
    # 2. Chamar API
    resposta = chamar_api(prompt)
    if not resposta:
        print("❌ Não foi possível obter resposta da API")
        return
    
    print("✅ Resposta recebida!")
    print()
    
    # 3. Extrair JSON
    print("🔍 Extraindo JSON da resposta...")
    json_texto = extrair_json(resposta)
    
    # 4. Validar JSON
    print("✅ Validando JSON...")
    valido, resultado = validar_json(json_texto)
    
    if not valido:
        print(f"❌ JSON inválido!")
        print(f"   Erro: {resultado}")
        print()
        print("📋 Resposta completa (primeiros 500 caracteres):")
        print(resposta[:500])
        return
    
    print("✅ JSON válido!")
    print()
    
    # 5. Salvar resultado
    caminho_saida = 'models/baseline/test_output.json'
    salvar_resultado(resultado, caminho_saida)
    
    # 6. Corrigir JSON (adicionar customProperties e converter IDs para UUIDs)
    print("\n🔧 Corrigindo JSON para compatibilidade com ferramenta iStar...")
    try:
        import sys
        import uuid
        
        def adicionar_custom_properties(obj):
            if 'customProperties' not in obj:
                obj['customProperties'] = {"Description": ""}
            return obj
        
        def converter_ids_para_uuid(obj, id_map=None):
            if id_map is None:
                id_map = {}
            
            if isinstance(obj, dict):
                if 'id' in obj:
                    old_id = obj['id']
                    if not (isinstance(old_id, str) and len(old_id) == 36 and old_id.count('-') == 4):
                        new_id = str(uuid.uuid4())
                        id_map[old_id] = new_id
                        obj['id'] = new_id
                    else:
                        id_map[old_id] = old_id
                
                if 'type' in obj and any(t in str(obj.get('type', '')) for t in ['istar.Actor', 'istar.Agent', 'istar.Role', 'istar.Goal', 'istar.Task', 'istar.Quality', 'istar.Resource']):
                    obj = adicionar_custom_properties(obj)
                
                for key, value in obj.items():
                    if key == 'source' or key == 'target':
                        if value in id_map:
                            obj[key] = id_map[value]
                    else:
                        obj[key] = converter_ids_para_uuid(value, id_map)
            elif isinstance(obj, list):
                return [converter_ids_para_uuid(item, id_map) for item in obj]
            
            return obj
        
        resultado = converter_ids_para_uuid(resultado)
        
        # Corrigir tipos de dependencies (NUNCA pode ser DependencyLink)
        if 'dependencies' in resultado:
            for dep in resultado['dependencies']:
                if dep.get('type') == 'istar.DependencyLink':
                    print(f"⚠️  Corrigindo dependency com tipo inválido: {dep.get('id', 'unknown')}")
                    dep['type'] = 'istar.Goal'  # Padrão: Goal
        
        # Coletar todos os IDs de atores e nodes
        ator_ids = set()
        node_ids = set()
        
        if 'actors' in resultado:
            for actor in resultado['actors']:
                ator_ids.add(actor.get('id'))
                for node in actor.get('nodes', []):
                    node_ids.add(node.get('id'))
        
        # Remover links que conectam atores diretamente (devem conectar nodes)
        if 'links' in resultado:
            links_validos = []
            for link in resultado['links']:
                source = link.get('source')
                target = link.get('target')
                if source in ator_ids or target in ator_ids:
                    print(f"⚠️  Removendo link inválido que conecta atores: {link.get('id', 'unknown')}")
                    continue
                links_validos.append(link)
            resultado['links'] = links_validos
        
        # Garantir campos obrigatórios
        if 'tool' not in resultado or resultado['tool'] != 'pistar.2.0.0':
            resultado['tool'] = 'pistar.2.0.0'
        if 'istar' not in resultado or resultado['istar'] != '2.0':
            resultado['istar'] = '2.0'
        if 'display' not in resultado:
            resultado['display'] = {}
        if 'orphans' not in resultado:
            resultado['orphans'] = []
        if 'diagram' not in resultado:
            resultado['diagram'] = {
                "width": 1700,
                "height": 1300,
                "name": "",
                "customProperties": {}
            }
        
        # Salvar JSON corrigido
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, indent=2, ensure_ascii=False)
        
        print("✅ JSON corrigido!")
    except Exception as e:
        print(f"⚠️  Não foi possível corrigir automaticamente: {e}")
        print("   Você pode corrigir manualmente usando: python3 fix_json.py models/baseline/test_output.json")
    
    # 7. Mostrar estatísticas
    mostrar_estatisticas(resultado)
    
    print()
    print("=" * 60)
    print("✅ Teste concluído com sucesso!")
    print("=" * 60)
    print()
    print("📁 Você pode ver o JSON gerado em:")
    print(f"   {caminho_saida}")

if __name__ == "__main__":
    main()

