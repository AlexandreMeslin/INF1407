{
    var texto = "Este texto será dinamicamente incluído na página.";

    function incluiTexto(lugar: string) {
        var node: HTMLParagraphElement;
        node = document.createElement("p");
        let novoTexto: Text;
        novoTexto = document.createTextNode("Um texto.");
        node.appendChild(novoTexto);
        let elemento: HTMLDivElement;
        elemento = document.getElementById(lugar) as HTMLDivElement;
        elemento.appendChild(node);
    }

    function removeTexto(lugar: string) {
        var elemento: HTMLElement;
        elemento = document.getElementById(lugar) as HTMLElement;
        if(elemento != null && elemento.lastChild != null) 
            elemento.removeChild(elemento.lastChild);
    }
}

onload = () => {
    (document.getElementById('link') as HTMLLinkElement).addEventListener('click', () => incluiTexto('lugar'));
    (document.getElementById('button') as HTMLButtonElement).addEventListener('click', () => removeTexto('lugar'));
    // Variável global definida dentro da função
    window.texto = "Este texto será dinamicamente incluído na página.";
}

function incluiTexto(lugar: string) {
    var node: HTMLParagraphElement;
    node = document.createElement("p");
    let novoTexto: Text;
    novoTexto = document.createTextNode(texto);
    node.appendChild(novoTexto);
    let elemento: HTMLDivElement;
    elemento = document.getElementById(lugar) as HTMLDivElement;
    elemento.appendChild(node);
}

function removeTexto(lugar: string) {
    var elemento: HTMLElement;
    elemento = document.getElementById(lugar) as HTMLElement;
    if(elemento != null && elemento.lastChild != null) 
        elemento.removeChild(elemento.lastChild);
}
