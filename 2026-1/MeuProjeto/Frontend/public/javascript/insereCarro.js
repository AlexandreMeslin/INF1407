"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
onload = () => {
    const objBotao = document.getElementById('insere');
    objBotao.addEventListener('click', (evento) => __awaiter(void 0, void 0, void 0, function* () {
        evento.preventDefault(); // Evita o comportamento padrão do botão (submissão do formulário)
        let data = {}; // Objeto para armazenar os dados do formulário
        const elements = document.getElementById('meuFormulario').elements;
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i];
            if (element.name) { // Verifica se o elemento tem um atributo 'name'
                data[element.name] = element.value; // Adiciona o valor ao objeto 'data' usando o nome do campo como chave
            }
        }
        try {
            const response = yield fetch(backendAddress + 'carros/varioscarros/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data) // Converte o objeto 'data' para uma string JSON
            });
            if (response.ok) {
                document.getElementById('mensagem')
                    .textContent = 'Carro inserido com sucesso!';
            }
            else {
                document.getElementById('mensagem')
                    .textContent = 'Erro ao inserir carro.';
            }
        }
        catch (error) {
            console.error('Erro ao inserir carro:', error);
        }
    }));
};
