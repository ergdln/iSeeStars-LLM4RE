// Estado da aplicação
let state = {
    sessionId: null,
    cenario: null,
    perguntas: [],
    respostas: {},
    modelo: null
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
    questionsContainer: document.getElementById('questions-container'),
    questionsButtons: document.getElementById('questions-buttons'),
    btnSubmitAnswers: document.getElementById('btn-submit-answers'),
    btnAddMoreQuestions: document.getElementById('btn-add-more-questions'),
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
    elements.btnSubmitAnswers.addEventListener('click', handleGenerateModel);
    elements.btnAddMoreQuestions.addEventListener('click', handleAddMoreQuestions);
    elements.btnCopyJson.addEventListener('click', copyJson);
    elements.btnDownloadJson.addEventListener('click', downloadJson);
    elements.btnNewSession.addEventListener('click', resetSession);
    elements.btnValidateJson.addEventListener('click', validateJson);
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
        
        // Gerar perguntas
        showStep('questions');
        await generateQuestions();
        
    } catch (error) {
        showError(error.message);
        elements.btnStart.disabled = false;
        elements.btnStart.textContent = 'Iniciar Elicitação';
    }
}

async function generateQuestions() {
    elements.loadingQuestions.style.display = 'block';
    elements.questionsContainer.innerHTML = '';
    elements.questionsButtons.style.display = 'none';
    
    try {
        const response = await fetch('/api/generate-questions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Erro ao gerar perguntas');
        }
        
        const data = await response.json();
        state.perguntas = data.perguntas;
        
        // Renderizar perguntas
        renderQuestions();
        
    } catch (error) {
        showError(error.message);
        showStep('input');
    } finally {
        elements.loadingQuestions.style.display = 'none';
    }
}

function renderQuestions() {
    elements.questionsContainer.innerHTML = '';
    
    state.perguntas.forEach((pergunta, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question-item';
        questionDiv.innerHTML = `
            <h3>Pergunta ${index + 1}</h3>
            <div class="question-text">${pergunta}</div>
            <textarea 
                id="answer-${index}" 
                placeholder="Digite sua resposta aqui..."
                data-question-id="${index}"
            ></textarea>
        `;
        
        // Adicionar listener para atualizar estado
        const textarea = questionDiv.querySelector('textarea');
        textarea.addEventListener('input', () => {
            state.respostas[index] = textarea.value.trim();
            updateSubmitButton();
        });
        
        elements.questionsContainer.appendChild(questionDiv);
    });
    
    elements.questionsButtons.style.display = 'flex';
    updateSubmitButton();
}

function updateSubmitButton() {
    const todasRespondidas = state.perguntas.every((_, index) => {
        return state.respostas[index] && state.respostas[index].length > 0;
    });
    
    elements.btnSubmitAnswers.disabled = !todasRespondidas;
}

async function handleGenerateModel() {
    // Enviar respostas
    for (let i = 0; i < state.perguntas.length; i++) {
        if (state.respostas[i]) {
            try {
                await fetch('/api/submit-answer', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        pergunta_id: i,
                        resposta: state.respostas[i]
                    })
                });
            } catch (error) {
                console.error('Erro ao enviar resposta:', error);
            }
        }
    }
    
    // Gerar modelo
    elements.loadingModel.style.display = 'block';
    elements.modelContainer.style.display = 'none';
    
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
        perguntas: [],
        respostas: {},
        modelo: null
    };
    
    elements.cenarioInput.value = '';
    elements.questionsContainer.innerHTML = '';
    elements.modelContainer.style.display = 'none';
    
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

async function handleAddMoreQuestions() {
    // Implementar lógica para gerar mais perguntas
    showError('Funcionalidade em desenvolvimento. Por enquanto, você pode gerar o modelo com as perguntas atuais.');
}

