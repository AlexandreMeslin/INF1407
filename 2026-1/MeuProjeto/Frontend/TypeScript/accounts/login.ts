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
      msg.textContent = "Usuário ou senha inválidos";
    }
  });
}

/**
 * Função para realizar o login do usuário, enviando as credenciais para o backend e recebendo os tokens JWT em resposta.
 * @param username username
 * @param password senha
 * @returns promise JSON
 */
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