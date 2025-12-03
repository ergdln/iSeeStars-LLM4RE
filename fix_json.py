#!/usr/bin/env python3
"""
Script para corrigir JSON gerado e adicionar campos obrigatórios faltantes
"""

import json
import sys
import uuid
from pathlib import Path

def gerar_uuid():
    """Gera um UUID v4"""
    return str(uuid.uuid4())

def adicionar_custom_properties(obj):
    """Adiciona customProperties se não existir"""
    if 'customProperties' not in obj:
        obj['customProperties'] = {"Description": ""}
    return obj

def converter_ids_para_uuid(obj, id_map=None):
    """Converte IDs simples para UUIDs, mantendo referências"""
    if id_map is None:
        id_map = {}
    
    if isinstance(obj, dict):
        if 'id' in obj:
            old_id = obj['id']
            # Se não é UUID, gerar novo
            if not (isinstance(old_id, str) and len(old_id) == 36 and old_id.count('-') == 4):
                new_id = gerar_uuid()
                id_map[old_id] = new_id
                obj['id'] = new_id
            else:
                id_map[old_id] = old_id
        
        # Adicionar customProperties se necessário
        if 'type' in obj and any(t in str(obj.get('type', '')) for t in ['istar.Actor', 'istar.Agent', 'istar.Role', 'istar.Goal', 'istar.Task', 'istar.Quality', 'istar.Resource']):
            obj = adicionar_custom_properties(obj)
        
        # Processar recursivamente
        for key, value in obj.items():
            if key == 'source' or key == 'target':
                # Atualizar referências
                if value in id_map:
                    obj[key] = id_map[value]
            else:
                obj[key] = converter_ids_para_uuid(value, id_map)
    
    elif isinstance(obj, list):
        return [converter_ids_para_uuid(item, id_map) for item in obj]
    
    return obj

def corrigir_json(arquivo_entrada, arquivo_saida=None):
    """Corrige JSON adicionando campos obrigatórios"""
    
    # Ler JSON
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {arquivo_entrada}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido: {e}")
        return False
    
    print(f"📝 Corrigindo JSON: {arquivo_entrada}")
    
    # Converter IDs para UUIDs e adicionar customProperties
    dados_corrigidos = converter_ids_para_uuid(dados)
    
    # Corrigir tipos de dependencies (NUNCA pode ser DependencyLink)
    if 'dependencies' in dados_corrigidos:
        for dep in dados_corrigidos['dependencies']:
            if dep.get('type') == 'istar.DependencyLink':
                print(f"⚠️  Corrigindo dependency com tipo inválido: {dep.get('id', 'unknown')}")
                # Mudar para Goal por padrão (pode ser ajustado manualmente)
                dep['type'] = 'istar.Goal'
    
    # Coletar todos os IDs de atores e nodes
    ator_ids = set()
    node_ids = set()
    
    if 'actors' in dados_corrigidos:
        for actor in dados_corrigidos['actors']:
            ator_ids.add(actor.get('id'))
            for node in actor.get('nodes', []):
                node_ids.add(node.get('id'))
    
    # Remover links que conectam atores diretamente (devem conectar nodes)
    if 'links' in dados_corrigidos:
        links_validos = []
        for link in dados_corrigidos['links']:
            source = link.get('source')
            target = link.get('target')
            # Se source ou target são IDs de atores, remover o link
            if source in ator_ids or target in ator_ids:
                print(f"⚠️  Removendo link inválido que conecta atores: {link.get('id', 'unknown')}")
                continue
            links_validos.append(link)
        dados_corrigidos['links'] = links_validos
    
    # Garantir campos obrigatórios no nível raiz
    if 'tool' not in dados_corrigidos or dados_corrigidos['tool'] != 'pistar.2.0.0':
        dados_corrigidos['tool'] = 'pistar.2.0.0'
    
    if 'istar' not in dados_corrigidos or dados_corrigidos['istar'] != '2.0':
        dados_corrigidos['istar'] = '2.0'
    
    if 'display' not in dados_corrigidos:
        dados_corrigidos['display'] = {}
    
    if 'orphans' not in dados_corrigidos:
        dados_corrigidos['orphans'] = []
    
    if 'diagram' not in dados_corrigidos:
        dados_corrigidos['diagram'] = {
            "width": 1700,
            "height": 1300,
            "name": "",
            "customProperties": {}
        }
    
    # Salvar
    if arquivo_saida is None:
        arquivo_saida = arquivo_entrada.replace('.json', '_fixed.json')
    
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        json.dump(dados_corrigidos, f, indent=2, ensure_ascii=False)
    
    print(f"✅ JSON corrigido salvo em: {arquivo_saida}")
    
    # Estatísticas
    atores = len(dados_corrigidos.get('actors', []))
    nodes = sum(len(a.get('nodes', [])) for a in dados_corrigidos.get('actors', []))
    deps = len(dados_corrigidos.get('dependencies', []))
    links = len(dados_corrigidos.get('links', []))
    
    print(f"\n📊 Estatísticas:")
    print(f"   Atores: {atores}")
    print(f"   Nodes: {nodes}")
    print(f"   Dependencies: {deps}")
    print(f"   Links: {links}")
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 fix_json.py <arquivo.json> [arquivo_saida.json]")
        print("\nExemplo:")
        print("  python3 fix_json.py models/baseline/test_output.json")
        print("  python3 fix_json.py models/baseline/test_output.json models/baseline/test_output_fixed.json")
        sys.exit(1)
    
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2] if len(sys.argv) > 2 else None
    
    if corrigir_json(arquivo_entrada, arquivo_saida):
        print("\n✅ Correção concluída!")
    else:
        print("\n❌ Erro na correção")
        sys.exit(1)

if __name__ == "__main__":
    main()

