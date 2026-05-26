onload = () => {
    const objBotao = document.getElementById('insere') as HTMLButtonElement;
    objBotao.addEventListener('click', async (evento) => {
        evento.preventDefault();    // Evita o comportamento padrão do botão (submissão do formulário)
        let data: Record<string, string> = {};  // Objeto para armazenar os dados do formulário
        const elements =
            (document.getElementById('meuFormulario') as HTMLFormElement).elements;
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i] as HTMLInputElement;
            if (element.name) {  // Verifica se o elemento tem um atributo 'name'
                data[element.name] = element.value;  // Adiciona o valor ao objeto 'data' usando o nome do campo como chave
            }
        }
        try {
            const response = await fetch(backendAddress + 'carros/criar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)  // Converte o objeto 'data' para uma string JSON
            });
            if (response.ok) {
                (document.getElementById('mensagem') as HTMLDivElement)
                    .textContent = 'Carro inserido com sucesso!';
            } else {
                (document.getElementById('mensagem') as HTMLDivElement)
                    .textContent = 'Erro ao inserir carro.';
            }
        } catch (error) {
            console.error('Erro ao inserir carro:', error);
        }
    });
}