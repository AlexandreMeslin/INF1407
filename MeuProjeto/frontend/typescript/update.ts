onload = async () => {
    // Parte 1: carregar dados do carro a ser editado e preencher o formulário
    // Carrega os dados do carro a ser editado do banco de dados
    // Preenche o formulário com os dados do carro
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    const idPlace = document.getElementById('id') as HTMLInputElement;
    if (id) {
        idPlace.value = id;
        try {
            const response = await fetch(backendAddress + 'carros/umcarro/' + id + '/');
            if (response.ok) {
                const carro = await response.json();
                let campos = ['id', 'name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
                campos.forEach(campo => {
                    (document.getElementById(campo) as HTMLInputElement).value = carro[campo];
                });
            } else {
                console.error('Erro ao buscar dados do carro:', response.status);
            }
        } catch (error) {
            console.error('Erro ao buscar dados do carro:', error);
        }
    } else {
        idPlace.value = 'URL mal formada: ' + window.location;
    }

    // Parte 2: configurar o evento de clique do botão "Atualizar"
    (document.getElementById('atualiza') as HTMLButtonElement).addEventListener('click', async evento => {
        evento.preventDefault();
        const form = document.getElementById('meuFormulario') as HTMLFormElement;
        const elements = form.elements;
        let data: Record<string, string> = {};

        // Coleta os dados do formulário
        for (let i = 0; i < elements.length; i++) {
            const element = elements.item(i) as HTMLInputElement;
            if (element.name) {
                data[element.name] = element.value;
            }
        }

        try {
            const response = await fetch(backendAddress + 'carros/umcarro/' + id + '/', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if(response.ok) {
                (document.getElementById('mensagem') as HTMLDivElement).textContent = 'Carro atualizado com sucesso!';
            } else {
                (document.getElementById('mensagem') as HTMLDivElement).textContent = 'Erro ao atualizar carro.';
            }
        } catch (error) {
            console.error('Erro ao enviar dados para o backend:', error);
        }
    });
}
