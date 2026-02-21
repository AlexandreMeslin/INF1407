onload = () => {
    const form = document.getElementById("loginForm") as HTMLFormElement;

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const msg = document.getElementById("msg") as HTMLDivElement;

        const username = (document.getElementById("username") as HTMLInputElement).value;
        const password = (document.getElementById("password") as HTMLInputElement).value;

        try {
            const tokens = await login(username, password);

            localStorage.setItem("access_token", tokens.access);
            localStorage.setItem("refresh_token", tokens.refresh);

            window.location.href = "/";

        } catch (err) {

            // JEITO ERRADO (Vulnerável):
            // safeArea.innerHTML = userInput; 

            // JEITO CERTO (Seguro):
            // safeArea.textContent = userInput; // O navegador renderiza como texto puro, não como HTML

            msg.textContent = "Usuário ou senha inválidos";
        }
    });
}

async function login(username: string, password: string): Promise<JwtResposta> {
    const response = await fetch(backendAddress + "api/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    if (!response.ok) {
        throw new Error("Login inválido");
    }

    return await response.json();
}
