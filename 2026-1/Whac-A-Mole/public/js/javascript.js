"use strict";
onload = () => {
    for (let i = 0; i < 5; i++) {
        const buraco = document.getElementById(`buraco${i}`);
        if (buraco) {
            buraco.addEventListener('click', martelada);
        }
    }
};
/**
 * Função chamada quando o usuário clicar em um buraco
 *
 * @param evento O evento de clique do mouse
 * @return void
 */
function martelada(evento) {
    // TODO: implementar a lógica do jogo aqui
    var objBuraco = evento.target;
    console.log('Martelada no ' + objBuraco.id + '!');
}
