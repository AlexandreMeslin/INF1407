"use strict";
onload = () => {
    document.getElementById('insere').addEventListener('click', async (evento) => {
        console.log('Enviando dados do formulário para o backend...');
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
            const response = await fetch(backendAddress + 'carros/criar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
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
