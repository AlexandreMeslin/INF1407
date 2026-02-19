addEventListener('load', async () => {
    // esse evento possui 2 partes
    // - a primeira parte é a configuração do evento de clique no botão de logout, que remove os tokens do localStorage e redireciona para a página inicial
    // - a segunda parte é a verificação do token armazenado no localStorage, que é feita ao carregar a página. Se o token for válido, o nome do usuário é exibido e os links de login e logout são alternados. Se o token for inválido, o nome do usuário é definido como "visitante" e os links de login e logout são alternados.

    // prepara os elementos HTML que serão manipulados via evento
    document.getElementById('logout')?.addEventListener('click', (evento) => {
        evento.preventDefault();
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/';
    });

    // ao carregar a página, verificamos se o token armazenado no localStorage é válido
    const spanElement = document.getElementById('identificacao') as HTMLSpanElement;
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('access_token')
    }
    const response = await authFetch(backendAddress + 'accounts/whoiam/', {
        method: 'GET',
        headers: headers
    });
    if (response.ok) {
        const data = await response.json();
        // token enviado no cabeçalho foi aceito pelo servidor
        let objDiv = (document.getElementById('logged') as HTMLDivElement);
        objDiv.classList.remove('invisivel');
        objDiv.classList.add('visivel');
        objDiv = (document.getElementById('unlogged') as HTMLDivElement);
        objDiv.classList.remove('visivel');
        objDiv.classList.add('invisivel');
        if(data.username === null) {
            spanElement.innerHTML = 'visitante';
        } else {
            spanElement.innerHTML = data.username;
        }
    } else {
        // token enviado no cabeçalho foi rejeitado pelo servidor
        let objDiv = (document.getElementById('logged') as HTMLDivElement);
        objDiv.classList.remove('visivel');
        objDiv.classList.add('invisivel');
        objDiv = (document.getElementById('unlogged') as HTMLDivElement);
        objDiv.classList.remove('invisivel');
        objDiv.classList.add('visivel');
        spanElement.innerHTML = 'visitante';
    }
});
