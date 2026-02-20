"use strict";
onload = () => {
    document.getElementById('insere').addEventListener('click', async (evento) => {
        evento.preventDefault();
        const elements = document.getElementById('meuFormulario').elements;
        let data = {};
        // Coleta os dados do formulário
        for (let i = 0; i < elements.length; i++) {
            const element = elements.item(i);
            if (element.name) {
                data[element.name] = element.value;
            }
        }
        try {
            const response = await authFetch(backendAddress + 'carros/criar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            // JEITO ERRADO (Vulnerável):
            // safeArea.innerHTML = userInput; 
            // JEITO CERTO (Seguro):
            // safeArea.textContent = userInput; // O navegador renderiza como texto puro, não como HTML
            if (response.ok) {
                document.getElementById('mensagem').textContent = 'Carro inserido com sucesso!';
            }
            else {
                document.getElementById('mensagem').textContent = 'Erro ao inserir carro.';
            }
        }
        catch (error) {
            console.error('Erro ao enviar dados para o backend:', error);
        }
    });
};
