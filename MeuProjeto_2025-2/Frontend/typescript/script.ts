onload = function () {  

    (document.getElementById('insere') as HTMLButtonElement).
        addEventListener('click', evento => { location.href = 'insereCarro.html' });
  	(document.getElementById('remove') as HTMLButtonElement)
		.addEventListener('click', apagaCarros);


    exibeListaDeCarros();   // exibe lista de carros ao carregar a página
}

function exibeListaDeCarros() {
    fetch(backendAddress + "carros/lista/", {
        method: 'GET',
        headers: {
            'Authorization': tokenKeyword + localStorage.getItem('token')
        }
    })
    .then(response => response.json())
    .then(carros => {
        let campos = ['name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
        let tbody = document.getElementById('idtbody') as HTMLTableSectionElement;
        tbody.innerHTML = ""
        for (let carro of carros) {
            let tr = document.createElement('tr') as HTMLTableRowElement;
            for (let i = 0; i < campos.length; i++) {
                let td = document.createElement('td') as HTMLTableCellElement;
                let href = document.createElement('a') as HTMLAnchorElement;
                href.setAttribute('href', 'update.html?id=' + carro['id']);
                let texto = document.createTextNode(carro[campos[i]]) as Text;
                href.appendChild(texto);
                td.appendChild(href);
                tr.appendChild(td);
            }
			let checkbox = document.createElement('input') as HTMLInputElement;
			checkbox.setAttribute('type', 'checkbox');
			checkbox.setAttribute('name', 'id');
			checkbox.setAttribute('id', 'id');
			checkbox.setAttribute('value', carro['id']);
			let td = document.createElement('td') as HTMLTableCellElement;
			td.appendChild(checkbox);
            tr.appendChild(td);
            tbody.appendChild(tr);
        }
    })
    .catch(error => {
        console.error("Erro:", error);
    });
}

let apagaCarros = (evento: Event) => {
	evento.preventDefault();
    const checkboxes = document.querySelectorAll<HTMLInputElement>('input[type="checkbox"]:checked');
	const checkedValues: string[] = [];
	checkboxes.forEach(checkbox => {  checkedValues.push(checkbox.value); });

    fetch(backendAddress + "carros/lista/", {
			method: 'DELETE',
			body: JSON.stringify(checkedValues),
			headers: { 
                'Content-Type': 'application/json',
                'Authorization': tokenKeyword + localStorage.getItem('token')
            }
	})
	.then(response => {
			if(response.ok) {
				alert('Dados removidos com sucesso');
			} else {
				alert('Dados removidos com erro');
			}
	})
	.catch(error => { console.log(error) })
	.finally(() => { exibeListaDeCarros();})
}
