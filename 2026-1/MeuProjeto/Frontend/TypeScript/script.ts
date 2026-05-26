onload = function () {
    exibeListaDeCarros();
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
                objTd.textContent = carro[campo];
                objTr.appendChild(objTd);
            });
            objTBody.appendChild(objTr);
        });
    } catch (error) {
        console.error('Erro ao buscar lista de carros:', error);
    }
}