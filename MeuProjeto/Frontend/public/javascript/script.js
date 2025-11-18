"use strict";
onload = function () {
    document.getElementById('insere').
        addEventListener('click', evento => { location.href = 'insereCarro.html'; });
    document.getElementById('remove')
        .addEventListener('click', apagaCarros);
    exibeListaDeCarros(); // exibe lista de carros ao carregar a página
};
function exibeListaDeCarros() {
    fetch(backendAddress + "carros/lista/")
        .then(response => response.json())
        .then(carros => {
        let campos = ['name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
        let tbody = document.getElementById('idtbody');
        tbody.innerHTML = "";
        for (let carro of carros) {
            let tr = document.createElement('tr');
            for (let i = 0; i < campos.length; i++) {
                let td = document.createElement('td');
                let href = document.createElement('a');
                href.setAttribute('href', 'update.html?id=' + carro['id']);
                let texto = document.createTextNode(carro[campos[i]]);
                href.appendChild(texto);
                td.appendChild(href);
                tr.appendChild(td);
            }
            let checkbox = document.createElement('input');
            checkbox.setAttribute('type', 'checkbox');
            checkbox.setAttribute('name', 'id');
            checkbox.setAttribute('id', 'id');
            checkbox.setAttribute('value', carro['id']);
            let td = document.createElement('td');
            td.appendChild(checkbox);
            tr.appendChild(td);
            tbody.appendChild(tr);
        }
    })
        .catch(error => {
        console.error("Erro:", error);
    });
}
let apagaCarros = (evento) => {
    evento.preventDefault();
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const checkedValues = [];
    checkboxes.forEach(checkbox => { checkedValues.push(checkbox.value); });
    fetch(backendAddress + "carros/lista/", {
        method: 'DELETE',
        body: JSON.stringify(checkedValues),
        headers: { 'Content-Type': 'application/json', }
    })
        .then(response => {
        if (response.ok) {
            alert('Dados removidos com sucesso');
        }
        else {
            alert('Dados removidos com erro');
        }
    })
        .catch(error => { console.log(error); })
        .finally(() => { exibeListaDeCarros(); });
};
