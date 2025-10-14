"use strict";
onload = () => {
    document.getElementById('idInnerHTML').addEventListener('click', htmlDeDentro);
    document.getElementById('idAppendChild').addEventListener('click', acrescentaFilho);
};
var qtd = 256;
function htmlDeDentro() {
    var inicio = new Date().getTime();
    var idDiv;
    for (var i = 0; i < qtd; i++)
        document.getElementById("idDiv").innerHTML += "<input type=text>";
    alert((new Date().getTime() - inicio) + " ms");
    while ((idDiv = document.getElementById("idDiv")).firstChild)
        idDiv.removeChild(idDiv.firstChild);
}
function acrescentaFilho() {
    var inicio = new Date().getTime();
    var idDiv;
    for (var i = 0; i < qtd; i++) {
        var campo = document.createElement("input");
        campo.setAttribute("type", "text");
        document.getElementById("idDiv").appendChild(campo);
    }
    alert((new Date().getTime() - inicio) + " ms");
    while ((idDiv = document.getElementById("idDiv")).firstChild)
        idDiv.removeChild(idDiv.firstChild);
}
