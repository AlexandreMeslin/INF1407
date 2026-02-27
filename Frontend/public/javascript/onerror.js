"use strict";
function manipuladorDeErros() {
    alert("Aconteceu um erro!");
}
window.onerror = manipuladorDeErros;
// Parte 1
console.log("Início...");
// remover o comentário abaixo para testar
//console.log(erro de sintaxe);
console.log("FIM!");
// Parte 2
console.log("Início...");
// remover o comentário abaixo para testar
//var a: any = b;
console.log("FIM!");
{
    onerror = function (msg, url, linha, coluna) {
        alert("Aconteceu um erro!");
        alert('Mensagem de erro: ' + msg + '\nURL: ' + url + '\nLinha: '
            + linha + '\nColuna: ' + coluna);
    };
    console.log("Início...");
    // remover o comentário abaixo para testar
    //console.log(erro de sintaxe);
    console.log("FIM!");
}
{
    try {
        console.log("Início do bloco try...<br/>");
        // erro
        // remover o comentário abaixo para testar
        //var x = parseInt(a);
    }
    catch (e) { // a variável e deve ser any ou unknown
        console.log("Exceção capturada<br/>");
        console.log("Nome do erro: " + e.name + "<br/>");
        console.log("Mensagem de erro: " + e.message + "<br/>");
        console.log("Pinha no momento do erro: " + e.stack + "<br/>");
    }
    finally {
        console.log("Bloco finally.<br/>");
    }
}
{
    let a = NaN;
    try {
        if (isNaN(a))
            throw new Error("Não é um número");
    }
    catch (e) {
        console.log("Exceção capturada<br/>");
        console.log("Nome do erro: " + e.name + "<br/>");
        console.log("Mensagem de erro: " + e.message + "<br/>");
        console.log("Pinha no momento do erro: " + e.stack + "<br/>");
    }
}
{
    let a = NaN;
    try {
        if (isNaN(a))
            throw {
                name: "Nome da Exceção",
                message: "Não é um número"
            };
    }
    catch (e) {
        console.log("Exceção capturada<br/>");
        console.log("Nome do erro: " + e.name + "<br/>");
        console.log("Mensagem de erro: " + e.message + "<br/>");
        console.log("Número do erro: " + e.number + "<br/>");
        console.log("Descrição do erro: " + e.description + "<br/>");
    }
}
{
    let a = NaN;
    try {
        if (isNaN(a)) {
            throw {
                name: "Nome da Exceção",
                message: "Não é um número"
            };
        }
    }
    catch (e) {
        console.log("Exceção capturada<br/>");
        // Verifica se é um objeto com as propriedades esperadas
        if (typeof e === "object" && e !== null && "name" in e && "message" in e) {
            const err = e;
            console.log("Nome do erro: " + err.name + "<br/>");
            console.log("Mensagem de erro: " + err.message + "<br/>");
            console.log("Número do erro: " + err.number + "<br/>");
            console.log("Descrição do erro: " + err.description + "<br/>");
        }
        else {
            console.log("Erro desconhecido:", e);
        }
    }
}
