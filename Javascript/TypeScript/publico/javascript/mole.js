"use strict";
let ponto = 0;
onload = function () {
    setInterval(sobeToupeira, 5 * 1000);
    for (var i = 0; i < 5; i++)
        document.getElementById('buraco' + i).addEventListener('click', martelada);
    document.getElementById('idMesa').addEventListener('mousedown', marteloBaixo);
    document.getElementById('idMesa').addEventListener('mouseup', marteloCima);
};
function sobeToupeira() {
    var buraco = Math.floor(Math.random() * 5);
    var objBuraco = document.getElementById('buraco' + buraco);
    objBuraco.src = 'imagens/scene_top.png';
    setTimeout(tiraToupeira, 2 * 1000, buraco);
}
function tiraToupeira(buraco) {
    var objBuraco = document.getElementById('buraco' + buraco);
    objBuraco.src = 'imagens/scene2.png';
}
function martelada(evento) {
    if (evento.target.src.includes('scene_top')) {
        // acertou 
        ponto++;
        evento.target.src = 'imagens/scene2.png';
    }
    else {
        // errou
        ponto--;
    }
    document.getElementById('idPontos').innerHTML = ponto.toString();
}
function marteloBaixo() {
    document.getElementById('idMesa').style.cursor = 'url(imagens/hammerDown.png), default';
}
function marteloCima() {
    document.getElementById('idMesa').style.cursor = 'url(imagens/hammer.png), default';
}
