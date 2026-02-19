"use strict";
onload = () => {
    const form = document.getElementById("loginForm");
    const msg = document.getElementById("msg");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        try {
            const tokens = await login(username, password);
            localStorage.setItem("access_token", tokens.access);
            localStorage.setItem("refresh_token", tokens.refresh);
            window.location.href = "/";
        }
        catch (err) {
            msg.textContent = "Usuário ou senha inválidos";
        }
    });
};
async function login(username, password) {
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
