onload = (evento) => {
    (document.getElementById('recuperaSenha') as HTMLButtonElement).addEventListener('click', (evento) => {
        evento.preventDefault();
        console.log('enviando para', backendAddress + 'accounts/password-reset/');
        fetch(backendAddress + 'accounts/password-reset/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify({ 'email': (document.getElementById('email') as HTMLInputElement).value, })
        })
        .then(response => {
            if (response.ok) {
                window.location.assign('passwordResetDone.html');
            } else {
                (document.getElementById('msg') as HTMLDivElement).innerHTML = 'Erro: ' + response.status + ' '
                    + response.statusText;
            }
        })
        .catch(erro => { console.log(erro) });
    });
}