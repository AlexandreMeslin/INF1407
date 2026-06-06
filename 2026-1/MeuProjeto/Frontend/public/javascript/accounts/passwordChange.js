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
addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("formulario");
    form.addEventListener("submit", (event) => __awaiter(void 0, void 0, void 0, function* () {
        event.preventDefault();
        const messageDiv = document.getElementById("message");
        const currentPassword = document.getElementById("old_password").value;
        const newPassword = document.getElementById("new_password").value;
        const confirmPassword = document.getElementById("confirm_password").value;
        if (newPassword !== confirmPassword) {
            messageDiv.textContent = "A nova senha e a confirmação não coincidem.";
            return;
        }
        try {
            const response = yield authFetch(backendAddress + "accounts/change-password/", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    old_password: currentPassword,
                    new_password: newPassword
                })
            });
            if (response.ok) {
                messageDiv.textContent = "Senha alterada com sucesso! Você será redirecionado para a página de login em breve.";
                // Remove os tokens do localStorage para garantir que o usuário seja deslogado após a alteração da senha.
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                setTimeout(() => {
                    location.href = "login.html";
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
