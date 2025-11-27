onload = (evento) => {
    (document.getElementById('enviaNovaSenha') as HTMLButtonElement).
                addEventListener('click', (evento) => {
        evento.preventDefault();
        const token = (document.getElementById('token') as HTMLInputElement).value;
        const senha = (document.getElementById('senha') as HTMLInputElement).value;
        const senha2 = (document.getElementById('senha2') as HTMLInputElement).value;
        const msg = (document.getElementById('msg') as HTMLInputElement);
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
            } else {
                msg.innerHTML = 'Erro ao tentar configurar a senha: ' + response.status + ' '
                    + response.statusText;
            }
        })
        .catch(erro => { console.log(erro) })
    })
}
