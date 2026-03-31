onload = () => {
    // Carrega os dados do banco de dados
    // e preenche o formulário
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    const idPlace = document.getElementById('id') as HTMLSpanElement
    if (id) {
        console.log('id = ', id);
        idPlace.innerHTML = id;
        fetch(backendAddress + 'carros/umcarro/' + id + '/', {
            method: 'GET',
            headers: {
                'Authorization': tokenKeyword + localStorage.getItem('token')
            }
        })
        .then(response => response.json())
        .then(carro => {
            let campos = ['id', 'name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
            for (let i = 0; i < campos.length; i++) {
                (document.getElementById(campos[i]) as HTMLInputElement).value = carro[campos[i]];
            }
        })
        .catch(erro => {
            console.log('Deu erro: ' + erro);
        });
    } else {
        idPlace.innerHTML = 'URL mal formada: ' + window.location;
    }

    (document.getElementById('atualiza') as HTMLButtonElement).addEventListener('click', (evento) => {
        evento.preventDefault();
        const form = document.getElementById('meuFormulario') as HTMLFormElement;
        const elements = form.elements;
        let data: Record<string, string> = {};
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i] as HTMLInputElement;
            data[element.name] = element.value;
        }
        fetch(backendAddress + "carros/umcarro/" + id + '/', {
            method: 'PUT',
            body: JSON.stringify(data),
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + localStorage.getItem('token')
            },
        })
        .then(response => {
            if (response.ok) {
                (document.getElementById('mensagem') as HTMLDivElement).innerHTML = 'Sucesso'
            } else {
                (document.getElementById('mensagem') as HTMLDivElement).innerHTML = 'Erro: ' + response.status + " " + response.statusText
            }
        })
        .catch(erro => {
            console.log('Deu erro: ' + erro)
        });
    });
};
