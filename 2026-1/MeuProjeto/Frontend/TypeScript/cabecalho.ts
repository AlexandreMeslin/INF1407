addEventListener('load', async () => {
    document.getElementById('logout')?.addEventListener('click', logout);
    identifica();
});

/**
 * Função para realizar o logout do usuário.
 * Removendo os tokens do armazenamento local 
 * e redireciona para a home page.
 * @param evento click de mouse
 */
const logout = (evento: MouseEvent) => {
    evento.preventDefault();
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/';
}

/**
 * Função para identificar o usuário autenticado.
 * Exibe o nome do usuário autenticado 
 * ou "visitante" se não houver um usuário autenticado.
 */
const identifica = async () => {
    const spanElement = document.getElementById('identificacao') as HTMLSpanElement;

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('access_token')
    }
    const response = await authFetch(backendAddress + 'accounts/whoami/', {
        method: 'GET',
        headers: headers
    });

    let objDivlogged = (document.getElementById('logged') as HTMLDivElement);
    let objDivunlogged = (document.getElementById('unlogged') as HTMLDivElement);
    if (response.ok) {
        // token enviado no cabeçalho foi aceito pelo servidor
        const data = await response.json();
        objDivlogged.classList.remove('invisivel');
        objDivlogged.classList.add('visivel');
        objDivunlogged.classList.remove('visivel');
        objDivunlogged.classList.add('invisivel');
        spanElement.textContent = data.username ?? 'visitante';
    } else {
        // token enviado no cabeçalho foi rejeitado pelo servidor
        objDivlogged.classList.remove('visivel');
        objDivlogged.classList.add('invisivel');
        objDivunlogged.classList.remove('invisivel');
        objDivunlogged.classList.add('visivel');
        spanElement.textContent = 'visitante';
    }
}