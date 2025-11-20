"use strict";
onload = () => {
    document.getElementById('insere').
        addEventListener('click', evento => {
        evento.preventDefault();
        // TODO: colocar mensagem "Em andamento..." em azul
        const elements = document.getElementById('formulario')
            .elements;
        let data = {}; // Objeto para armazenar os dados do formulário
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i];
            data[element.name] = element.value; // Adiciona um campo do formulário no objeto data
        }
        // enviar os dados para o backend
        fetch(backendAddress + 'carros/umcarro/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data) // Converte o objeto data para JSON
        })
            .then(response => {
            if (response.ok) {
                // TODO: mudar a mensagem para verde
                document.getElementById('mensagem').innerText =
                    'Carro inserido com sucesso!';
            }
            else {
                // TODO: mudar a mensagem para vermelho
                document.getElementById('mensagem').innerText =
                    'Erro ao inserir o carro.';
            }
        });
    });
};
