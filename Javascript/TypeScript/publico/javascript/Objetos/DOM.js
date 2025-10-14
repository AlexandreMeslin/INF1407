"use strict";
onload = () => {
    // Parte 1
    const valor = (document.getElementById('idTexto'));
    console.log("texto: ", valor.value);
    console.log("Número:", valor.valueAsNumber);
    // Parte 2
    // const link1 = document.querySelector('a');
    // console.log("link: ", link1.href); // <== errado porque link pode ser null, usar ! como mostrado abaixo
    const link = document.querySelector('a'); // ! ==> programador garante que não é nulo
    console.log("Endereço: ", link.href);
    console.log("innerHTML: ", link.innerHTML);
    const links = document.querySelectorAll('a');
    console.log("links: ", links);
    const outroLink = document.getElementById('idCursos');
    console.log("Endereço: ", outroLink.href);
    console.log("innerHTML: ", outroLink.innerHTML);
    // Parte 3
    document.getElementById('idCria').addEventListener('click', adiciona);
    document.getElementById('idRemove').addEventListener('click', remove);
};
function adiciona() {
    var campoInput = document.createElement("input");
    campoInput.setAttribute("type", "button");
    campoInput.setAttribute("value", "botão criado");
    campoInput.setAttribute("id", "idCriado");
    var formulario = document.getElementById("idFormulario");
    formulario.appendChild(campoInput);
}
function remove() {
    var campoCriado = document.getElementById("idCriado");
    campoCriado.remove();
}
{
    function mudaCor(evento) {
        var objeto;
        objeto = evento.target;
        objeto.style.color = "#808080";
    }
}
{
    function eventoDrop(evento) {
        var _a;
        evento.preventDefault();
        // ? para indicar que o programador garante que não é nulo
        var idBloco = (_a = evento.dataTransfer) === null || _a === void 0 ? void 0 : _a.getData("bloco");
        evento.target.appendChild(document.getElementById(idBloco));
    }
    function eventoDragOver(evento) {
        evento.preventDefault();
    }
    function eventoDragStart(evento) {
        var _a;
        (_a = evento.dataTransfer) === null || _a === void 0 ? void 0 : _a.setData("bloco", evento.target.id);
    }
}
