// Estado da aplicação
let state = {
    sessionId: null,
    cenario: null,
    conversa: [],
    modelo: null,
    prontoParaGerar: false
};

// Elementos DOM
const elements = {
    stepInput: document.getElementById('step-input'),
    stepQuestions: document.getElementById('step-questions'),
    stepModel: document.getElementById('step-model'),
    cenarioInput: document.getElementById('cenario-input'),
    btnStart: document.getElementById('btn-start'),
    btnLoadExample: document.getElementById('btn-load-example'),
    loadingQuestions: document.getElementById('loading-questions'),
    chatMessages: document.getElementById('chat-messages'),
    chatInput: document.getElementById('chat-input'),
    chatInputContainer: document.getElementById('chat-input-container'),
    btnSendAnswer: document.getElementById('btn-send-answer'),
    questionsButtons: document.getElementById('questions-buttons'),
    btnGenerateModel: document.getElementById('btn-generate-model'),
    loadingModel: document.getElementById('loading-model'),
    modelContainer: document.getElementById('model-container'),
    jsonOutput: document.getElementById('json-output'),
    modelStats: document.getElementById('model-stats'),
    btnCopyJson: document.getElementById('btn-copy-json'),
    btnDownloadJson: document.getElementById('btn-download-json'),
    btnNewSession: document.getElementById('btn-new-session'),
    btnValidateJson: document.getElementById('btn-validate-json'),
    errorMessage: document.getElementById('error-message')
};

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
});

function setupEventListeners() {
    elements.btnStart.addEventListener('click', handleStart);
    elements.btnLoadExample.addEventListener('click', loadExample);
    elements.btnSendAnswer.addEventListener('click', handleSendAnswer);
    elements.btnGenerateModel.addEventListener('click', handleGenerateModel);
    elements.btnCopyJson.addEventListener('click', copyJson);
    elements.btnDownloadJson.addEventListener('click', downloadJson);
    elements.btnNewSession.addEventListener('click', resetSession);
    elements.btnValidateJson.addEventListener('click', validateJson);
    
    // Permitir enviar resposta com Enter (Shift+Enter para nova linha)
    elements.chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendAnswer();
        }
    });
}

function showError(message) {
    elements.errorMessage.textContent = message;
    elements.errorMessage.style.display = 'block';
    setTimeout(() => {
        elements.errorMessage.style.display = 'none';
    }, 5000);
}

function showStep(stepName) {
    elements.stepInput.classList.remove('active');
    elements.stepQuestions.classList.remove('active');
    elements.stepModel.classList.remove('active');
    
    if (stepName === 'input') {
        elements.stepInput.classList.add('active');
    } else if (stepName === 'questions') {
        elements.stepQuestions.classList.add('active');
    } else if (stepName === 'model') {
        elements.stepModel.classList.add('active');
    }
}

async function handleStart() {
    const cenario = elements.cenarioInput.value.trim();
    
    if (!cenario) {
        showError('Por favor, insira um cenário de requisitos.');
        return;
    }
    
    if (cenario.length < 50) {
        showError('O cenário deve ter pelo menos 50 caracteres.');
        return;
    }
    
    state.cenario = cenario;
    elements.btnStart.disabled = true;
    elements.btnStart.textContent = 'Iniciando...';
    
    try {
        // Iniciar sessão
        const response = await fetch('/api/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ cenario })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Erro ao iniciar sessão');
        }
        
        const data = await response.json();
        state.sessionId = data.session_id;
        
        // Iniciar conversa
        showStep('questions');
        addMessage('system', `Cenário recebido: "${state.cenario.substring(0, 100)}..."`);
        await askNextQuestion();
        
    } catch (error) {
        showError(error.message);
        elements.btnStart.disabled = false;
        elements.btnStart.textContent = 'Iniciar Elicitação';
    }
}

async function askNextQuestion() {
    elements.loadingQuestions.style.display = 'block';
    elements.chatInputContainer.style.display = 'none';
    
    try {
        const response = await fetch('/api/ask-question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Erro ao gerar pergunta');
        }
        
        const data = await response.json();
        
        if (data.pronto_para_gerar) {
            // IA indicou que tem informações suficientes
            addMessage('ai', data.mensagem || 'Tenho informações suficientes para gerar o modelo.');
            state.prontoParaGerar = true;
            elements.questionsButtons.style.display = 'flex';
            elements.chatInputContainer.style.display = 'none';
        } else {
            // Adicionar pergunta(s) ao chat
            if (data.perguntas && data.perguntas.length > 0) {
                data.perguntas.forEach(pergunta => {
                    addMessage('ai', pergunta);
                });
            } else {
                addMessage('ai', data.mensagem);
            }
            elements.chatInputContainer.style.display = 'flex';
            elements.chatInput.focus();
        }
        
    } catch (error) {
        showError(error.message);
        showStep('input');
    } finally {
        elements.loadingQuestions.style.display = 'none';
    }
}

function addMessage(tipo, texto) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message chat-message-${tipo}`;
    
    const icon = tipo === 'ai' ? '🤖' : tipo === 'user' ? '👤' : 'ℹ️';
    const label = tipo === 'ai' ? 'IA' : tipo === 'user' ? 'Você' : 'Sistema';
    
    messageDiv.innerHTML = `
        <div class="chat-message-header">
            <span class="chat-icon">${icon}</span>
            <span class="chat-label">${label}</span>
        </div>
        <div class="chat-message-content">${texto}</div>
    `;
    
    elements.chatMessages.appendChild(messageDiv);
    elements.chatMessages.scrollTop = elements.chatMessages.scrollHeight;
    
    // Adicionar ao estado
    state.conversa.push({ tipo, texto });
}

async function handleSendAnswer() {
    const resposta = elements.chatInput.value.trim();
    
    if (!resposta) {
        showError('Por favor, digite uma resposta.');
        return;
    }
    
    // Adicionar resposta ao chat
    addMessage('user', resposta);
    elements.chatInput.value = '';
    
    // Enviar resposta ao servidor
    try {
        const response = await fetch('/api/submit-answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ resposta })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Erro ao enviar resposta');
        }
        
        // Pedir próxima pergunta
        await askNextQuestion();
        
    } catch (error) {
        showError(error.message);
    }
}

// Funções removidas - não são mais necessárias com o fluxo conversacional

async function handleGenerateModel() {
    // Gerar modelo
    elements.loadingModel.style.display = 'block';
    elements.modelContainer.style.display = 'none';
    elements.questionsButtons.style.display = 'none';
    
    addMessage('system', 'Gerando modelo iStar 2.0...');
    
    try {
        const response = await fetch('/api/generate-model', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Erro ao gerar modelo');
        }
        
        const data = await response.json();
        state.modelo = data.modelo;
        
        // Renderizar modelo
        showStep('model');
        renderModel();
        
    } catch (error) {
        showError(error.message);
    } finally {
        elements.loadingModel.style.display = 'none';
    }
}

function renderModel() {
    // Estatísticas
    const stats = {
        atores: state.modelo.actors?.length || 0,
        nodes: state.modelo.actors?.reduce((sum, a) => sum + (a.nodes?.length || 0), 0) || 0,
        dependencies: state.modelo.dependencies?.length || 0,
        links: state.modelo.links?.length || 0
    };
    
    elements.modelStats.innerHTML = `
        <div class="stat-item">
            <div class="stat-value">${stats.atores}</div>
            <div class="stat-label">Atores</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">${stats.nodes}</div>
            <div class="stat-label">Nodes</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">${stats.dependencies}</div>
            <div class="stat-label">Dependencies</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">${stats.links}</div>
            <div class="stat-label">Links</div>
        </div>
    `;
    
    // JSON formatado
    elements.jsonOutput.textContent = JSON.stringify(state.modelo, null, 2);
    
    elements.modelContainer.style.display = 'block';
    showStep('model');
}

function copyJson() {
    const jsonText = JSON.stringify(state.modelo, null, 2);
    navigator.clipboard.writeText(jsonText).then(() => {
        elements.btnCopyJson.textContent = '✓ Copiado!';
        setTimeout(() => {
            elements.btnCopyJson.textContent = '📋 Copiar';
        }, 2000);
    });
}

function downloadJson() {
    const jsonText = JSON.stringify(state.modelo, null, 2);
    const blob = new Blob([jsonText], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `istar-model-${Date.now()}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function resetSession() {
    state = {
        sessionId: null,
        cenario: null,
        conversa: [],
        modelo: null,
        prontoParaGerar: false
    };
    
    elements.cenarioInput.value = '';
    elements.chatMessages.innerHTML = '';
    elements.chatInput.value = '';
    elements.modelContainer.style.display = 'none';
    elements.questionsButtons.style.display = 'none';
    elements.chatInputContainer.style.display = 'none';
    
    showStep('input');
}

function validateJson() {
    // Validação básica
    const errors = [];
    
    if (!state.modelo.tool || state.modelo.tool !== 'pistar.2.0.0') {
        errors.push('Campo "tool" deve ser "pistar.2.0.0"');
    }
    
    if (!state.modelo.istar || state.modelo.istar !== '2.0') {
        errors.push('Campo "istar" deve ser "2.0"');
    }
    
    if (errors.length === 0) {
        alert('✅ JSON válido! O modelo está pronto para ser usado no iStar.');
    } else {
        alert('⚠️ Problemas encontrados:\n\n' + errors.join('\n'));
    }
}

function loadExample() {
    const exemplo = `Um aplicativo de táxi onde usuários podem solicitar corridas através de um aplicativo móvel. Os usuários podem especificar origem e destino, ver o preço estimado e escolher o tipo de veículo. Motoristas recebem notificações de corridas próximas e podem aceitar ou recusar. O sistema calcula a rota, processa pagamentos e permite que usuários e motoristas se avaliem após a viagem.`;
    
    elements.cenarioInput.value = exemplo;
}

// Função removida - não é mais necessária com o fluxo conversacional




