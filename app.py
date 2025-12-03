#!/usr/bin/env python3
"""
Servidor Flask para interface web interativa do I See Stars
"""

import os
import json
import uuid
from flask import Flask, render_template, request, jsonify, session
# Não importar OpenAI aqui - será importado dentro da função get_openai_client()
# para evitar problemas de compatibilidade e conflitos de versão

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Inicializar cliente OpenAI
def get_openai_client():
    """
    Cria e retorna um cliente OpenAI.
    Tenta múltiplas abordagens para garantir compatibilidade.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY não configurada")
    
    # Importar OpenAI dentro da função para evitar problemas de importação
    try:
        from openai import OpenAI as OpenAIClient
    except ImportError as e:
        raise ValueError(f"Erro ao importar biblioteca OpenAI: {e}")
    
    # Tentar múltiplas abordagens
    approaches = [
        # Abordagem 1: Usar variável de ambiente (mais seguro)
        lambda: OpenAIClient(),
        # Abordagem 2: Passar api_key explicitamente
        lambda: OpenAIClient(api_key=api_key),
    ]
    
    last_error = None
    for i, approach in enumerate(approaches, 1):
        try:
            # Garantir que a variável de ambiente está configurada
            os.environ['OPENAI_API_KEY'] = api_key
            client = approach()
            # Testar se o cliente funciona fazendo uma chamada simples (não vamos realmente chamar)
            return client
        except (TypeError, ValueError) as e:
            error_msg = str(e)
            last_error = e
            # Se o erro mencionar 'proxies', pode ser um problema de versão
            if 'proxies' in error_msg.lower() and i < len(approaches):
                # Tentar próxima abordagem
                continue
            elif 'proxies' in error_msg.lower():
                # Última tentativa: verificar versão e sugerir atualização
                import openai
                raise ValueError(
                    f"Erro de compatibilidade com biblioteca OpenAI. "
                    f"Versão instalada: {openai.__version__}. "
                    f"O erro 'proxies' indica possível incompatibilidade. "
                    f"Tente executar: pip install --upgrade --force-reinstall openai httpx. "
                    f"Erro original: {error_msg}"
                )
            else:
                # Outro tipo de erro, propagar
                raise ValueError(f"Erro ao inicializar cliente OpenAI: {error_msg}")
        except Exception as e:
            last_error = e
            if i < len(approaches):
                continue
            raise ValueError(f"Erro ao inicializar cliente OpenAI: {str(e)}")
    
    # Se chegou aqui, todas as abordagens falharam
    if last_error:
        raise ValueError(f"Erro ao inicializar cliente OpenAI após tentar múltiplas abordagens: {str(last_error)}")
    raise ValueError("Erro desconhecido ao inicializar cliente OpenAI")

def ler_arquivo(caminho):
    """Lê um arquivo e retorna o conteúdo"""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def corrigir_json(dados):
    """Corrige JSON adicionando campos obrigatórios e corrigindo erros"""
    import uuid as uuid_lib
    
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
                    new_id = str(uuid_lib.uuid4())
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
    
    dados_corrigidos = converter_ids_para_uuid(dados)
    
    # Corrigir tipos de dependencies
    if 'dependencies' in dados_corrigidos:
        for dep in dados_corrigidos['dependencies']:
            if dep.get('type') == 'istar.DependencyLink':
                dep['type'] = 'istar.Goal'
    
    # Coletar IDs de atores e nodes
    ator_ids = set()
    node_ids = set()
    
    if 'actors' in dados_corrigidos:
        for actor in dados_corrigidos['actors']:
            ator_ids.add(actor.get('id'))
            for node in actor.get('nodes', []):
                node_ids.add(node.get('id'))
    
    # Remover links que conectam atores diretamente
    if 'links' in dados_corrigidos:
        links_validos = []
        for link in dados_corrigidos['links']:
            source = link.get('source')
            target = link.get('target')
            if source in ator_ids or target in ator_ids:
                continue
            links_validos.append(link)
        dados_corrigidos['links'] = links_validos
    
    # Garantir campos obrigatórios
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
    
    return dados_corrigidos

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/start', methods=['POST'])
def start_session():
    """Inicia uma nova sessão de elicitação"""
    data = request.json
    cenario = data.get('cenario', '').strip()
    
    if not cenario:
        return jsonify({'error': 'Cenário não pode estar vazio'}), 400
    
    # Inicializar sessão
    session_id = str(uuid.uuid4())
    session['session_id'] = session_id
    session['cenario'] = cenario
    session['respostas'] = []
    session['perguntas'] = []
    session['estado'] = 'gerando_perguntas'
    
    return jsonify({
        'session_id': session_id,
        'status': 'success'
    })

@app.route('/api/generate-questions', methods=['POST'])
def generate_questions():
    """Gera perguntas de clarificação baseadas no cenário"""
    try:
        cenario = session.get('cenario')
        if not cenario:
            return jsonify({'error': 'Cenário não encontrado'}), 400
        
        # Carregar prompt interativo
        prompt_template = ler_arquivo('prompts/interactive_master.txt')
        if not prompt_template:
            return jsonify({'error': 'Prompt interativo não encontrado'}), 500
        
        # Substituir cenário no prompt
        prompt_completo = prompt_template.replace('[INSERIR CENÁRIO AQUI]', cenario)
        
        # Adicionar instrução para gerar primeira rodada de perguntas
        prompt_completo += "\n\nIMPORTANTE: Neste momento, gere APENAS a primeira rodada de 5-8 perguntas de clarificação. Numere as perguntas (1, 2, 3, etc). Não gere o modelo JSON ainda."
        
        # Chamar API
        try:
            client = get_openai_client()
        except Exception as e:
            return jsonify({'error': f'Erro ao inicializar cliente OpenAI: {str(e)}'}), 500
        
        model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt_completo}
                ],
                temperature=0.7,
                max_tokens=1500
            )
        except Exception as e:
            return jsonify({'error': f'Erro ao chamar API OpenAI: {str(e)}'}), 500
        
        resposta_texto = response.choices[0].message.content
        
        # Extrair perguntas (simples: dividir por linhas numeradas)
        perguntas = []
        linhas = resposta_texto.split('\n')
        for linha in linhas:
            linha = linha.strip()
            # Procurar por linhas que começam com número seguido de ponto ou parêntese
            if linha and (linha[0].isdigit() or linha.startswith('•') or linha.startswith('-') or '?' in linha):
                # Limpar formatação
                linha_limpa = linha.lstrip('0123456789. •-()[]').strip()
                if linha_limpa and '?' in linha_limpa:
                    perguntas.append(linha_limpa)
        
        # Se não encontrou perguntas numeradas, usar a resposta completa
        if not perguntas:
            # Dividir por parágrafos que terminam com ?
            partes = resposta_texto.split('?')
            for parte in partes:
                parte_limpa = parte.strip()
                if parte_limpa and len(parte_limpa) > 20:
                    perguntas.append(parte_limpa + '?')
                    if len(perguntas) >= 8:
                        break
        
        # Limitar a 8 perguntas
        perguntas = perguntas[:8]
        
        session['perguntas'] = perguntas
        session['estado'] = 'aguardando_respostas'
        
        return jsonify({
            'perguntas': perguntas,
            'resposta_completa': resposta_texto,
            'status': 'success'
        })
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Erro em generate_questions: {error_details}")
        return jsonify({'error': f'Erro ao gerar perguntas: {str(e)}'}), 500

@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    """Submete uma resposta do usuário"""
    data = request.json
    pergunta_id = data.get('pergunta_id')
    resposta = data.get('resposta', '').strip()
    
    if not resposta:
        return jsonify({'error': 'Resposta não pode estar vazia'}), 400
    
    respostas = session.get('respostas', [])
    respostas.append({
        'pergunta_id': pergunta_id,
        'resposta': resposta
    })
    session['respostas'] = respostas
    
    return jsonify({'status': 'success'})

@app.route('/api/generate-model', methods=['POST'])
def generate_model():
    """Gera o modelo iStar 2.0 final"""
    try:
        cenario = session.get('cenario')
        respostas = session.get('respostas', [])
        
        if not cenario:
            return jsonify({'error': 'Cenário não encontrado'}), 400
        
        # Carregar prompt de geração final
        prompt_template = ler_arquivo('prompts/final_json_generation.txt')
        if not prompt_template:
            return jsonify({'error': 'Prompt de geração não encontrado'}), 500
        
        # Construir contexto com cenário e respostas
        contexto_cenario = cenario
        
        contexto_respostas = ""
        if respostas:
            perguntas = session.get('perguntas', [])
            for i, resp in enumerate(respostas):
                pergunta_texto = perguntas[resp['pergunta_id']] if resp['pergunta_id'] < len(perguntas) else f"Pergunta {resp['pergunta_id'] + 1}"
                contexto_respostas += f"Q: {pergunta_texto}\nA: {resp['resposta']}\n\n"
        
        # Substituir placeholders no prompt
        prompt_completo = prompt_template.replace('[CENÁRIO ORIGINAL]', contexto_cenario)
        
        # Adicionar respostas se houver
        if contexto_respostas:
            # Se houver placeholder para respostas, substituir; senão, adicionar após o cenário
            if '[RESPOSTAS DO USUÁRIO]' in prompt_completo:
                prompt_completo = prompt_completo.replace('[RESPOSTAS DO USUÁRIO]', contexto_respostas)
            elif '[LISTA DE ATORES]' in prompt_completo:
                # Adicionar respostas antes da seção de informações coletadas
                prompt_completo = prompt_completo.replace(
                    '- Cenário original: [CENÁRIO ORIGINAL]',
                    f"- Cenário original: {contexto_cenario}\n- Respostas do usuário:\n{contexto_respostas}"
                )
            else:
                # Adicionar no início da seção de informações coletadas
                prompt_completo = prompt_completo.replace(
                    'INFORMAÇÕES COLETADAS:',
                    f'INFORMAÇÕES COLETADAS:\n\nRESPOSTAS DO USUÁRIO:\n{contexto_respostas}'
                )
        
        # Garantir que o prompt tenha instrução clara
        if 'Retorne APENAS o JSON' not in prompt_completo:
            prompt_completo += "\n\nIMPORTANTE: Retorne APENAS o JSON do modelo, sem explicações ou texto adicional."
        
        # Chamar API
        try:
            client = get_openai_client()
        except Exception as e:
            return jsonify({'error': f'Erro ao inicializar cliente OpenAI: {str(e)}'}), 500
        
        model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt_completo}
                ],
                temperature=0.3,
                max_tokens=4000
            )
        except Exception as e:
            return jsonify({'error': f'Erro ao chamar API OpenAI: {str(e)}'}), 500
        
        resposta_texto = response.choices[0].message.content
        
        # Extrair JSON
        json_texto = resposta_texto
        if "```json" in resposta_texto:
            inicio = resposta_texto.find("```json") + 7
            fim = resposta_texto.find("```", inicio)
            json_texto = resposta_texto[inicio:fim].strip()
        elif "```" in resposta_texto:
            inicio = resposta_texto.find("```") + 3
            fim = resposta_texto.find("```", inicio)
            json_texto = resposta_texto[inicio:fim].strip()
        else:
            # Tentar encontrar JSON direto
            inicio = resposta_texto.find("{")
            fim = resposta_texto.rfind("}") + 1
            if inicio >= 0 and fim > inicio:
                json_texto = resposta_texto[inicio:fim]
        
        # Validar e corrigir JSON
        try:
            dados = json.loads(json_texto)
            dados_corrigidos = corrigir_json(dados)
            
            session['modelo_json'] = dados_corrigidos
            session['estado'] = 'modelo_gerado'
            
            return jsonify({
                'modelo': dados_corrigidos,
                'status': 'success'
            })
        except json.JSONDecodeError as e:
            return jsonify({
                'error': f'JSON inválido: {str(e)}',
                'resposta_bruta': resposta_texto[:500]
            }), 400
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Erro em generate_model: {error_details}")
        return jsonify({'error': f'Erro ao gerar modelo: {str(e)}'}), 500

@app.route('/api/download-model', methods=['GET'])
def download_model():
    """Baixa o modelo JSON gerado"""
    modelo = session.get('modelo_json')
    if not modelo:
        return jsonify({'error': 'Modelo não encontrado'}), 404
    
    return jsonify(modelo)

if __name__ == '__main__':
    # Verificar se API key está configurada
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  AVISO: OPENAI_API_KEY não configurada!")
        print("   Execute: export OPENAI_API_KEY='sua-chave'")
    
    print("=" * 60)
    print("🔭 I SEE STARS - Interface Web")
    print("=" * 60)
    print()
    print("🌐 Servidor iniciando em: http://localhost:5000")
    print("📝 Certifique-se de que OPENAI_API_KEY está configurada")
    print()
    print("Pressione Ctrl+C para parar o servidor")
    print("=" * 60)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5001)

