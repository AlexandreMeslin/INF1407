onload = function () {
    exibeListaDeCarros();
    var objBtnRemover = document.getElementById('remove') as HTMLAnchorElement;
    objBtnRemover.addEventListener('click', apagaCarros);
}

async function apagaCarros(evento: MouseEvent) {
    evento.preventDefault();
    const checkboxes = document.querySelectorAll('input[name="id"]:checked') as NodeListOf<HTMLInputElement>;
    const checkedValues: string[] = [];
    checkboxes.forEach((checkbox) => {
        checkedValues.push(checkbox.value);
    });
    try {
        console.log('IDs dos carros a serem removidos:', checkedValues);
        const response = await fetch(backendAddress + 'carros/varioscarros/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            // NÃO enviar o nome do campo, apenas a lista dos IDs
            body: JSON.stringify(checkedValues)
        });
        if (!response.ok) {
            throw new Error('Erro ao remover carros');
        }
        alert('Carros removidos com sucesso!');
    } catch (error) {
        console.error('Erro ao remover carros:', error);
        alert('Erro ao remover carros. Por favor, tente novamente.');
    } finally {
        // com ou sem erro, a lista de carros tem que ser atualizadas
        exibeListaDeCarros();
    }
}

async function exibeListaDeCarros() {
    try {
        const response = await fetch(backendAddress + 'carros/varioscarros/');
        if(!response.ok) {
            throw new Error('Erro ao buscar lista de carros');
        }
        const carros = await response.json();
        let campos = ['name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
        let objTBody = document.getElementById('tbody') as HTMLTableSectionElement;
        objTBody.innerHTML = '';
        carros.forEach((carro: any) => {
            let objTr = document.createElement('tr');
            campos.forEach(campo => {
                let objTd = document.createElement('td');
                //objTd.textContent = carro[campo];
                let objHref = document.createElement('a') as HTMLAnchorElement;
                objHref.setAttribute('href', `update.html?id=${carro.id}`);
                objHref.textContent = carro[campo];
                objTd.appendChild(objHref);
                objTr.appendChild(objTd);
            });
            var objCheckbox = document.createElement('input') as HTMLInputElement;
            objCheckbox.setAttribute('type', 'checkbox');
            objCheckbox.setAttribute('value', carro.id);
            objCheckbox.setAttribute('id', 'id');
            objCheckbox.setAttribute('name', 'id');
            var objTd = document.createElement('td');
            objTd.appendChild(objCheckbox);
            objTr.appendChild(objTd);
            objTBody.appendChild(objTr);
        });
    } catch (error) {
        console.error('Erro ao buscar lista de carros:', error);
    }
}