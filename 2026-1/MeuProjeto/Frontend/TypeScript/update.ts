onload = async () => {
    // Parte 1A: obter os dados do carro via banco de dados no backend
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    const idPlace = document.getElementById('id') as HTMLSpanElement;
    if (id) {
       idPlace.textContent = id;
        // URL com o parâmetro 'id'
        // busca os dados do carro e preenche os campos do formulário
        try {
            const response = await fetch(backendAddress + `carros/umcarro/${id}/`);
            if (!response.ok) {
                throw new Error('Erro ao buscar dados do carro');
            }
            const carro = await response.json();
            // campos são os campos do formulário e do banco de dados
            // eles precisam, por isso, terem o mesmo nome
            let campos = ['id', 'name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
            campos.forEach(campo => {
                const input = document.getElementById(campo) as HTMLInputElement;
                if (input) {
                    input.value = carro[campo]; // Preenche o campo do formulário com o valor do carro
                }
            });
        } catch (error) {
        }
    } else {
        // URL sem o parâmetro 'id', exibe mensagem de erro
        idPlace.textContent = 'ID do carro não fornecido na URL.';
        return; // Encerra a execução da função
    }
    // Parte 1B: configurar o listener do botão de atualização
    const objBotao = document.getElementById('atualiza') as HTMLButtonElement;
    objBotao.addEventListener('click', atualizaCarro);
}

async function atualizaCarro(evento: MouseEvent) {
    evento.preventDefault();    // Evita o comportamento padrão do botão (submissão do formulário)
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');

    // Criar um objeto Record com os dados do formulário
    const dados = {} as Record<string, string>;
    const objFormulario = document.getElementById('meuFormulario') as HTMLFormElement;
    const elements = objFormulario.elements;
    for(let i=0; i<elements.length; i++) {
        const element = elements[i] as HTMLInputElement;
        if (element.name) {  // Verifica se o elemento tem um atributo 'name'
            dados[element.name] = element.value;  // Adiciona o valor ao objeto 'dados' usando o nome do campo como chave
        }
    }

    // Enviar os dados para o backend usando fetch com método PUT
    try {
        const response = await fetch(backendAddress + `carros/umcarro/${id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        });
        if (!response.ok) {
            throw new Error('Erro ao atualizar dados do carro');
        }
        // Exibir mensagem de sucesso
        var objMensagem = document.getElementById('mensagem') as HTMLDivElement;
        objMensagem.textContent = 'Carro atualizado com sucesso!';
    } catch (error) {
        // Exibir mensagem de erro
        var objMensagem = document.getElementById('mensagem') as HTMLDivElement;
        objMensagem.textContent = 'Erro ao atualizar dados do carro.';
    }
}