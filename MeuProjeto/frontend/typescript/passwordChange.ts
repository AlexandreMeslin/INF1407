addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("formulario") as HTMLFormElement;
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const messageDiv = document.getElementById("message") as HTMLDivElement;

        const currentPassword = (document.getElementById("old_password") as HTMLInputElement).value;
        const newPassword = (document.getElementById("new_password") as HTMLInputElement).value;
        const confirmPassword = (document.getElementById("confirm_password") as HTMLInputElement).value;

        if (newPassword !== confirmPassword) {
            messageDiv.textContent = "A nova senha e a confirmação não coincidem.";
            return;
        }
        
        try {
            const response = await authFetch(backendAddress + "accounts/change-password/", {
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
                messageDiv.style.color = "green";

                // Remove os tokens do localStorage para garantir que o usuário seja deslogado após a alteração da senha.
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');

                setTimeout(() => {
                    location.href = "login.html";
                }, 3000);
            } else {
                const errorData = await response.json();
                messageDiv.textContent = `Erro: ${errorData.message}`;
                messageDiv.style.color = "red";
            }
        } catch (error) {
            messageDiv.textContent = `Erro de rede: ${error}`;
            messageDiv.style.color = "red";
        }
    });
});
