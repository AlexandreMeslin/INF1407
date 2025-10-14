onload = () => {
    // Parte 1
	const valor = (document.getElementById('idTexto') 
        ) as HTMLInputElement;
	console.log("texto: ", valor.value);
	console.log("Número:", valor.valueAsNumber);

    // Parte 2
    // const link1 = document.querySelector('a');
    // console.log("link: ", link1.href); // <== errado porque link pode ser null, usar ! como mostrado abaixo
    const link = document.querySelector('a')!; // ! ==> programador garante que não é nulo
    console.log("Endereço: ", link.href);
    console.log("innerHTML: ", link.innerHTML);
    const links = document.querySelectorAll('a'); 
    console.log("links: ", links);

    const outroLink = document.getElementById('idCursos') as HTMLAnchorElement;
    console.log("Endereço: ", outroLink.href);
    console.log("innerHTML: ", outroLink.innerHTML);

    // Parte 3
    (document.getElementById('idCria') as HTMLButtonElement).addEventListener('click', adiciona);
    (document.getElementById('idRemove') as HTMLButtonElement).addEventListener('click', remove);
}
    
function adiciona() {
    var campoInput = document.createElement("input");
    campoInput.setAttribute("type", "button");
    campoInput.setAttribute("value", "botão criado");
    campoInput.setAttribute("id", "idCriado");
    var formulario = document.getElementById("idFormulario") as HTMLFormElement;
    formulario.appendChild(campoInput); 
}

function remove() {
    var campoCriado = document.getElementById("idCriado") as HTMLInputElement;
    campoCriado.remove();
}

{
    function mudaCor(evento: MouseEvent) {
        var objeto: HTMLElement;
        objeto = evento.target as HTMLElement;
        objeto.style.color = "#808080";
    } 
}

{
    function eventoDrop(evento: DragEvent) {
        evento.preventDefault();
        // ? para indicar que o programador garante que não é nulo
        var idBloco = evento.dataTransfer?.getData("bloco") as string;
        (evento.target as HTMLElement).appendChild(document.getElementById(idBloco) as HTMLElement);
    } 

    function eventoDragOver(evento: DragEvent) {
        evento.preventDefault();
    }

    function eventoDragStart(evento: DragEvent) {
        evento.dataTransfer?.setData("bloco", (evento.target as HTMLElement).id);
    }
}