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
onload = () => {
    const form = document.getElementById("loginForm");
    form.addEventListener("submit", (e) => __awaiter(void 0, void 0, void 0, function* () {
        e.preventDefault();
        const msg = document.getElementById("msg");
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        try {
            const tokens = yield login(username, password);
            localStorage.setItem("access_token", tokens.access);
            localStorage.setItem("refresh_token", tokens.refresh);
            window.location.href = "/";
        }
        catch (err) {
            msg.textContent = "Usuário ou senha inválidos";
        }
    }));
};
function login(username, password) {
    return __awaiter(this, void 0, void 0, function* () {
        const response = yield fetch(backendAddress + "api/token/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });
        if (!response.ok) {
            throw new Error("Login inválido");
        }
        return yield response.json();
    });
}
