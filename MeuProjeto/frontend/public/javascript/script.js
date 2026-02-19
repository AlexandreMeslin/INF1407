"use strict";
onload = function () {
    document.getElementById('insere').addEventListener('click', evento => {
        this.location.href = 'insereCarro.html';
    });
    document.getElementById('remove').addEventListener('click', apagaCarros);
    exibeListaDeCarros(); // Exibe a lista de carros ao carregar a página
};
/**
 * Busca a lista de carros do backend e exibe na tabela HTML.
 * Esta função é assíncrona porque envolve uma chamada de rede (fetch).
 * Ela usa async/await para lidar com a promessa retornada pelo fetch.
 * Se a resposta da API não for ok, ela lança um erro que é capturado no bloco catch.
 * Em caso de erro, ele é logado no console.
 * Se a resposta for bem-sucedida, ela processa os dados JSON e os exibe na tabela HTML.
 * A função assume que a resposta da API é uma lista de objetos, onde cada objeto representa um carro com os campos especificados.
 * A função também limpa o conteúdo do tbody antes de adicionar novos dados, para evitar duplicação.
 * Nota: Em um ambiente de produção, você deve lidar com erros de forma mais robusta, talvez exibindo uma mensagem de erro para o usuário em vez de apenas logar no console.
 */
async function exibeListaDeCarros() {
    try {
        const response = await authFetch(backendAddress + 'carros/varioscarros/');
        if (!response.ok) {
            // Nota: Em um ambiente de produção, você deve lidar com erros de forma mais robusta,
            // talvez exibindo uma mensagem de erro para o usuário em vez de apenas logar no console.
            throw new Error('Erro na resposta da API: ' + response.status);
        }
        const carros = await response.json();
        let campos = ['name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
        let tbody = document.getElementById('idtbody');
        tbody.innerHTML = ''; // Limpa o conteúdo do tbody antes de adicionar novos dados
        carros.forEach((carro) => {
            let tr = document.createElement('tr');
            campos.forEach(campo => {
                let td = document.createElement('td');
                let href = document.createElement('a');
                href.href = 'update.html?id=' + carro['id'];
                href.textContent = carro[campo];
                td.appendChild(href);
                tr.appendChild(td);
            });
            let checkbox = document.createElement('input');
            checkbox.setAttribute('type', 'checkbox');
            checkbox.setAttribute('name', 'id');
            checkbox.setAttribute('id', 'id');
            checkbox.setAttribute('value', carro['id']);
            let td = document.createElement('td');
            td.appendChild(checkbox);
            tr.appendChild(td);
            tbody.appendChild(tr);
        });
    }
    catch (error) {
        console.error('Erro ao buscar a lista de carros:', error);
    }
}
/**
 * Função para apagar carros selecionados.
 * Esta função é assíncrona porque envolve uma chamada de rede (fetch).
 * Ela coleta os IDs dos carros selecionados usando checkboxes,
 * envia uma requisição DELETE para o backend e atualiza a lista de carros após a exclusão.
 * Se a resposta da API não for ok, ela lança um erro que é capturado no bloco catch.
 * Em caso de erro, ele é logado no console.
 * Se a resposta for bem-sucedida, ela exibe uma mensagem de sucesso e atualiza a lista de carros.
 * Nota: Em um ambiente de produção, você deve lidar com erros de forma mais robusta,
 * talvez exibindo uma mensagem de erro para o usuário em vez de apenas logar no console.
 *
 * @param evento
 */
let apagaCarros = async (evento) => {
    evento.preventDefault();
    const checkboxes = document.querySelectorAll('input[name="id"]:checked');
    const checkedValues = [];
    checkboxes.forEach(checkbox => {
        checkedValues.push(checkbox.value);
    });
    try {
        const response = await authFetch(backendAddress + 'carros/varioscarros/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(checkedValues)
        });
        if (response.ok) {
            alert('Carros excluídos com sucesso!');
        }
        else {
            alert('Erro ao excluir carros!');
        }
    }
    catch (error) {
        // Nota: Em um ambiente de produção, você deve lidar com erros de forma mais robusta
        console.error('Erro ao enviar dados para o backend:', error);
    }
    finally {
        exibeListaDeCarros(); // Atualiza a lista de carros após a exclusão
    }
};
