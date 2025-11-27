"use strict";
onload = (evento) => {
    document.getElementById('recuperaSenha').addEventListener('click', (evento) => {
        evento.preventDefault();
        console.log('enviando para', backendAddress + 'accounts/password-reset/');
        fetch(backendAddress + 'accounts/password-reset/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify({ 'email': document.getElementById('email').value, })
        })
            .then(response => {
            if (response.ok) {
                window.location.assign('passwordResetDone.html');
            }
            else {
                document.getElementById('msg').innerHTML = 'Erro: ' + response.status + ' '
                    + response.statusText;
            }
        })
            .catch(erro => { console.log(erro); });
    });
};
