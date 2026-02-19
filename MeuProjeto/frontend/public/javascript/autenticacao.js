"use strict";
addEventListener('load', async () => {
    var _a;
    // prepara os elementos HTML que serão manipulados via evento
    (_a = document.getElementById('logout')) === null || _a === void 0 ? void 0 : _a.addEventListener('click', (evento) => {
        evento.preventDefault();
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/';
    });
    // ao carregar a página, verificamos se o token armazenado no localStorage é válido
    const spanElement = document.getElementById('identificacao');
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('access_token')
    };
    console.log(headers);
    const response = await fetch(backendAddress + '/accounts/whoiam/', {
        method: 'GET',
        headers: headers
    });
    if (response.ok) {
        const data = await response.json();
        // token enviado no cabeçalho foi aceito pelo servidor
        let objDiv = document.getElementById('logged');
        objDiv.classList.remove('invisivel');
        objDiv.classList.add('visivel');
        objDiv = document.getElementById('unlogged');
        objDiv.classList.remove('visivel');
        objDiv.classList.add('invisivel');
        if (data.username === null) {
            spanElement.innerHTML = 'visitante';
        }
        else {
            spanElement.innerHTML = data.username;
        }
    }
    else {
        // token enviado no cabeçalho foi rejeitado pelo servidor
        let objDiv = document.getElementById('logged');
        objDiv.classList.remove('visivel');
        objDiv.classList.add('invisivel');
        objDiv = document.getElementById('unlogged');
        objDiv.classList.remove('invisivel');
        objDiv.classList.add('visivel');
        spanElement.innerHTML = 'visitante';
    }
});
