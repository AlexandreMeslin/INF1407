"use strict";
onload = () => {
    console.log("Página carregada!");
    var objParagrafo = document.getElementById("paragrafo");
    if (objParagrafo) {
        objParagrafo.onclick = () => {
            var objMsg = document.getElementById("msg");
            objMsg.innerHTML = "Você clicou no parágrafo!"; // NÃO use innerHTML!!!
        };
    }
};
