"use strict";
onload = (evento) => {
    document.getElementById('recuperaSenha').addEventListener('click', (evento) => {
        evento.preventDefault();
        fetch(backendAddress + 'accounts/password_reset/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify({ 'email': document.getElementById('email').value, })
        })
            .then(response => {
            if (response.ok) {
                console.log('Solicitação de redefinição de senha enviada com sucesso.');
                window.location.assign('passwordResetDone.html');
            }
            else {
                document.getElementById('msg').innerHTML = 'Erro: ' + response.status + ' ' + response.statusText;
            }
        })
            .catch(erro => { console.log(erro); });
    });
};
