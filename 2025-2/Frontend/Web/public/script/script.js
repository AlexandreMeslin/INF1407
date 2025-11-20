"use strict";
onload = function () {
    document.getElementById("insere").
        addEventListener("click", evento => { this.location.href = "insereCarro.html"; });
    exibeListaDeCarros();
};
function exibeListaDeCarros() {
    fetch(backendAddress + "carros/lista/", {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_TOKEN'
        }
    })
        .then(response => response.json())
        .then(carros => {
        let campos = ['name', 'mpg', 'cyl',
            'disp', 'hp', 'wt',
            'qsec', 'vs', 'am',
            'gear'];
        let tbody = document.getElementById('idtbody');
        tbody.innerHTML = "";
        for (let carro of carros) {
            let tr = document.createElement('tr');
            for (let i = 0; i < campos.length; i++) {
                let td = document.createElement('td');
                let texto = document.createTextNode(carro[campos[i]]);
                let a = document.createElement('a');
                a.setAttribute('href', 'update.html?id=' + carro['id']);
                a.appendChild(texto);
                td.appendChild(a);
                tr.appendChild(td);
            }
            tbody.appendChild(tr);
        }
    })
        .catch(error => {
        console.error("Erro:", error);
    });
}
