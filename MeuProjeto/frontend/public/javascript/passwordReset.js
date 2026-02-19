"use strict";
addEventListener("DOMContentLoaded", (evento) => {
    const form = document.getElementById("formulario");
    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const messageDiv = document.getElementById("message");
        const email = document.getElementById("email").value;
        try {
            const response = await fetch(backendAddress + "accounts/password-reset/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email })
            });
            if (response.ok) {
                messageDiv.textContent = "Instruções para resetar a senha foram enviadas para o seu e-mail.";
            }
            else {
                const errorData = await response.json();
                messageDiv.textContent = `Erro: ${errorData.message}`;
            }
        }
        catch (error) {
            messageDiv.textContent = `Erro de rede: ${error}`;
        }
    });
});
