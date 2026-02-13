"use strict";
onload = function () {
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
        const response = await fetch(backendAddress + 'carros/lista/');
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
                td.textContent = carro[campo];
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
    }
    catch (error) {
        console.error('Erro ao buscar a lista de carros:', error);
    }
}
