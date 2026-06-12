import { backendAddress } from "./constantes.js";
export async function login(username, password) {
    const response = await fetch(backendAddress + "token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });
    if (!response.ok) {
        throw new Error("Login inválido");
    }
    return await response.json();
}
