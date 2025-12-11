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
    
    # Configurar timeout para httpx (usado internamente pelo OpenAI)
    timeout_config = None
    try:
        import httpx
        timeout_config = httpx.Timeout(60.0, connect=10.0)  # 60s total, 10s para conectar
    except ImportError:
        pass  # httpx pode não estar disponível, usar sem timeout
    
    # Tentar múltiplas abordagens
    approaches = []
    if timeout_config:
        approaches.extend([
            # Abordagem 1: Usar variável de ambiente com timeout
            lambda: OpenAIClient(timeout=timeout_config),
            # Abordagem 2: Passar api_key explicitamente com timeout
            lambda: OpenAIClient(api_key=api_key, timeout=timeout_config),
        ])
    # Fallbacks sem timeout
    approaches.extend([
        # Abordagem 3: Sem timeout
        lambda: OpenAIClient(),
        # Abordagem 4: Com api_key sem timeout
        lambda: OpenAIClient(api_key=api_key),
    ])
    
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
    if 'tool' not in dados_corrigidos:
        dados_corrigidos['tool'] = 'pistar.2.0.0'
    elif dados_corrigidos['tool'] not in ['pistar.2.0.0', 'pistar.2.1.0']:
        dados_corrigidos['tool'] = 'pistar.2.0.0'
    
    if 'istar' not in dados_corrigidos or dados_corrigidos['istar'] != '2.0':
        dados_corrigidos['istar'] = '2.0'
    
    if 'orphans' not in dados_corrigidos:
        dados_corrigidos['orphans'] = []
    
    if 'display' not in dados_corrigidos:
        dados_corrigidos['display'] = {}
    
    # Garantir que display tenha informações básicas se necessário
    if not dados_corrigidos['display'] and 'actors' in dados_corrigidos:
        # Adicionar informações básicas de display para atores (opcional)
        for actor in dados_corrigidos['actors']:
            actor_id = actor.get('id')
            if actor_id:
                dados_corrigidos['display'][actor_id] = {'collapsed': False}
    
    if 'diagram' not in dados_corrigidos:
        dados_corrigidos['diagram'] = {
            "width": 1700,
            "height": 1300,
            "name": "",
            "customProperties": {}
        }
    elif 'customProperties' not in dados_corrigidos['diagram']:
        dados_corrigidos['diagram']['customProperties'] = {}
    
    if 'saveDate' not in dados_corrigidos:
        dados_corrigidos['saveDate'] = ""
    
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
    session['conversa'] = []  # Histórico da conversa
    session['num_perguntas'] = 0  # Contador de perguntas
    session['estado'] = 'conversando'
    
    return jsonify({
        'session_id': session_id,
        'status': 'success'
    })

@app.route('/api/ask-question', methods=['POST'])
def ask_question():
    """Gera a próxima pergunta baseada no contexto da conversa"""
    try:
        print(f"\n{'='*80}")
        print("API /api/ask-question chamada")
        print(f"Session ID: {session.get('session_id', 'N/A')}")
        print(f"{'='*80}\n")
        
        cenario = session.get('cenario')
        conversa = session.get('conversa', [])
        num_perguntas = session.get('num_perguntas', 0)
        
        print(f"Cenário encontrado: {cenario is not None}")
        print(f"Tamanho da conversa: {len(conversa)}")
        print(f"Número de perguntas: {num_perguntas}")
        
        if not cenario:
            print("ERRO: Cenário não encontrado na sessão")
            return jsonify({'error': 'Cenário não encontrado. Por favor, inicie uma nova sessão.'}), 400
        
        # Limite de 5 perguntas - se já atingiu, forçar geração
        if num_perguntas >= 5:
            session['estado'] = 'pronto_para_gerar'
            return jsonify({
                'pergunta': None,
                'mensagem': 'Limite de 5 perguntas atingido. Tenho informações suficientes para gerar o modelo.',
                'pronto_para_gerar': True,
                'status': 'success'
            })
        
        # Carregar prompt conversacional (versão compacta para melhor performance)
        prompt_template = ler_arquivo('prompts/conversational_elicitation_compact.txt')
        if not prompt_template:
            # Fallback para versão completa se compacta não existir
            prompt_template = ler_arquivo('prompts/conversational_elicitation.txt')
        if not prompt_template:
            return jsonify({'error': 'Prompt conversacional não encontrado'}), 500
        
        # Construir histórico da conversa
        historico_texto = ""
        num_perguntas_feitas = sum(1 for item in conversa if item['tipo'] == 'pergunta')
        
        if conversa:
            for item in conversa:
                if item['tipo'] == 'pergunta':
                    historico_texto += f"IA: {item['texto']}\n\n"
                elif item['tipo'] == 'resposta':
                    historico_texto += f"Usuário: {item['texto']}\n\n"
        else:
            historico_texto = "(Esta é a primeira interação - ainda não há histórico)"
        
        # Adicionar informação sobre número de perguntas
        historico_texto += f"\n⚠️ IMPORTANTE: Você já fez {num_perguntas_feitas} pergunta(s). Você tem NO MÁXIMO 5 perguntas no total.\n"
        if num_perguntas_feitas >= 4:
            historico_texto += "⚠️ ATENÇÃO: Esta deve ser sua ÚLTIMA pergunta (5ª). Após esta, você DEVE indicar que está pronto para gerar o modelo.\n"
        
        # Substituir placeholders no prompt
        prompt_completo = prompt_template.replace('[INSERIR CENÁRIO AQUI]', cenario)
        prompt_completo = prompt_completo.replace('[INSERIR HISTÓRICO AQUI]', historico_texto)
        
        # Limitar tamanho do histórico para melhorar performance
        if len(historico_texto) > 2000:
            print(f"⚠️ Histórico grande ({len(historico_texto)} caracteres). Reduzindo para melhorar performance...")
            # Manter apenas últimas 2-3 interações (últimas perguntas e respostas)
            linhas_historico = historico_texto.split('\n\n')
            # Manter últimas 4-6 linhas (2-3 interações Q+A)
            historico_reduzido = '\n\n'.join(linhas_historico[-6:])
            historico_texto = historico_reduzido
            print(f"✓ Histórico reduzido para {len(historico_texto)} caracteres")
        
        # Limitar tamanho do cenário se muito grande
        if len(cenario) > 2000:
            print(f"⚠️ Cenário muito grande ({len(cenario)} caracteres). Usando resumo...")
            cenario = cenario[:2000] + "..."
        
        # Reconstruir prompt com tamanhos limitados
        prompt_completo = prompt_template.replace('[INSERIR CENÁRIO AQUI]', cenario)
        prompt_completo = prompt_completo.replace('[INSERIR HISTÓRICO AQUI]', historico_texto)
        
        if len(prompt_completo) > 5000:
            print(f"⚠️ AVISO: Prompt ainda grande ({len(prompt_completo)} caracteres), mas dentro do limite aceitável.")
        
        # Chamar API
        try:
            client = get_openai_client()
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Erro ao inicializar cliente OpenAI: {error_details}")
            return jsonify({'error': f'Erro ao inicializar cliente OpenAI: {str(e)}'}), 500
        
        model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
        
        print(f"\n{'='*80}")
        print(f"Gerando pergunta {num_perguntas_feitas + 1} de 5")
        print(f"Modelo: {model}")
        print(f"Tamanho do prompt: {len(prompt_completo)} caracteres")
        print(f"{'='*80}\n")
        
        try:
            # Verificar se API key está configurada
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                return jsonify({'error': 'OPENAI_API_KEY não configurada. Configure a variável de ambiente antes de usar.'}), 500
            
            print(f"Chamando API OpenAI com modelo {model}...")
            print(f"Prompt tem {len(prompt_completo)} caracteres")
            
            # Chamar API com timeout através do cliente httpx
            import time
            start_time = time.time()
            
            try:
                # Usar configurações otimizadas para resposta mais rápida
                # max_tokens reduzido para acelerar (perguntas devem ser curtas)
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt_completo}
                    ],
                    temperature=0.7,
                    max_tokens=300  # Reduzido para 300 - perguntas devem ser curtas e diretas
                )
                elapsed_time = time.time() - start_time
                print(f"✓ Resposta recebida em {elapsed_time:.2f} segundos")
                print(f"✓ Tamanho da resposta: {len(response.choices[0].message.content)} caracteres")
            except Exception as api_error:
                elapsed_time = time.time() - start_time
                print(f"✗ Erro após {elapsed_time:.2f} segundos: {str(api_error)}")
                raise api_error
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"✗ Erro ao chamar API OpenAI: {error_details}")
            
            error_msg = str(e)
            error_lower = error_msg.lower()
            
            if 'api key' in error_lower or 'authentication' in error_lower or 'invalid api key' in error_lower:
                return jsonify({'error': 'Erro de autenticação. Verifique se OPENAI_API_KEY está configurada corretamente.'}), 500
            elif 'rate limit' in error_lower or 'quota' in error_lower:
                return jsonify({'error': 'Limite de taxa ou cota excedido. Aguarde alguns instantes e tente novamente.'}), 500
            elif 'timeout' in error_lower or 'timed out' in error_lower or 'connection' in error_lower:
                return jsonify({'error': 'Timeout na conexão com a API. Verifique sua conexão com a internet e tente novamente.'}), 500
            elif 'read timeout' in error_lower or 'request timeout' in error_lower:
                return jsonify({'error': 'A requisição demorou muito. O prompt pode estar muito grande. Tente com um cenário mais curto.'}), 500
            else:
                # Retornar erro mais detalhado para debug
                return jsonify({
                    'error': f'Erro ao chamar API OpenAI: {error_msg[:200]}',
                    'details': 'Verifique os logs do servidor para mais informações.'
                }), 500
        
        # Verificar se a resposta está vazia
        if not response.choices or not response.choices[0].message.content:
            print("ERRO: Resposta vazia da API OpenAI")
            return jsonify({'error': 'A API OpenAI retornou uma resposta vazia. Tente novamente.'}), 500
        
        resposta_texto = response.choices[0].message.content.strip()
        
        if not resposta_texto:
            print("ERRO: Resposta vazia após strip")
            return jsonify({'error': 'A API OpenAI retornou uma resposta vazia. Tente novamente.'}), 500
        
        print(f"Resposta processada: {resposta_texto[:100]}...")
        
        # Verificar se já atingiu o limite de perguntas
        num_perguntas = session.get('num_perguntas', 0)
        if num_perguntas >= 4:  # Se já fez 4 perguntas, esta será a última (5ª)
            # Forçar que está pronto após a 5ª pergunta
            session['estado'] = 'pronto_para_gerar'
            # Ainda mostra a pergunta, mas marca como última
            pass  # Continua para processar a pergunta
        
        # Verificar se a IA indicou que tem informações suficientes
        if 'informações suficientes' in resposta_texto.lower() or 'gerando modelo' in resposta_texto.lower():
            session['estado'] = 'pronto_para_gerar'
            return jsonify({
                'pergunta': None,
                'mensagem': resposta_texto,
                'pronto_para_gerar': True,
                'status': 'success'
            })
        
        # Extrair pergunta(s) da resposta
        perguntas = []
        linhas = resposta_texto.split('\n')
        for linha in linhas:
            linha = linha.strip()
            if linha and '?' in linha:
                # Limpar formatação inicial
                linha_limpa = linha.lstrip('0123456789. •-()[]').strip()
                if linha_limpa and len(linha_limpa) > 10:
                    perguntas.append(linha_limpa)
        
        # Se não encontrou perguntas claras, usar a resposta completa
        if not perguntas:
            # Tentar encontrar a primeira frase com ?
            partes = resposta_texto.split('?')
            for parte in partes:
                parte_limpa = parte.strip()
                if parte_limpa and len(parte_limpa) > 20:
                    perguntas.append(parte_limpa + '?')
                    break
        
        # Limitar a 2 perguntas por vez
        perguntas = perguntas[:2]
        
        if not perguntas:
            # Se ainda não encontrou, usar a resposta completa
            perguntas = [resposta_texto]
        
        # Adicionar pergunta(s) ao histórico
        for pergunta in perguntas:
            conversa.append({
                'tipo': 'pergunta',
                'texto': pergunta,
                'timestamp': str(uuid.uuid4())
            })
        
        # Incrementar contador de perguntas
        num_perguntas = session.get('num_perguntas', 0) + len(perguntas)
        session['num_perguntas'] = num_perguntas
        session['conversa'] = conversa
        
        # Se atingiu 5 perguntas, marcar como última pergunta
        if num_perguntas >= 5:
            session['estado'] = 'aguardando_resposta'  # Ainda aguarda resposta da última pergunta
            return jsonify({
                'perguntas': perguntas,
                'mensagem': resposta_texto,  # Mensagem original sem adicionar texto extra
                'pronto_para_gerar': False,  # Ainda não está pronto, precisa da resposta
                'ultima_pergunta': True,  # Marca como última pergunta
                'num_perguntas': num_perguntas,
                'status': 'success'
            })
        
        session['estado'] = 'aguardando_resposta'
        
        return jsonify({
            'perguntas': perguntas,
            'mensagem': resposta_texto,
            'pronto_para_gerar': False,
            'num_perguntas': num_perguntas,
            'status': 'success'
        })
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Erro em ask_question: {error_details}")
        return jsonify({'error': f'Erro ao gerar pergunta: {str(e)}'}), 500

@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    """Submete uma resposta do usuário"""
    data = request.json
    resposta = data.get('resposta', '').strip()
    
    if not resposta:
        return jsonify({'error': 'Resposta não pode estar vazia'}), 400
    
    # Adicionar resposta ao histórico da conversa
    conversa = session.get('conversa', [])
    conversa.append({
        'tipo': 'resposta',
        'texto': resposta,
        'timestamp': str(uuid.uuid4())
    })
    session['conversa'] = conversa
    
    # Também adicionar à lista de respostas (para compatibilidade)
    respostas = session.get('respostas', [])
    respostas.append({
        'resposta': resposta
    })
    session['respostas'] = respostas
    
    # Verificar se já atingiu 5 perguntas e todas foram respondidas
    num_perguntas = session.get('num_perguntas', 0)
    num_respostas = len([item for item in conversa if item['tipo'] == 'resposta'])
    
    if num_perguntas >= 5 and num_respostas >= 5:
        session['estado'] = 'pronto_para_gerar'
        return jsonify({
            'status': 'success',
            'pronto_para_gerar': True,
            'mensagem': 'Todas as perguntas foram respondidas. Você pode gerar o modelo agora.'
        })
    else:
        session['estado'] = 'conversando'
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
        
        # Construir contexto completo com cenário e histórico da conversa
        contexto_cenario = cenario
        
        # Usar histórico da conversa se disponível, senão usar respostas antigas
        conversa = session.get('conversa', [])
        contexto_completo = ""
        
        # Construir contexto completo da conversa
        if conversa:
            contexto_completo = "=== HISTÓRICO COMPLETO DA CONVERSA ===\n\n"
            for item in conversa:
                if item['tipo'] == 'pergunta':
                    contexto_completo += f"🤖 IA: {item['texto']}\n\n"
                elif item['tipo'] == 'resposta':
                    contexto_completo += f"👤 USUÁRIO: {item['texto']}\n\n"
                elif item['tipo'] == 'system':
                    contexto_completo += f"ℹ️ {item['texto']}\n\n"
        elif respostas:
            # Fallback para formato antigo
            perguntas = session.get('perguntas', [])
            contexto_completo = "=== PERGUNTAS E RESPOSTAS ===\n\n"
            for i, resp in enumerate(respostas):
                pergunta_texto = perguntas[resp.get('pergunta_id', i)] if resp.get('pergunta_id') and resp['pergunta_id'] < len(perguntas) else f"Pergunta {i + 1}"
                contexto_completo += f"Q: {pergunta_texto}\nA: {resp.get('resposta', resp)}\n\n"
        
        # Substituir placeholders no prompt
        prompt_completo = prompt_template.replace('[CENÁRIO ORIGINAL]', contexto_cenario)
        
        # Adicionar contexto completo da conversa de forma explícita
        if contexto_completo:
            # Primeiro, tentar substituir o placeholder específico
            if 'HISTÓRICO COMPLETO DA CONVERSA:\n[RESPOSTAS DO USUÁRIO]' in prompt_completo:
                prompt_completo = prompt_completo.replace(
                    'HISTÓRICO COMPLETO DA CONVERSA:\n[RESPOSTAS DO USUÁRIO]',
                    f'HISTÓRICO COMPLETO DA CONVERSA:\n{contexto_completo}'
                )
            elif '[RESPOSTAS DO USUÁRIO]' in prompt_completo:
                prompt_completo = prompt_completo.replace('[RESPOSTAS DO USUÁRIO]', contexto_completo)
            else:
                # Se não encontrou placeholder, adicionar após o cenário
                prompt_completo = prompt_completo.replace(
                    'CENÁRIO ORIGINAL:\n[CENÁRIO ORIGINAL]',
                    f'CENÁRIO ORIGINAL:\n{contexto_cenario}\n\nHISTÓRICO COMPLETO DA CONVERSA:\n{contexto_completo}'
                )
            
            # Log para debug
            print(f"\n{'='*80}")
            print("CONTEXTO DA CONVERSA ENVIADO PARA GERAÇÃO:")
            print(f"{'='*80}")
            print(f"Tamanho total do contexto: {len(contexto_completo)} caracteres")
            print(f"Número de interações: {len([item for item in conversa if item['tipo'] in ['pergunta', 'resposta']])}")
            print(f"\nPrimeiros 800 caracteres do contexto:")
            print(contexto_completo[:800] + "..." if len(contexto_completo) > 800 else contexto_completo)
            print(f"\nÚltimos 300 caracteres do contexto:")
            print("..." + contexto_completo[-300:] if len(contexto_completo) > 300 else contexto_completo)
            print(f"{'='*80}\n")
        
        # Adicionar instrução final explícita sobre usar todo o contexto
        if contexto_completo:
            prompt_completo += "\n\n" + "="*80 + "\n"
            prompt_completo += "INSTRUÇÃO FINAL CRÍTICA:\n"
            prompt_completo += "="*80 + "\n"
            prompt_completo += "Você recebeu uma conversa completa acima. O modelo JSON que você gerar DEVE:\n"
            prompt_completo += "1. Incluir TODAS as tarefas, recursos, objetivos e qualidades mencionados pelo usuário\n"
            prompt_completo += "2. Usar os nomes e descrições EXATAS fornecidas pelo usuário\n"
            prompt_completo += "3. Criar links e dependencies baseados nas informações da conversa\n"
            prompt_completo += "4. NÃO ignorar ou simplificar informações detalhadas fornecidas\n"
            prompt_completo += "5. Ser completo e refletir fielmente toda a conversa\n"
            prompt_completo += "\n"
        
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
                max_tokens=8000  # Aumentado para permitir modelos mais completos
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

