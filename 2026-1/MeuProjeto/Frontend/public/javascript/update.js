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
onload = () => __awaiter(void 0, void 0, void 0, function* () {
    // Parte 1A: obter os dados do carro via banco de dados no backend
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    const idPlace = document.getElementById('id');
    if (id) {
        idPlace.textContent = id;
        // URL com o parâmetro 'id'
        // busca os dados do carro e preenche os campos do formulário
        try {
            const response = yield fetch(backendAddress + `carros/umcarro/${id}/`);
            if (!response.ok) {
                throw new Error('Erro ao buscar dados do carro');
            }
            const carro = yield response.json();
            // campos são os campos do formulário e do banco de dados
            // eles precisam, por isso, terem o mesmo nome
            let campos = ['id', 'name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
            campos.forEach(campo => {
                const input = document.getElementById(campo);
                if (input) {
                    input.value = carro[campo]; // Preenche o campo do formulário com o valor do carro
                }
            });
        }
        catch (error) {
        }
    }
    else {
        // URL sem o parâmetro 'id', exibe mensagem de erro
        idPlace.textContent = 'ID do carro não fornecido na URL.';
        return; // Encerra a execução da função
    }
    // Parte 1B: configurar o listener do botão de atualização
    const objBotao = document.getElementById('atualiza');
    objBotao.addEventListener('click', atualizaCarro);
});
function atualizaCarro(evento) {
    return __awaiter(this, void 0, void 0, function* () {
        evento.preventDefault(); // Evita o comportamento padrão do botão (submissão do formulário)
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('id');
        // Criar um objeto Record com os dados do formulário
        const dados = {};
        const objFormulario = document.getElementById('meuFormulario');
        const elements = objFormulario.elements;
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i];
            if (element.name) { // Verifica se o elemento tem um atributo 'name'
                dados[element.name] = element.value; // Adiciona o valor ao objeto 'dados' usando o nome do campo como chave
            }
        }
        // Enviar os dados para o backend usando fetch com método PUT
        try {
            const response = yield fetch(backendAddress + `carros/umcarro/${id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dados)
            });
            if (!response.ok) {
                throw new Error('Erro ao atualizar dados do carro');
            }
            // Exibir mensagem de sucesso
            var objMensagem = document.getElementById('mensagem');
            objMensagem.textContent = 'Carro atualizado com sucesso!';
        }
        catch (error) {
            // Exibir mensagem de erro
            var objMensagem = document.getElementById('mensagem');
            objMensagem.textContent = 'Erro ao atualizar dados do carro.';
        }
    });
}
