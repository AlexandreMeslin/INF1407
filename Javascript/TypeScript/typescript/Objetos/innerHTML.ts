    onload = () => {
    (document.getElementById('idInnerHTML') as HTMLButtonElement).addEventListener('click', htmlDeDentro);
    (document.getElementById('idAppendChild') as HTMLButtonElement).addEventListener('click', acrescentaFilho); 
}

var qtd = 256;

function htmlDeDentro() {
    var inicio = new Date().getTime();
    var idDiv;
    for(var i=0; i<qtd; i++)
        (document.getElementById("idDiv") as HTMLDivElement).innerHTML += "<input type=text>"; 
    alert ((new Date().getTime() - inicio) + " ms");
    while((idDiv = document.getElementById("idDiv") as HTMLDivElement).firstChild) idDiv.removeChild(idDiv.firstChild);
}

function acrescentaFilho() {
    var inicio = new Date().getTime();
    var idDiv;
    for(var i=0; i<qtd; i++) {
        var campo = document.createElement("input");
        campo.setAttribute("type", "text");
        (document.getElementById("idDiv") as HTMLDivElement).appendChild(campo);
    }
    alert ((new Date().getTime() - inicio) + " ms");
    while((idDiv = document.getElementById("idDiv") as HTMLDivElement).firstChild) idDiv.removeChild(idDiv.firstChild);
}
