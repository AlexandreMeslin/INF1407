onload = inicializa;

function inicializa() {
    console.log("Estamos na inicializa");
    var objH1 = document.getElementById('id_titulo');
    objH1.addEventListener("mouseover", mouseNoH1);

    // contador tem que ser variável global
    // não pode ser declarada com var ou let
    contador = 0;   // representa o estado do objeto h1
}

/**
 * Trata o evento no título
 * 
 * @param {*} evento objeto referente ao evento que aconteceu
 */
function mouseNoH1(evento) {
    contador += 1;
    console.log("Mouse", contador, "vez(es) em cima do título");
}