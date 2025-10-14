"use strict";
{
    var texto = "Este texto será dinamicamente incluído na página.";
    function incluiTexto(lugar) {
        var node;
        node = document.createElement("p");
        let novoTexto;
        novoTexto = document.createTextNode("Um texto.");
        node.appendChild(novoTexto);
        let elemento;
        elemento = document.getElementById(lugar);
        elemento.appendChild(node);
    }
    function removeTexto(lugar) {
        var elemento;
        elemento = document.getElementById(lugar);
        if (elemento != null && elemento.lastChild != null)
            elemento.removeChild(elemento.lastChild);
    }
}
onload = () => {
    document.getElementById('link').addEventListener('click', () => incluiTexto('lugar'));
    document.getElementById('button').addEventListener('click', () => removeTexto('lugar'));
    // Variável global definida dentro da função
    window.texto = "Este texto será dinamicamente incluído na página.";
};
function incluiTexto(lugar) {
    var node;
    node = document.createElement("p");
    let novoTexto;
    novoTexto = document.createTextNode(texto);
    node.appendChild(novoTexto);
    let elemento;
    elemento = document.getElementById(lugar);
    elemento.appendChild(node);
}
function removeTexto(lugar) {
    var elemento;
    elemento = document.getElementById(lugar);
    if (elemento != null && elemento.lastChild != null)
        elemento.removeChild(elemento.lastChild);
}
