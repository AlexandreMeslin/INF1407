"use strict";
onload = (evento) => {
    document.getElementById('enviaNovaSenha').
        addEventListener('click', (evento) => {
        evento.preventDefault();
        const token = document.getElementById('token').value;
        const senha = document.getElementById('senha').value;
        const senha2 = document.getElementById('senha2').value;
        const msg = document.getElementById('msg');
        // verifica se as duas senhas são iguais
        if (senha != senha2) {
            msg.innerHTML = 'As senhas devem ser iguais';
            return;
        }
        // prepara o formulário via script
        const formData = new FormData();
        formData.append('token', token);
        formData.append('password', senha);
        fetch(backendAddress + 'accounts/password_reset/confirm/', {
            method: 'POST',
            body: formData,
        })
            .then(response => {
            if (response.ok) {
                window.location.href = 'passwordResetFinish.html';
            }
            else {
                msg.innerHTML = 'Erro ao tentar configurar a senha: ' + response.status + ' '
                    + response.statusText;
            }
        })
            .catch(erro => { console.log(erro); });
    });
};
