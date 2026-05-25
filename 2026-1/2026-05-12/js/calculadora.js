onload = function() {
    var objBtnNumber;

    for (var i = 0; i < 10; i++) {
        objBtnNumber = document.getElementById("tecla_" + i);
        objBtnNumber.addEventListener("click", listaNumeros);
    }
}

function listaNumeros(evento) {
    var numero = evento.target.innerText;
    console.log("O número " + numero + " foi clicado");
}
