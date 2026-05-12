console.log("Alô mundo JavaScript");

onload = function() {
    var contador = 0;
    contMouseOver = 0;

    console.log("A página foi carregada");
    var objTitulo = document.getElementById("titulo");
    var objImagem = document.getElementById("imagem");

    objImagem.addEventListener("mouseover", sobreImagem);
    objImagem.addEventListener("click", function() {
        contador++;
        console.log("A imagem foi clicada " + contador + " vez(es)");
    });

    objTitulo.addEventListener("click", function() {
        console.log("O título foi clicado");
    });
}

function sobreImagem() {
    contMouseOver++;
    console.log("O mouse está sobre a imagem " + contMouseOver + " vez(es)");
}
