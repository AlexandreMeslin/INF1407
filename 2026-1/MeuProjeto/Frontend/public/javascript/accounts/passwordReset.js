"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
addEventListener("DOMContentLoaded", (evento) => {
    const form = document.getElementById("formulario");
    form.addEventListener("submit", (event) => __awaiter(void 0, void 0, void 0, function* () {
        event.preventDefault();
        const messageDiv = document.getElementById("message");
        const email = document.getElementById("email").value;
        try {
            const response = yield fetch(backendAddress + "accounts/password-reset/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email })
            });
            if (response.ok) {
                messageDiv.textContent = "Instruções para resetar a senha foram enviadas para o seu e-mail.";
                messageDiv.style.color = "green";
                setTimeout(() => {
                    location.href = 'passwordResetDone.html';
                }, 3000);
            }
            else {
                const errorData = yield response.json();
                messageDiv.textContent = `Erro: ${errorData.message}`;
            }
        }
        catch (error) {
            messageDiv.textContent = `Erro de rede: ${error}`;
        }
    }));
});
