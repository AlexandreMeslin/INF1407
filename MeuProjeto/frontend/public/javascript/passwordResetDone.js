"use strict";
addEventListener("load", function () {
    document.getElementById("enviaNovaSenha").addEventListener("click", async function (evento) {
        evento.preventDefault();
        const token = document.getElementById("token").value;
        const senha = document.getElementById("novaSenha").value;
        const senha2 = document.getElementById("confirmarSenha").value;
        const message = document.getElementById("message");
        if (senha !== senha2) {
            message.textContent = "As senhas não coincidem.";
            message.style.color = "red";
            return;
        }
        let response = await fetch(backendAddress + 'password-reset/', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                token: token,
                password: senha
            })
        });
        if (response.ok) {
            message.textContent = "Senha alterada com sucesso! Redirecionando para a página de login...";
            message.style.color = "green";
            setTimeout(() => {
                location.href = "login.html";
            }, 3000);
        }
        else {
            const data = await response.json();
            message.textContent = data.detail || "Ocorreu um erro ao alterar a senha.";
            message.style.color = "red";
        }
    });
});
